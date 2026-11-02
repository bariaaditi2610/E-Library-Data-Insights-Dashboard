# E-Library Data Analysis Dashboard

## Project Description
This project is a Python-based E-Library Data Analysis Dashboard that loads library transaction data from a CSV file and provides statistics, filtering, reports, and data visualizations.

## Features
- Load library transaction data from CSV
- View dataset statistics
- Filter records by genre
- Generate a summary report (`report.txt`)
- Display charts: Bar Chart, Line Graph, Pie Chart, Heatmap

## Technologies Used
- Python 3
- pandas
- NumPy
- matplotlib
- seaborn

## Files
- `library_dashboard (1).py` - Main program
- `README.md` - Project documentation
- `report.txt` - Summary report file
- `requirements.txt` - Python dependencies
- `terminal_output.txt` - Last run terminal command and exit status

## How to Run
1. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the program:
   ```bash
   python "library_dashboard (1).py"
   ```
3. Follow the interactive menu to load your CSV file and choose analysis options.

## Expected CSV Columns
The input CSV should include at least:
- `Borrowing_Duration`
- `Genre`
- `Date`

## Output
- Console statistics for borrowing duration
- Filtered transaction records by genre
- Genre-level borrowing duration report
- Visual charts for genre distribution and trends

## Notes
- `Date` values are parsed for the line graph.
- The script uses interactive menu input and opens matplotlib windows for plots.
- If you rename or move the script file, update the run command accordingly.

## Author
Hasmukh Parmar