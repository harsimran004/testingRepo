def check_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_sign(10))  


def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(11)) 


def divisible_by_3_and_5(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Divisible by 3 and 5"
    else:
        return "Not divisible by 3 and 5"

print(divisible_by_3_and_5(15))  


def largest_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(largest_of_three(3, 5, 4))  


def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

print(check_leap_year(2024))  


def is_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

print(is_palindrome("madam"))  


def is_prime(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

print(is_prime(29))  


def can_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

print(can_vote(17)) 


def check_century(year):
    if 2001 <= year <= 2100:
        return "21st Century"
    else:
        return "Not 21st Century"

print(check_century(2025))  


def check_range(num, start, end):
    if start <= num <= end:
        return f"{num} is within the range {start} and {end}"
    else:
        return f"{num} is outside the range {start} and {end}"

print(check_range(7, 5, 10))  

