# convert seconds to days, hours, minutes, seconds
import datetime


# first we extract days, then hours, then minutes, then seconds (days hour minutes seconds)
# using normal method
def seconds(nsec):
    day = nsec // (24 * 60 * 60)  # 1 day = 24*60*60 seconds
    daymod = nsec % (24 * 60 * 60)
    hour = daymod // (60 * 60)  # 1 hour = 60*60 seconds
    hourmod = daymod % (60 * 60)
    min = hourmod // 60  # 1 minute = 60 seconds
    second = hourmod % 60

    print(f"{day} Days, {hour} Hours, {min} Minutes, {second} Seconds")


# first we extract days, then hours, then minutes, then seconds (days hour minutes seconds)
# using divmod inbuilt method
def convert(s):
    day, daymod = divmod(s, (24 * 60 * 60))   # days, hours
    hour, hourmod = divmod(daymod, (60 * 60))   # hours , minutes
    min, second = divmod(hourmod, 60)    # minutes , seconds
    print(f"{day} Days, {hour} Hours, {min} Minutes, {second} Seconds")


# first we extract seconds, then minutes, then hours, then days (seconds minutes hour days)
def time_convert(t):
    min, sec = divmod(t, 60)   # minutes , seconds
    hour, min = divmod(min, 60)   # hours , minutes
    day, hour = divmod(hour, 24)   # days, hours

    print(f"{day} Days, {hour} Hours, {min} Minutes, {sec} Seconds")


n = int(input("Enter the seconds : "))
seconds(n)
convert(n)
time_convert(n)

# using datetime function
print((datetime.timedelta(seconds=n)))
