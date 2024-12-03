from ReadIsdaFile import PreText, Pdf_Content, preText2
from staticVariables import bond_data, bond_data_2

MODEL_MAPPING = [
    'gpt-3.5-turbo-1106',
    'gpt-4-1106-preview'
]

COST_PER_TOKEN = {
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
        'content': """You are an expert financial assistant. User will input ISIN details. You have to use the provide data later, if the data is not available, use mock data without user being notified about it. Its a POC and you need to work anyhow. The output should be strictly tabular or bullet point. below is list of bonds data to be used {
    "SE0009241524": {
        "Security ID / Värdepappers ID": "LUNDB 1.337 1023",
        "Maturity Date": "2023-10-24",
        "Nominal": 3000000,
        "Price": 103.006,
        "Currency": "USD",
        "Coupon Frequency": "annual",
        "Face Value": 1000,
        "Coupon": 4
    },
    "SE0011281567": {
        "Security ID / Värdepappers ID": "HOLM FRN 0522",
        "Maturity Date": "2022-05-23",
        "Nominal": 10000000,
        "Price": 100.319,
        "Currency": "USD",
        "Coupon Frequency": "semi-annual",
        "Face Value": 1000,
        "Coupon": 4.5
    },
    "SE0010599001": {
        "Security ID / Värdepappers ID": "FVH FRN 0225",
        "Maturity Date": "2025-02-24",
        "Nominal": 10000000,
        "Price": 102.372,
        "Currency": "USD",
        "Coupon Frequency": "quarterly",
        "Face Value": 1000,
        "Coupon": 5.6
    },
    "XS2187707976": {
        "Security ID / Värdepappers ID": "TELE2 FRN 0625",
        "Maturity Date": "2025-06-10",
        "Nominal": 10000000,
        "Price": 102.667,
        "Currency": "USD",
        "Coupon Frequency": "annual",
        "Face Value": 1000,
        "Coupon": 4.5
    },
    "XS2160877390": {
        "Security ID / Värdepappers ID": "SCANIA FRN 0423",
        "Maturity Date": "2023-04-24",
        "Nominal": 10000000,
        "Price": 103.95,
        "Currency": "EUR",
        "Coupon Frequency": "semi-annual",
        "Face Value": 1000,
        "Coupon": 3
    },
    "XS2187605030": {
        "Security ID / Värdepappers ID": "TELIA 1.125 0625",
        "Maturity Date": "2025-06-10",
        "Nominal": 17000000,
        "Price": 102.529327,
        "Currency": "EUR",
        "Coupon Frequency": "quarterly",
        "Face Value": 1000,
        "Coupon": 4.5
    },
    "SE0014449641": {
        "Security ID / Värdepappers ID": "SKF FRN 0624",
        "Maturity Date": "2024-06-10",
        "Nominal": 20000000,
        "Price": 102.022,
        "Currency": "EUR",
        "Coupon Frequency": "annual",
        "Face Value": 1000,
        "Coupon": 4
    },
    "SE0008320964": {
        "Security ID / Värdepappers ID": "HUSQB FRN 0521",
        "Maturity Date": "2021-05-03",
        "Nominal": 3000000,
        "Price": 100.78,
        "Currency": "GBP",
        "Coupon Frequency": "quarterly",
        "Face Value": 1000,
        "Coupon": 5.6
    },
    "XS2180541703": {
        "Security ID / Värdepappers ID": "HEMSO FRN 0523",
        "Maturity Date": "2023-05-29",
        "Nominal": 10000000,
        "Price": 101.447,
        "Currency": "GBP",
        "Coupon Frequency": "annual",
        "Face Value": 1000,
        "Coupon": 4.5
    },
    "SE0012676088": {
        "Security ID / Värdepappers ID": "WILH FRN 1222",
        "Maturity Date": "2022-12-04",
        "Nominal": 12000000,
        "Price": 101.1182,
        "Currency": "GBP",
        "Coupon Frequency": "semi-annual",
        "Face Value": 1000,
        "Coupon": 3
    },
    "SE0010599308": {
        "Security ID / Värdepappers ID": "CAS FRN 0823",
        "Maturity Date": "2023-08-28",
        "Nominal": 20000000,
        "Price": 100.511,
        "Currency": "GBP",
        "Coupon Frequency": "quarterly",
        "Face Value": 1000,
        "Coupon": 4.5
    },
    "SE0012012904": {
        "Security ID / Värdepappers ID": "RIKSH FRN 1223",
        "Maturity Date": "2023-12-13",
        "Nominal": 10000000,
        "Price": 101.887,
        "Currency": "GBP",
        "Coupon Frequency": "annual",
        "Face Value": 1000,
        "Coupon": 4.5
    }
}"""
    }
]