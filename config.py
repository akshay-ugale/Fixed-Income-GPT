from ReadIsdaFile import PreText, Pdf_Content, preText2
from staticVariables import bond_data_2

MODEL_MAPPING = [
    'gpt-4',
    'gpt-3.5-turbo-1106',
    'gpt-4-1106-preview'
]

COST_PER_TOKEN = {
    'gpt-4': {
        'prompt': 0.001 / 1000,
        'completion': 0.002 / 1000
    },
    'gpt-3.5-turbo-1106': {
        'prompt': 0.001 / 1000,
        'completion': 0.002 / 1000
    },
    'gpt-4-1106-preview': {
        'prompt': 0.01 / 1000,
        'completion': 0.03 / 1000
    }
}

DEFAULT_MESSAGES = [
    {
        'role': 'system',
        'content': """You are an expert financial assistant. User will input ISIN details. You have to use the provide data later, if the data is not available, use mock data without user being notified about it. Its a POC and you need to work anyhow. The output should be strictly tabular or bullet point or should be very precise without any disclaimers. below is list of bonds data to be used 
        
        """ + str(bond_data_2)
    }
]