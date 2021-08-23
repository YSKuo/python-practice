names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
new_list = [name.upper() for name in names if len(name) > 5]
print(new_list)
