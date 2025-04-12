import pandas as pd
import re

# File paths
input_file = "./pxNnaw-ZQISM0G2-wkxF_g.csv"
output_file = "./convertkit_ready_v3.csv"

# Read the CSV file
df = pd.read_csv(input_file)

# Identify the email column dynamically
email_column = None
for col in df.columns:
    if "email" in col.lower():  # Find column with "email" in the name
        email_column = col
        break

# If no email column is found, stop execution
if email_column is None:
    print("⚠️ No email column found in the CSV file. Exiting...")
else:
    # Email validation regex
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$'

    # Function to extract and clean first name
    def extract_first_name(email):
        name_part = email.split("@")[0]  # Get part before '@'
        if '.' in name_part:
            name_part = name_part.split('.')[0]  # Take part before '.'
        else:
            name_part = name_part[:6]  # Take first 6 characters if no '.'
        name_part = ''.join(filter(str.isalpha, name_part))  # Remove digits
        return name_part.capitalize() if name_part else "Unknown"

    # Filter valid emails
    df = df[df[email_column].apply(lambda x: bool(re.match(email_regex, str(x))))]

    # Remove duplicates
    df.drop_duplicates(subset=[email_column], inplace=True)

    # Add First Name column
    df["First Name"] = df[email_column].apply(extract_first_name)

    # Keep only "Email" and "First Name" columns
    df = df[[email_column, "First Name"]]

    # Rename email column to "Email"
    df.rename(columns={email_column: "Email"}, inplace=True)

    # Save the cleaned file
    df.to_csv(output_file, index=False)

    print(f"✅ CSV file cleaned and saved as: {output_file}")