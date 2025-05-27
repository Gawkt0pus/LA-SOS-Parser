# Louisiana SOS Parser

Parses publicly available business registration data from the Louisiana Secretary of State (SOS) into a structured CSV format.

## Features

- Parses `.txt` files containing business registration data from Louisiana SOS
- Extracts key information including:
  - Business name and address
  - Filing number and date
  - Registered agent details
  - Officer/Member/Manager information (up to 5 officers)
- Outputs clean, structured CSV data
- Handles UTF-8 encoding for proper character support

## Requirements

- Python 3.x
- No external dependencies required (uses built-in `re` and `csv` modules)

## Usage

1. Place your Louisiana SOS `.txt` file in the desired directory
2. Update the `input_file` and `output_file` paths in the script
3. Run the script:
   ```bash
   python la_sos_parser.py
