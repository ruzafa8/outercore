from datetime import datetime
from time import time

initial_dt = f"Seconds since {datetime(1970, 1, 1).strftime('%B %d, %Y')}"
secs = int(time())

now = datetime.now()

print(
    f"{initial_dt}: {secs:,} or {secs:.2e} in scientific notation"
)
print(now.strftime("%b %d %Y"))
