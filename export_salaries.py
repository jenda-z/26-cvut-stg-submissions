import pandas as pd
import os

EUR_to_CZK = 24.5  # Conversion rate from EUR to CZK

def round_salary(salary):
    """Unified rounding of CZK salary to the nearest thousand."""
    return [int(s / 1000) * 1000 for s in salary]

def round_EUR_salary(salary):
    """Unified rounding of salary to the nearest hundered."""
    return [int(s / (EUR_to_CZK* 100)) * 100 for s in salary]

if __name__ == '__main__':
    # Load the Excel file
    excel_file = 'data/CR_252_MZS.xlsx'

    try:
        # PI salary range
        data = pd.read_excel(excel_file, sheet_name='MZS-M8', skiprows=5)
        filtered_data = data[data.iloc[:, 0].astype(str).str.contains('1223 Řídící pracovníci v oblasti výzkumu a vývoje', na=False)]

        PI_salary = [
            max( filtered_data['1. kvartil'].values[0], 60000 ),
            filtered_data['Unnamed: 2'].values[0],
        ]

        print( 'PI salary:', round_salary(PI_salary), 
               ' EUR ', round_EUR_salary(PI_salary) )

        filtered_data = data[data.iloc[:, 0].astype(str).str.contains('23101 Vědečtí, výzkumní a vývojoví pracovníci na vysokých školách', na=False)]

        Postdoc_salary = [
            filtered_data['3. kvartil'].values[0],
            filtered_data['9. decil'].values[0],
        ]

        print( 'Postdoc salary:', round_salary(Postdoc_salary),
               ' EUR ', round_EUR_salary(Postdoc_salary) )

        filtered_data = data[data.iloc[:, 0].astype(str).str.contains('23101 Vědečtí, výzkumní a vývojoví pracovníci na vysokých školách', na=False)]

        PhD_salary = [
            max( filtered_data['1. kvartil'].values[0], 45000 ),
            filtered_data['průměr'].values[0],
        ]

        print( 'PhD candidate salary:', round_salary(PhD_salary),
                ' EUR ', round_EUR_salary(PhD_salary) )

        filtered_data = data[data.iloc[:, 0].astype(str).str.contains('23101 Vědečtí, výzkumní a vývojoví pracovníci na vysokých školách', na=False)]

        technician_salary = [
            filtered_data['1. kvartil'].values[0],
            filtered_data['Unnamed: 2'].values[0],
        ]
        print( 'Technician salary: CZK ', round_salary(technician_salary), 
                ' EUR ', round_EUR_salary(technician_salary) )

    except Exception as e:
        print(f"Error reading Excel file: {e}")
        exit(1)