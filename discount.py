from datetime import datetime

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()

subtotal = float(input('Please enter the subtotal: '))
tax = subtotal * .06
total = subtotal + tax

print(f'Sales tax amount: {tax:.02f}')

print(f'Total: {total:.02f}')