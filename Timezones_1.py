
from datetime import datetime as dt
import pytz

timezones = pytz.all_timezones
for i in range(len(timezones)):
    zone = timezones[i]
    tz = pytz.timezone(zone)
    cur_time = dt.now(tz)
    print("Current time of zone",zone,"is",cur_time)
    