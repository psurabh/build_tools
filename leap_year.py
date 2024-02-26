def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
def validate_input(input):
    try:
        int(input)
        return "Integer"
    except ValueError:
        return "String"
        year = None
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
            print(f"{year} is not a leap year.")
    print(f"{user_input} is a {input_type}.")
