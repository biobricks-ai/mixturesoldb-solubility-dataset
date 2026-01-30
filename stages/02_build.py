import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os
import re

def clean_column_name(col):
    # Remove parenthesis and content inside if it's units, or just replace with underscore
    # Actually, the columns have units in parens like (mole_fraction).
    # Let's replace brackets/parens with underscores and lower case
    col = col.lower()
    col = re.sub(r'[\(\)]', '_', col)
    col = re.sub(r'[^a-z0-9_]', '_', col)
    col = re.sub(r'_+', '_', col)
    col = col.strip('_')
    return col

def build_brick():
    input_file = "download/MixtureSolDB.csv"
    output_dir = "brick"
    output_file = os.path.join(output_dir, "data.parquet")
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    df = pd.read_csv(input_file)
    
    # Rename columns map
    # Specifically map the main SMILES to 'smiles'
    rename_map = {
        'SMILES_Solute': 'smiles',
        'SMILES_Solvent1': 'smiles_solvent1',
        'SMILES_Solvent2': 'smiles_solvent2',
    }
    
    # Rename specific columns first
    df = df.rename(columns=rename_map)
    
    # Clean up other column names
    new_columns = [clean_column_name(c) for c in df.columns]
    df.columns = new_columns
    
    # Ensure types
    # Temperature_K -> temperature_k (float)
    # Solubility -> float
    # Fraction -> float
    
    # Save to parquet
    table = pa.Table.from_pandas(df)
    pq.write_table(table, output_file)
    
    print(f"Build complete. Saved to {output_file}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"Shape: {df.shape}")

if __name__ == "__main__":
    build_brick()
