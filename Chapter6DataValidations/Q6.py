message = input("Enter a message: ")
punctuation_count = 0
for character in message:
    if not character.isalnum() and not character.isspace()):
        punctuation_count += 1
print(punctuation_count)
