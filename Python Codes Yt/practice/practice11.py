def is_palindrome(word):
    word = word.lower()
    new_word = ""
    for ch in word:
        if ch.isalnum():
            new_word+=ch
    if new_word == new_word[::-1]:
        return True

    else:
        return False

word = input("Enter The Word  :")
if is_palindrome(word):
    print("PALINDROME")

else:
    print("NOT A PALINDROME")