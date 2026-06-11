text = input("input: ")
print("output: " , end =" ")
for letter in text: 
    if letter not in "aeiou AEIOU":
        print(letter , end =" ")

        print()