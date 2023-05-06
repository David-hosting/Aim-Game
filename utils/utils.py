def timer(sec):
    """
    | Just a function to calculate time.
    """
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return (sec, mins, hours)