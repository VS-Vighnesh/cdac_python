def check_vowel(char):
    match char:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            return "Yes, it is a vowel"
        case _:
            return "No, it's not a vowel"

x = input("Enter the character to check whether it's a vowel or not: ").lower()
out = check_vowel(x)
print(f"The character {x} {out}")
