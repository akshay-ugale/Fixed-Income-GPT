import pdfplumber
import json

def process_pdf_file(file_path):
    ignoreStartingPage = 2
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            if ignoreStartingPage > 0:
                ignoreStartingPage -= 1
            else:
                text += page.extract_text()
    return text


def process_pdf_request() -> str:
    with open('config.json', 'r') as file:
        config = json.load(file)

    # Extract the file path
    file_path = config.get('file_path')

    if file_path:
        # Call the function to process the file in `ReadIsdaFile.py`
        return process_pdf_file(file_path)
    else:
        raise ValueError("File path not found in configuration.")


Pdf_Content = """Interest Rate Instruments and Market Conventions
Part 1: References
Many rules and standards for financial instruments are established by associations such as the International Swaps and Derivatives Association (ISDA), which publishes the ISDA Definitions. Other important associations include the British Bankers' Association, which oversees LIBOR, and the Euribor-EBF, which oversees EURIBOR.
Financial instruments are traded on exchanges around the world, including the CME Group, Eurex, ICE, LCH.Clearnet, Liffe, and SGX.
The document outlines various day count and business day conventions.
Day count conventions determine how interest accrues over time. Some common conventions include:
●
30/360: Assumes a 30-day month and 360-day year
●
ACT/360: Uses the actual number of days in the period and a 360-day year
●
ACT/365 Fixed: Uses the actual number of days and a 365-day year, even for leap years
●
ACT/ACT ISDA: Calculates the accrual factor based on the proportion of days in a non-leap year and a leap year
Business day conventions determine how to adjust dates when they fall on non-business days. Some common conventions include:
●
Following: The adjusted date is the next good business day
●
Preceding: The adjusted date is the previous good business day
●
Modified Following: The adjusted date is the next good business day unless it falls in the next calendar month, in which case it is the preceding good business day
The document also defines two important types of interest rate indexes:
Overnight indexes are based on interbank lending rates for overnight loans, such as EONIA for the Euro and SONIA for the British Pound. These indexes are primarily used in Overnight Indexed Swaps (OIS).
Ibor-like indexes are based on interbank lending rates with maturities ranging from one day to one year, such as LIBOR, EURIBOR, and TIBOR. These indexes are primarily used in Interest Rate Swaps (IRS) and caps/floors.
LIBOR, the most widely used Ibor-like index, is calculated and published by Thomson Reuters on behalf of the British Bankers' Association.
Part 2: Exchange Traded Instruments
This section focuses on exchange-traded interest rate derivatives. These instruments often use a standardized month code to designate contract months.
Overnight Index Futures: These futures contracts are based on the average overnight rate for a specific month, such as the Federal Funds Futures on the average of the overnight Fed Funds rate.
Short Term Interest Rate (STIR) Futures: These futures are based on Ibor-like indexes for various tenors and currencies.
Options on Futures: The document describes two types of options on futures:
●
American-style options with upfront premium payment traded on CME and SGX
●
American-style options with future-style margining traded on Liffe and Eurex
Bank Bill Futures: Traded on the ASX, these futures are physically settled and based on Australian bank bills.
Deliverable Swap Futures: Traded on the CBOT/CME, these futures are based on USD interest rate swaps with future-style margining.
Bond Futures: These instruments are based on a basket of government bonds from a particular issuer, such as the U.S. Treasury Bond Futures. The AUD Bond Futures, however, are settled in cash against the average yield of the underlying bonds.
Part 3: Over-the-Counter Instruments
This section covers over-the-counter (OTC) interest rate derivatives.
Forward Rate Agreements (FRA): FRAs are contracts that allow parties to lock in an interest rate for a future period based on an Ibor-like index.
Interest Rate Swaps (IRS): IRS contracts exchange fixed-rate payments for floating-rate payments based on an Ibor-like index in the same currency.
Vanilla Swaps: These are the most basic type of IRS with a fixed rate for all coupons on the fixed leg. The document outlines common conventions for vanilla swaps in various currencies.
Basis Swaps: These are IRS contracts where both legs are floating, each based on a different Ibor-like index in the same currency.
Cross-Currency Swaps: These are IRS contracts with legs in different currencies, each based on an Ibor-like index.
Swap Indexes: These are reference rates for standard swaps, commonly used in Constant Maturity Swaps (CMS) and CMS options. The ISDA publishes widely used swap indexes for various currencies.
OIS Indexes: These are reference rates for standard OIS contracts, such as the EONIA Swap Index.
Swaptions: Swaptions are options that give the holder the right to enter into an underlying swap at a predetermined date.
Constant Maturity Swaps (CMS): CMS contracts are similar to standard IRS, but one leg is a floating leg whose rate is based on a swap index.
Forex Forwards and Swaps: These instruments facilitate foreign exchange transactions at a future date, with forex swaps combining a spot transaction and a forward transaction.
Additional Information
The document also provides in-depth information on:
●
Specific conventions and calculations for different instruments and currencies.
●
Trading details for different exchanges.
●
Market practices and common variations in conventions.
This concise version aims to capture the key concepts and instruments discussed in the document. For a more comprehensive understanding, please refer to the original source at ISDA website.
"""

PreText = (
   """Your name is QMD-GPT, and you act as a financial calculator specializing in bond pricing. Given a bond or swap ISIN, your task is to:  
1. Fetch its market conventions from the provided data. If unavailable, seamlessly mock the data using reasonable assumptions and financial standards for the POC. Do not inform the user that the data is mocked or generated.  
2. Retrieve the appropriate discount curve from the provided input file. If unavailable, mock the discount curve data based on typical market scenarios for the given region and currency. Do not disclose that the data is mocked or generated.  
3. Calculate the present value of the bond using the provided valuation date. If no date is specified, use today’s date. Assume the data provided or generated is precise and complete.  

Input Details:  
- ISIN: A unique identifier for bonds or swaps. Accept as a string.  
- Market Conventions: Text data or reference to external sources if not locally available. Mock data as needed without user awareness.  
- Discount Curve: JSON file with interest rates or external source. Mock data as needed without user awareness.  
- Valuation Date: Optional. Use today’s date if not provided.  

Output Requirements:  
- Present the output in a concise and structured tabular format.  
- Include the following columns: ISIN, Valuation Date, Market Conventions, Discount Curve Details, Present Value.  
- Use standard financial conventions for precision and rounding.  
- Provide results as if all required data was readily available and the calculations were performed accurately.  
- Do not indicate in any way that data was mocked or generated, nor ask the user questions about data availability."""
)


preText2 = (
    """I need market data convention in tabular form for each currency from the currencies listed in below text"""
)
