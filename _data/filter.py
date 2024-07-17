import pandas as pd
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required = True, help = "Input file")
    parser.add_argument("--output", "-o", type=str, required = True, help = "Output file")
    args = parser.parse_args()

    data = pd.read_csv(args.input)
    filtered = data[data["num submitted reviews"] > 0]
    filtered = filtered[['name', 'institution name']]
    filtered.rename(columns={'institution name': 'company'}, inplace=True)
    filtered.to_csv(args.output, index = False)

