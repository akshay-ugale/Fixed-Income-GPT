import json

bond_data_2 = {
    "US0009241524": {
        "Security ID / Värdepappers ID": "LUNDB 1.337 1023",
        "Maturity Date": "2023-10-24",
        "Nominal": 3000000,
        "Price": 103.006,
        "Currency": "USD",
        "Coupon Frequency": "annual",
        "Face Value": 1000,
        "Coupon": 4
    },
    "USE0011281567": {
        "Security ID / Värdepappers ID": "HOLM FRN 0522",
        "Maturity Date": "2022-05-23",
        "Nominal": 10000000,
        "Price": 100.319,
        "Currency": "USD",
        "Coupon Frequency": "semi-annual",
        "Face Value": 1000,
        "Coupon": 4.5
    },
    "US0010599001": {
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
}

# Convert dictionary to JSON string
# bond_data = json.dumps(bond_data_string, indent=4)

market_conventions = {
    "USD": {
        "Day Count Convention": "30/360",
        "Discounting Method": "Annual",
        "Interest Calculation Method": "Simple",
        "Compounding Frequency": "Annual"
    },
    "EUR": {
        "Day Count Convention": "Actual/360",
        "Discounting Method": "Annual",
        "Interest Calculation Method": "Simple",
        "Compounding Frequency": "Annual"
    },
    "GBP": {
        "Day Count Convention": "Actual/365",
        "Discounting Method": "Annual",
        "Interest Calculation Method": "Simple",
        "Compounding Frequency": "Annual"
    }
}

# market_conventions = json.dumps(market_conventions_strng, indent=4)

# Sample yield curve data (replace with actual data)
yield_curve = {
    "USD": {
        "0.5": 2.50,
        "1.0": 2.70,
        "1.5": 2.90,
        "2.0": 3.00,
        "3.0": 3.10,
        "5.0": 3.20,
        "7.0": 3.25,
        "10.0": 3.30,
        "15.0": 3.40,
        "20.0": 3.50,
        "25.0": 3.55,
        "30.0": 3.60
    },
    "EUR": {
        "0.5": 1.00,
        "1.0": 1.20,
        "1.5": 1.30,
        "2.0": 1.40,
        "3.0": 1.50,
        "5.0": 1.60,
        "7.0": 1.70,
        "10.0": 1.80,
        "15.0": 2.00,
        "20.0": 2.10,
        "25.0": 2.20,
        "30.0": 2.30
    },
    "GBP": {
        "0.5": 3.00,
        "1.0": 3.10,
        "1.5": 3.20,
        "2.0": 3.25,
        "3.0": 3.30,
        "5.0": 3.40,
        "7.0": 3.50,
        "10.0": 3.60,
        "15.0": 3.80,
        "20.0": 3.90,
        "25.0": 4.00,
        "30.0": 4.10
    }
}
#yield_curve = json.dumps(yield_curve_str, indent=4)