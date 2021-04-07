input_str = input("Please enter a string: ").lower()
if input_str == input_str[::-1]:
    print("{} is a palindrome".format(input_str))
else:
    print("{} is NOT a palindrome".format(input_str))
