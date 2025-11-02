str = input("Enter the name:")
for char in set(str):
    if str.count(char) > 1:
        print(f"The '{char}' repeated {str.count(char)} times.")
        