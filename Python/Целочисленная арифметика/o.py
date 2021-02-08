def format_seconds_to_hhmmss(seconds):
    hours = seconds // (3600)
    while hours >= 24:
        hours -=24
    seconds %= (3600)
    minutes = seconds // 60
    seconds %= 60
    return str(hours)+":" + "%02i:%02i" % (minutes, seconds)
n = int(input())
print(format_seconds_to_hhmmss(n))