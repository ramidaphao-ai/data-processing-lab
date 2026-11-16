# OOP Data Processing Lab

## Lab Overview
This lab converts procedural data processing code into object-oriented programming (OOP) using Python. It focuses on loading, filtering, aggregating, storing, and joining data from CSV files.

## Project Structure
```text
data-processing-lab/
├── README.md
├── Cities.csv
├── Countries.csv
└── data_processing.py
```

## Design Overview

### DataLoader Class
Loads CSV data as a list of dictionaries.

**Attributes:**
- `base_path`: Directory containing the CSV files.

**Methods:**
- `__init__()`: Initializes the base path.
- `load_csv()`: Reads data from a CSV file.

### Table Class
Stores and processes tabular data.

**Attributes:**
- `table_name`: Name of the table.
- `table`: List of dictionaries containing the data.

**Methods:**
- `__init__()`: Initializes the table.
- `filter()`: Filters rows based on a condition.
- `aggregate()`: Applies a function to a selected column.
- `join()`: Combines two tables using a common key.
- `__str__()`: Returns a string representation of the table.

### DB Class
Manages multiple tables in a database.

**Attributes:**
- `tables`: A list of Table objects.

**Methods:**
- `__init__()`: Initializes an empty database.
- `insert()`: Adds a table to the database.
- `search()`: Searches for a table by its name.

## Commit 4 Updates
This commit adds database management and table joining.

The `Countries.csv` dataset is used together with `Cities.csv` to analyze cities and countries.

The program can:
- Store and search multiple tables.
- Join tables using the country column.
- Filter joined data.
- Calculate aggregate values from the results.

## How to Test and Run
1. Install Python 3.
2. Open the project folder.
3. Make sure `Cities.csv` and `Countries.csv` are in the same folder as `data_processing.py`.
4. Run the following command:

   ```bash
   python3 data_processing.py
   ```

5. Check the results in the terminal and compare them with the expected output provided in the lab instructions.