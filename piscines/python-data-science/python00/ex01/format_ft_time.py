from datetime import datetime
from time import time

initial_datetime = datetime(1970, 1, 1)
initial_time = time()

now = datetime.now()

print(f"Seconds since {initial_datetime.strftime('%B %d, %Y')}: {int(initial_time):,} or {int(initial_time):.2e} in scientific notation")
print(now.strftime("%b %d %Y"))
