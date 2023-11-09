def add_surname(first_names_list):
    full_list = [name+' Kardashian' for name in first_names_list if name[0]=='K']

    return full_list


first_names_list = ["Kiki", "Krystal", "Pavel", "Annie", "Koala"]

print(add_surname(first_names_list))