def electricity_bill(units):
    if units < 0:
        return "Invalid Units"
    elif units <= 100:
        bill = units * 2 + 50
    elif units <= 200:
        bill = 200 + (units - 100) * 3 + 50
    else:
        bill = 500 + (units - 200) * 5 + 50

    return bill


print(electricity_bill(0))
print(electricity_bill(50))
print(electricity_bill(100))
print(electricity_bill(150))
print(electricity_bill(250))