# Optimal Exchange Project

This project implements a solution to calculate the optimal exchange (minimum number of coins needed) for values up to a given amount `K`, using a provided set of coin denominations. It evaluates multiple test cases to determine the average and maximum number of coins required to form all values from 1 to `K`.

## Project Structure

```text
optimal_exchange/
├── inputs/           # Directory containing input text files (e.g., case1.txt, case2.txt)
├── outputs/          # Directory where the parsed results will be saved
├── src/
│   ├── main.py       # Main interactive script to run the application
│   ├── solution.py   # Core logic to find the optimal coin exchanges
│   └── utils.py      # Utility functions for file I/O operations
└── README.md         # Project documentation
```

## How It Works

The program is a command-line interface (CLI) application that reads test cases from files located in the `inputs/` directory.

### Input Format
Each input file should follow this structure:
- **First line:** The total number of test cases `N`.
- **Following `N` lines:** Space-separated integers. 
  - The first integer is `K` (the maximum value to evaluate).
  - The second integer is `size` (the number of available coin denominations).
  - The rest of the integers are the actual coin denominations.

Example (`inputs/case1.txt`):
```text
3
100 6 1 2 5 10 20 50
100 6 1 3 10 15 51 84
100 6 1 4 9 16 25 36
```

### Core Logic (`solution.py`)
1. Parses the input parameters.
2. Sorts the coin denominations.
3. Processes values iteratively from 1 to `K`, determining the minimal number of coins to produce each value.
4. Returns a summarized result for each test case formatted as `Average_Value Max_Value`.

### Output
The application generates an output file for each processed input inside the `outputs/` folder (e.g. `outputs/case1.txt.out`). The output file contains the `Average_Value` and `Max_Value` on a new line for each corresponding test case.

## Execution Steps

### Prerequisites
- Minimal requirement is a stable installation of **Python 3**.

### Running the application
1. Ensure your terminal or command prompt is located at the root of the project (`optimal_exchange/`).
2. Make sure you have your input files defined inside the `inputs/` folder.
3. Run the following command:
   ```bash
   python src/main.py
   ```
4. The application will prompt an interactive menu listing all available inputs:
   ```text
   --- Inputs Menu ---
   1. case1.txt
   2. case2.txt
   --------------------
   ```
5. Enter the **number** corresponding to the file you want to evaluate (e.g., type `1` and press `Enter` to process `case1.txt`). Or input `0` to exit the application.
6. Check your `outputs/` folder for the newly generated `.out` files!