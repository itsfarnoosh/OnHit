# File to save meal logs
log_file = "nutrition_log.txt"

# Nutritional data (can be extended or read from a CSV file)
nutritional_data = {
    "chicken": {"calories": 165, "protein": 31, "carbs": 0, "fats": 3.6},
    "rice": {"calories": 130, "protein": 2.4, "carbs": 28, "fats": 0.3},
    "broccoli": {"calories": 55, "protein": 3.7, "carbs": 11, "fats": 0.6},
}

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
            ingredient_list.append((name, qty))
        except ValueError:
            print(f"Invalid input format for '{item.strip()}'. Use format 'ingredient 100g'.")
            return None  # Return None to indicate failure
    return ingredient_list
