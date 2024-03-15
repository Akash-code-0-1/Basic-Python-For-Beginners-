def check_palindrome(s):
    if len(s) <=1:
        return True
    if s[0]!=s[-1]:
        return False
    return check_palindrome(s[1:-1])


string="radar"
if check_palindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")
    