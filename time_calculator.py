def add_time(start, added_time, day="today"):
    AM_PM = ""
    for _ in start:
        AM_PM += _ if _.isalpha() else ''
    original_hour = start[0]
    added_hour = ""
    original_minutes = ""
    added_minutes = ""

    if start[1] != ':':
        original_hour += start[1]
        original_minutes = start[3:5]
    else:
        original_minutes = start[2:4]
    index = added_time.find(':')
    for i in range(index):
        added_hour += added_time[i]
    added_minutes = added_time[index + 1:]
    hours = int(original_hour)
    minutes = int(original_minutes)

    if AM_PM == "PM":
        hours += 12

    hours += int(added_hour)
    minutes += int(added_minutes)
    if minutes >= 60:
        minutes -= 60
        hours += 1

    days_later = hours // 24
    hours %= 24

    new_AM_PM = ""
    if hours >= 12:
        new_AM_PM = "PM"
    else:
        new_AM_PM = "AM"

    if hours > 12:
        hours -= 12
    if not hours:
        hours = 12

    new_time = str(hours) + ':'
    if minutes < 10:
        new_time += '0'
    new_time += str(minutes)
    nxt = ""
    if days_later == 1:
        nxt = " (next day)"
    elif days_later > 1:
        nxt = f" ({days_later} days later)"

    if day == "today":
        return f"{new_time} {new_AM_PM}{nxt}"
    else:
        for _ in range(7):
            if days_of_week[_] == day.lower():
                index = _
                break
        index = (index + days_later) % 7
        return f"{new_time} {new_AM_PM}, {days_of_week[index].capitalize()}{nxt}"


days_of_week = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
print(add_time('11:59 PM', '24:05'))
