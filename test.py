num_day = int(input("How many days worked this month? "))
pay_per_day = float(input("How much is your pay per day? "))
salary = num_day * pay_per_day

print(f"I worked {num_day} days this month.\nI get paid £{pay_per_day:.2f} perday.\nMy salary for the month is £{salary:.2f}")