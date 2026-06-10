def time_exec(starting_time, ending_time):
    timedelta = ending_time - starting_time
    seconds = timedelta.seconds
    microseconds = timedelta.microseconds
    print(f"{seconds}.{microseconds}s")
