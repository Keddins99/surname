def add_surname(first_names: list) -> list:
    return [name + " Kardashian" for name in first_names if name.startswith("K")]

# Example usage
if __name__ == "__main__":
    original_names = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
    modified_names = add_surname(original_names)
    print(modified_names)
