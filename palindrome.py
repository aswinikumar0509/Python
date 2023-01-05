def recurrev(number, rev):
    if number == 0:
        return rev

    remainder = int(number % 10)
    rev = (rev * 10) + remainder

    return recurrev(int(number / 10), rev)


num = 12321
reverse = 0
reverse = recurrev(num, reverse)

print(str(num) + " is: ", end="")
print("Palindrome") if reverse == num else print("Not Palindrome")