# File to save meal logs
log_file = "nutrition_log.txt"

# Nutritional data (can be extended or read from a CSV file)
nutritional_data = {
    "chicken": {"calories": 165, "protein": 31, "carbs": 0, "fats": 3.6},
    "rice": {"calories": 130, "protein": 2.4, "carbs": 28, "fats": 0.3},
    "broccoli": {"calories": 55, "protein": 3.7, "carbs": 11, "fats": 0.6},
}

def handle_missing_ingredient(ingredient):
    """
    Handle the case where the ingredient is not found in the nutritional data.
    Allows the user to either change the ingredient or add nutritional data.

    Args:
        ingredient (str): The missing ingredient name.

    Returns:
        bool: True if the ingredient was added to the nutritional data, False otherwise.
    """
    print(f"\nNutritional data for '{ingredient}' not found.")
    print("1. Change ingredient")
    print("2. Add ingredient data")
    print("3. Skip ingredient")

    while True:
        choice = input("Choose an option (1, 2, or 3): ").strip()
        if choice == "1":
            return False  # User opts to change the ingredient
        elif choice == "2":
            try:
                print(f"Enter nutritional data for '{ingredient}':")
                calories = float(input("Calories (per 100g): ").strip())
                protein = float(input("Protein (g per 100g): ").strip())
                carbs = float(input("Carbs (g per 100g): ").strip())
                fats = float(input("Fats (g per 100g): ").strip())
                nutritional_data[ingredient] = {
                    "calories": calories,
                    "protein": protein,
                    "carbs": carbs,
                    "fats": fats,
                }
                print(f"Data for '{ingredient}' added successfully.")
                return True
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "3":
            print(f"Skipping '{ingredient}'.")
            return False
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

def get_ingredients():
    """
    Prompt the user for ingredients and quantities.
    
    Returns:
        list of tuples: (ingredient_name, quantity_in_grams)
    
    Time Complexity: O(n)
        Where n is the number of ingredients entered by the user.
    """
    ingredients = input("Enter ingredients and quantities (e.g., 'chicken 100g, rice 200g'): ").strip()
    ingredient_list = []
    for item in ingredients.split(","):
        try:
            name, qty = item.strip().rsplit(" ", 1)
            qty = float(qty.strip("g"))
            while name not in nutritional_data:
                if not handle_missing_ingredient(name):
                    print(f"Re-enter the ingredient or skip it: {name}")
                    break
            else:
                ingredient_list.append((name, qty))
        except ValueError:
            print(f"Invalid input format for '{item.strip()}'. Use format 'ingredient 100g'.")
            return None  # Return None to indicate failure
    return ingredient_list


def calculate_nutrition(ingredient_list):
    """
    Calculate the total nutritional value of the meal.
    
    Args:
        ingredient_list (list): List of tuples (ingredient_name, quantity_in_grams)
    
    Returns:
        dict: Total nutrition (calories, protein, carbs, fats)
    
    Time Complexity: O(n)
        Where n is the number of ingredients in the list.
    """
    total_nutrition = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0}
    for name, qty in ingredient_list:
        qty_factor = qty / 100
        if name in nutritional_data:
            total_nutrition["calories"] += nutritional_data[name]["calories"] * qty_factor
            total_nutrition["protein"] += nutritional_data[name]["protein"] * qty_factor
            total_nutrition["carbs"] += nutritional_data[name]["carbs"] * qty_factor
            total_nutrition["fats"] += nutritional_data[name]["fats"] * qty_factor
    return total_nutrition


def save_meal(date, meal, nutrition):
    """
    Save the meal and its nutritional data to a text file.
    
    Args:
        date (str): Date of the meal (YYYY-MM-DD)
        meal (str): Name of the meal
        nutrition (dict): Nutritional data

    """
    


def weekly_summary():
    """
    Display the weekly nutritional summary.
    Reads data from the log file and calculates totals.

    """
    



def main():
    """
    Main menu for the Nutritional Insights Tracker.
    
    Time Complexity: O(1) for handling the menu loop and user input.
    """
    while True:
        print("\n=== Nutritional Insights Tracker ===")
        print("1. Add a meal")
        print("2. View weekly summary")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            meal = input("Enter the meal name: ")
            ingredient_list = get_ingredients()
            if ingredient_list:
                nutrition = calculate_nutrition(ingredient_list)
                save_meal(date, meal, nutrition)
        elif choice == "2":
            weekly_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
