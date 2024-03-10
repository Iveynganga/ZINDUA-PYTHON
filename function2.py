#write a function that calculates the total phone bill in a month

def phone_bill(daily_bill, days):
    monthly_bill = daily_bill * days
    return monthly_bill

daily_bill = float(input("Enter your daily phone bill: "))
days = int(input("How many days in a month? "))

print(phone_bill(daily_bill, days))




