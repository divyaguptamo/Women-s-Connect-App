import tkinter as tk
from tkinter import ttk

# Function to generate outfit recommendations
def recommend_outfit():
    age = int(age_entry.get())
    gender = gender_var.get()
    style = style_var.get()
    occasion = occasion_var.get()
    weather = weather_var.get()
    body_type = body_type_var.get()

    # Outfit recommendation logic based on user inputs
    outfit = ""
    
    if style == "Casual":
        if gender == "Male":
            if weather == "Summer":
                outfit = "T-shirt with shorts and sneakers"
            elif weather == "Winter":
                outfit = "Sweater with jeans and boots"
            else:
                outfit = "Hoodie with waterproof pants and sneakers"
        else:
            if weather == "Summer":
                outfit = "Flowy dress with sandals"
            elif weather == "Winter":
                outfit = "Cozy sweater with leggings and boots"
            else:
                outfit = "Raincoat with jeans and waterproof boots"
    
    elif style == "Dressy":
        if gender == "Male":
            outfit = "Blazer with trousers and dress shoes"
        else:
            outfit = "Elegant gown with heels and accessories"

    elif style == "Professional":
        if gender == "Male":
            outfit = "Formal shirt with trousers and leather shoes"
        else:
            outfit = "Blouse with pencil skirt and heels"
    
    # Display the recommendation
    result_label.config(text=f"Recommended Outfit: {outfit}")

# Create the main window
root = tk.Tk()
root.title("Outfit Recommendation System")
root.geometry("400x450")

# Age Input
tk.Label(root, text="Enter Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Gender Selection
tk.Label(root, text="Select Gender:").pack()
gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"])
gender_dropdown.pack()

# Style Selection
tk.Label(root, text="Select Style:").pack()
style_var = tk.StringVar()
style_dropdown = ttk.Combobox(root, textvariable=style_var, values=["Casual", "Dressy", "Professional"])
style_dropdown.pack()

# Occasion Selection
tk.Label(root, text="Select Occasion:").pack()
occasion_var = tk.StringVar()
occasion_dropdown = ttk.Combobox(root, textvariable=occasion_var, values=["Party", "Meeting", "Wedding", "Casual Outing"])
occasion_dropdown.pack()

# Weather Selection
tk.Label(root, text="Select Weather:").pack()
weather_var = tk.StringVar()
weather_dropdown = ttk.Combobox(root, textvariable=weather_var, values=["Summer", "Winter", "Rainy"])
weather_dropdown.pack()

# Body Type Selection
tk.Label(root, text="Select Body Type:").pack()
body_type_var = tk.StringVar()
body_type_dropdown = ttk.Combobox(root, textvariable=body_type_var, values=["Slim", "Athletic", "Plus-size"])
body_type_dropdown.pack()

# Submit Button
submit_btn = tk.Button(root, text="Get Recommendation", command=recommend_outfit, bg="lightblue")
submit_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
result_label.pack(pady=10)

# Run the Tkinter GUI
root.mainloop()
