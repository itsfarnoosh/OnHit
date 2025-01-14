import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Nutritional data (can be extended or read from a CSV file)
nutritional_data = {
    "chicken": {"calories": 165, "protein": 31, "carbs": 0, "fats": 3.6},
    "rice": {"calories": 130, "protein": 2.4, "carbs": 28, "fats": 0.3},
    "broccoli": {"calories": 55, "protein": 3.7, "carbs": 11, "fats": 0.6},
}

# File to save meal logs
log_file = "nutrition_log.txt"

class NutritionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nutritional Insights Tracker")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        """Set up the main interface."""
        tk.Label(self.root, text="Nutritional Insights Tracker", font=("Arial", 18, "bold"), fg="#808000").pack(pady=15)

        button_style = {"bg": "#ffe9e1", "fg": "#f6a192", "font": ("Arial", 12, "bold"), "relief": "raised"}

        tk.Button(self.root, text="Add a Meal", command=self.add_meal, **button_style).pack(pady=10)
        tk.Button(self.root, text="View Weekly Summary", command=self.view_summary, **button_style).pack(pady=10)
        tk.Button(self.root, text="Help", command=self.show_help, **button_style).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.on_closing, bg="#ffe9e1", fg="#f6a192", font=("Arial", 12, "bold"), relief="raised").pack(pady=10)

    def add_meal(self):
        """Add a meal to the log."""
        date = simpledialog.askstring("Input", "Enter the date (YYYY-MM-DD):")
        if not date:
            return

        meal_name = simpledialog.askstring("Input", "Enter the meal name:")
        if not meal_name:
            return

        ingredients = simpledialog.askstring("Input", "Enter ingredients and quantities (e.g., 'chicken 100g, rice 200g'):")
        if not ingredients:
            return

        ingredient_list = self.parse_ingredients(ingredients)
        if not ingredient_list:
            return

        nutrition = self.calculate_nutrition(ingredient_list)
        self.save_meal(date, meal_name, nutrition)

    def parse_ingredients(self, ingredients):
        """Parse ingredients and handle missing ones."""
        ingredient_list = []
        for item in ingredients.split(","):
            try:
                name, qty = item.strip().rsplit(" ", 1)
                qty = float(qty.strip("g"))

                while name not in nutritional_data:
                    choice = messagebox.askquestion(
                        "Ingredient Not Found",
                        f"Nutritional data for '{name}' not found.\nDo you want to add it?",
                    )
                    if choice == "yes":
                        self.add_ingredient_data(name)
                    else:
                        break
                else:
                    ingredient_list.append((name, qty))
            except ValueError:
                messagebox.showerror("Error", f"Invalid input format for '{item.strip()}'. Use format 'ingredient 100g'.")
                return None
        return ingredient_list

    def add_ingredient_data(self, ingredient):
        """Prompt the user to add missing nutritional data."""
        try:
            calories = float(simpledialog.askstring("Input", f"Enter calories (per 100g) for {ingredient}:"))
            protein = float(simpledialog.askstring("Input", f"Enter protein (per 100g) for {ingredient}:"))
            carbs = float(simpledialog.askstring("Input", f"Enter carbs (per 100g) for {ingredient}:"))
            fats = float(simpledialog.askstring("Input", f"Enter fats (per 100g) for {ingredient}:"))
            nutritional_data[ingredient] = {
                "calories": calories,
                "protein": protein,
                "carbs": carbs,
                "fats": fats,
            }
            messagebox.showinfo("Success", f"Nutritional data for '{ingredient}' added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Invalid nutritional data entered.")

    def calculate_nutrition(self, ingredient_list):
        """Calculate the total nutritional value of a meal."""
        total_nutrition = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0}
        for name, qty in ingredient_list:
            qty_factor = qty / 100
            if name in nutritional_data:
                total_nutrition["calories"] += nutritional_data[name]["calories"] * qty_factor
                total_nutrition["protein"] += nutritional_data[name]["protein"] * qty_factor
                total_nutrition["carbs"] += nutritional_data[name]["carbs"] * qty_factor
                total_nutrition["fats"] += nutritional_data[name]["fats"] * qty_factor
        return total_nutrition

    def save_meal(self, date, meal, nutrition):
        """Save the meal and its nutritional data to a text file."""
        with open(log_file, "a") as file:
            file.write(f"{date}|{meal}|{nutrition['calories']:.2f},{nutrition['protein']:.2f},"
                       f"{nutrition['carbs']:.2f},{nutrition['fats']:.2f}\n")
        messagebox.showinfo("Success", "Meal saved successfully!")

    def view_summary(self):
        """Display the weekly nutritional summary."""
        try:
            with open(log_file, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No data found! Add meals first.")
            return

        weekly_totals = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0}
        for line in lines:
            _, _, nutrition = line.strip().split("|")
            calories, protein, carbs, fats = map(float, nutrition.split(","))
            weekly_totals["calories"] += calories
            weekly_totals["protein"] += protein
            weekly_totals["carbs"] += carbs
            weekly_totals["fats"] += fats

        summary = (
            f"Weekly Summary:\n"
            f"Calories: {weekly_totals['calories']:.2f} kcal\n"
            f"Protein: {weekly_totals['protein']:.2f} g\n"
            f"Carbs: {weekly_totals['carbs']:.2f} g\n"
            f"Fats: {weekly_totals['fats']:.2f} g"
        )
        messagebox.showinfo("Weekly Summary", summary)

    def show_help(self):
        """Display help information."""
        help_message = (
            "How to Use Nutritional Insights Tracker:\n\n"
            "1. Click 'Add a Meal' to log a new meal.\n"
            "2. Enter ingredients and their quantities.\n"
            "3. View your weekly summary using 'View Weekly Summary'.\n"
            "4. Use 'Help' for guidance."
        )
        messagebox.showinfo("Help", help_message)

    def on_closing(self):
        """Prompt the user before exiting."""
        if messagebox.askokcancel("Quit", "Do you want to exit the application?"):
            self.root.destroy()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = NutritionApp(root)
    root.mainloop()
