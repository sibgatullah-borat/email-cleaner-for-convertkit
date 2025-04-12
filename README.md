# Email Cleaner for ConvertKit

This script helps you clean and prepare email lists for importing into ConvertKit. It validates emails, extracts clean first names, and outputs a properly formatted CSV.

## 🐍 What It Does

- Reads an input CSV file with email addresses
- Validates email format using regex
- Extracts a first name from the email address (e.g. `john.doe@example.com` → `John`)
- Removes duplicates
- Outputs a clean CSV with just `Email` and `First Name` columns

---

## 💾 How to Use

### 1. Install Requirements

This script requires `pandas`:

```bash
pip install pandas
