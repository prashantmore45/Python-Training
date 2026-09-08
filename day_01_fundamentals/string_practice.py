text = input("Enter a word or sentence: ")

print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Reversed:", text[::-1])
print("Palindrome:", text == text[::-1])
print("Vowel count:", sum(1 for character in text.lower() if character in "aeiou"))
print("Word count:", len(text.split()))