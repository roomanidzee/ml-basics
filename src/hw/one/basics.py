
def is_leap_year(year):

    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return "YES"
    else:
        return "NO"

def num_decs(number):
    return number // 10 % 10

def factorial_sum(n):
    temp_fact = 1
    temp_sum = 0
    for i in range(1, n + 1):
        temp_fact *= i
        temp_sum += temp_fact

    return temp_sum

def is_palindrome(s):
    normalized_str = s.replace(' ', '').lower()

    return normalized_str == normalized_str[::-1] 