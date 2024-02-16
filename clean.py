import pandas as pd
import sys

def clean_data(input1, input2, output):
    # Read the data from the CSV files
    contact_df = pd.read_csv(input1)
    other_df = pd.read_csv(input2)

    # Merge the two dataframes on the ID columns
    merged_df = pd.merge(contact_df, other_df, left_on='respondent_id', right_on='id')

    # Drop redundant column after merge
    merged_df.drop(columns='id', inplace=True)

    # Drop any rows with missing values
    merged_df.dropna(inplace=True)

    # Drop any rows where job contains 'insurance' or 'Insurance'
    merged_df = merged_df[~merged_df['job'].str.contains('insurance', case=False)]

    # Save the cleaned data to the output file
    merged_df.to_csv(output, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python clean.py <input1> <input2> <output>")
        sys.exit(1)

    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output = sys.argv[3]

    clean_data(input1, input2, output)