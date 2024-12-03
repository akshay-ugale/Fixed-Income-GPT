import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from typing import Tuple, Any
from config import MODEL_MAPPING, COST_PER_TOKEN, DEFAULT_MESSAGES
from ReadIsdaFile import process_pdf_request, Pdf_Content, PreText
from logic import get_bond_valuation

load_dotenv()

class GPTChat:
    def __init__(self, api_key: str):
        st.set_page_config(page_title='Fixed Income-GPT', page_icon='💬')
        self.client = OpenAI(api_key=api_key)
        self.MODEL_MAPPING = MODEL_MAPPING
        self.COST_PER_TOKEN = COST_PER_TOKEN
        self.DEFAULT_MESSAGES = DEFAULT_MESSAGES
        self.initialize_session_state()

    def initialize_session_state(self):
        initial_state = {
            'generated': [],
            'past': [],
            'messages': self.DEFAULT_MESSAGES.copy(),
            'model_name': [],
            'cost': [],
            'total_tokens': [],
            'total_cost': 0.0
        }
        for key, value in initial_state.items():
            st.session_state.setdefault(key, value)

    def reset_conversation(self):
        st.session_state.update({
            'generated': [],
            'past': [],
            'messages': self.DEFAULT_MESSAGES.copy(),
            'model_name': [],
            'cost': [],
            'total_tokens': [],
            'total_cost': 0.0
        })

    def generate_response(self, prompt: str, model_name: str) -> Tuple[str, Any]:
        #pdfContent = process_pdf_request()
        # header = PreText + Pdf_Content
        # st.session_state['messages'].append({'role': 'system', 'content': header})
        st.session_state['messages'].append({'role': 'user', 'content': prompt})

        # completion = self.client.chat.completions.create(
        #     model=model_name,
        #     messages=st.session_state['messages'],
        #     temperature=0,
        # )
        completion = get_bond_valuation(prompt)
        response = completion.choices[0].message.content
        st.session_state['messages'].append({'role': 'assistant', 'content': response})

        return response, completion.usage

    def process_user_input(self, user_input: str, model_name: str) -> Tuple[str, Any]:
        output, usage = self.generate_response(user_input, model_name)
        return output, usage

    def calculate_cost(self, model_name: str, usage: Any) -> float:
        return (usage.prompt_tokens * self.COST_PER_TOKEN[model_name]['prompt'] +
                usage.completion_tokens * self.COST_PER_TOKEN[model_name]['completion'])

    @staticmethod
    def display_chat_history(response_container: st.container):
        with response_container:
            for user_message, ai_message in zip(st.session_state['past'], st.session_state['generated']):
                st.chat_message(name='user', avatar='🧑').markdown(user_message)
                st.chat_message(name='ai', avatar='🤖').markdown(ai_message)

    def chat_demo(self):
        st.markdown('# Fixed Income GPT', unsafe_allow_html=True)

        model_name = st.sidebar.radio('Choose a model:', self.MODEL_MAPPING)
        counter_placeholder = st.sidebar.empty()
        counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
        if st.sidebar.button('Clear Conversation', key='clear'):
            self.reset_conversation()

        user_input = st.chat_input(placeholder='Type your message here...', key='input')
        if user_input:
            output, usage = self.process_user_input(user_input, model_name)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)
            st.session_state['model_name'].append(model_name)
            st.session_state['total_tokens'].append(usage.total_tokens)

            cost = self.calculate_cost(model_name, usage)
            st.session_state['cost'].append(cost)
            st.session_state['total_cost'] += cost

        self.display_chat_history(st.container())
        counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")

if __name__ == '__main__':
    api_key = os.getenv("OPENAI_API_KEY")  # Fetch the API key from environment variables
    gpt_chat = GPTChat(api_key)
    gpt_chat.chat_demo()