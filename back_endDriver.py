from back_end import askBot, read_dictionary

dicitonary = read_dictionary("database.txt")
query = input("Tanya apa = ").strip()
print(askBot(query,dicitonary,"Regex"))
