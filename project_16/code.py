# Example of datetime module


# from datetime import datetime

# now = datetime.now()

# print(now)


# date = now.date()
# time = now.time()

# print(date)
# print(time)


# formating date

# strftime() date to string
# strptime() string to date


# formatted = now.strftime('%d-%m-%Y')

# print(formatted)


# day = '03-04-2026'

# dd = datetime.strptime(day, "%d-%m-%Y")

# print(dd)



# Date Arithmetic (timedelta)


# from datetime import datetime, timedelta


# now = datetime.now()


# print(now + timedelta(days=20))  for add days

# print(now - timedelta(days=20)) for minus days




# time sleeping

import time

print('hello')
print('hello')

time.sleep(2)

print('hello')
print('hello')