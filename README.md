# Nutritional Insights Tracker

The **Nutritional Insights Tracker** is a Python-based program that allows users to log meals, calculate nutritional information, and view weekly summaries. This program is designed for individuals who want to track their nutritional intake and maintain a healthy lifestyle.

---

## Features

1. **Log Meals**:
   - Add meals with ingredients and their quantities.
   - Automatically calculate the total nutritional value of the meal based on a pre-defined database.

2. **Handle Missing Ingredients**:
   - If an ingredient is not found in the database, users can:
     - Add the missing ingredient with its nutritional data.
     - Skip the ingredient.
     - Re-enter a valid ingredient.

3. **Weekly Summary**:
   - Displays the total nutritional intake for the week, including calories, protein, carbs, and fats.

4. **Error Handling**:
   - Ensures invalid inputs are handled gracefully.
   - Prompts users to correct mistakes or add missing data.

---

## Requirements

- Python 3.x

---

## How to Run

1. Clone or download this repository.
2. Ensure Python is installed on your system.
3. Open a terminal or command prompt and navigate to the folder containing the script.
4. Run the script using:
   ```bash
   python nutrition_tracker.py
   ```

---

## How to Use

### Main Menu
- After running the program, you'll see the following menu:
  ```
  === Nutritional Insights Tracker ===
  1. Add a meal
  2. View weekly summary
  3. Exit
  ```

### Adding a Meal
1. Select option `1`.
2. Enter the date (e.g., `2025-01-14`).
3. Enter the meal name (e.g., `Lunch`).
4. Enter the ingredients and their quantities in the format: `ingredient quantity` (e.g., `chicken 200g, rice 100g`).
5. If an ingredient is missing from the database, you'll be prompted to add it or skip it.

### Viewing Weekly Summary
1. Select option `2`.
2. The program will calculate and display the total nutritional values for all meals logged in the current week.

### Exiting the Program
- Select option `3` to exit the program.

---

## Nutritional Data

The program includes a pre-defined nutritional database for common ingredients (per 100g):
```python
nutritional_data = {
    "chicken": {"calories": 165, "protein": 31, "carbs": 0, "fats": 3.6},
    "rice": {"calories": 130, "protein": 2.4, "carbs": 28, "fats": 0.3},
    "broccoli": {"calories": 55, "protein": 3.7, "carbs": 11, "fats": 0.6},
}
```

Users can extend this database by adding new ingredients during runtime.

---

## File Structure

- `nutrition_tracker.py`: Main script containing the logic for the program.
- `nutrition_log.txt`: Automatically created text file to store meal logs and their nutritional values.

---

## Example Output

### Adding a Meal
```bash
=== Nutritional Insights Tracker ===
1. Add a meal
2. View weekly summary
3. Exit
Enter your choice: 1
Enter the date (YYYY-MM-DD): 2025-01-14
Enter the meal name: Dinner
Enter ingredients and quantities (e.g., 'chicken 100g, rice 200g'): chicken 200g, rice 150g
Meal saved successfully!
```

### Weekly Summary
```bash
=== Nutritional Insights Tracker ===
1. Add a meal
2. View weekly summary
3. Exit
Enter your choice: 2

Weekly Summary:
Calories: 580.00 kcal
Protein: 65.80 g
Carbs: 43.00 g
Fats: 7.50 g
```

---

## Future Improvements

1. Add support for exporting summaries as a CSV file.
2. Allow users to edit or delete logged meals.
3. Include advanced features such as goal tracking or daily calorie recommendations.

---
