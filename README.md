
# OOP Data Processing Lab

## Lab Overview
This lab converts procedural data processing code into
object-oriented programming (OOP) using Python.

## Project Structure
data-processing-lab/
├── README.md
├── Cities.csv
└── data_processing.py

## Design Overview

### DataLoader Class
Loads CSV data as a list of dictionaries.

Attributes:
- base_path: Directory containing the CSV file.

Methods:
- __init__(): Initializes the base path.
- load_csv(): Reads data from a CSV file.

### Table Class
Stores and processes tabular data.

Attributes:
- table_name: Name of the table.
- table: List of dictionaries containing the data.

Methods:
- __init__(): Initializes the table.
- filter(): Filters rows based on a condition.
- aggregate(): Applies a function to a selected column.

## How to Test and Run
1. Install Python 3.
2. Open the project folder.
3. Make sure Cities.csv is in the project folder.
4. Run the following command:

   python3 data_processing.py

5. Check the results in the terminal.
