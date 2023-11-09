def add_surname(first_names):
    return [name + " Kardashian" for name in first_names if name.startswith("K")]

original_names = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
modified_names = add_surname(original_names)
print(modified_names)
