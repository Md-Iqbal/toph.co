def leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return "Yes"
            else:
                return "No"
        else:
            return "Yes"
    else:
        return "No"
print(leap_year(int(input())))