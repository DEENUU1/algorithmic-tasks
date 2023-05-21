def format_duration(seconds):
    if not seconds:
        return "now"
    if seconds == 1:
        return "1 second"

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    duration = []
    
    if years:
        duration.append(f"{years} year" + ("s" if years > 1 else ""))
    if days:
        duration.append(f"{days} day" + ("s" if days > 1 else ""))
    if hours:
        duration.append(f"{hours} hour" + ("s" if hours > 1 else ""))
    if minutes:
        duration.append(f"{minutes} minute" + ("s" if minutes > 1 else ""))
    if seconds:
        duration.append(f"{seconds} second" + ("s" if seconds > 1 else ""))

    if len(duration) > 1:
        return ", ".join(duration[:-1]) + " and " + duration[-1]
    else:
        return duration[0]
