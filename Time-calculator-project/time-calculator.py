def add_time(start, duration, start_day = None):
    week_index = {'sunday':0, 'monday':1, 'tuesday':2,'wednesday':3, 'thursday':4, 'friday':5, 'saturday':6}
    index_week = {0:'sunday', 1:'monday', 2:'tuesday', 3:'wednesday', 4:'thursday', 5:'friday', 6:'saturday'}

    time_parts = start.split(' ')
    time = time_parts[0]
    period = time_parts[1]

    hours, minutes = map(int, time.split(':'))
    if period == 'PM' and hours != 12:
        hours += 12
    elif period == 'AM' and hours == 12:
        hours = 0
    
    duration_hours, duration_minutes = map(int, duration.split(':'))

    final_minutes = minutes + duration_minutes
    additional_hours = final_minutes //60
    final_minutes = final_minutes % 60

    final_hours = hours + duration_hours + additional_hours
    days_passed = final_hours // 24
    final_hours = final_hours % 24

    if final_hours >= 12:
        final_period = 'PM'
        if final_hours > 12:
            final_hours -= 12
    else:
        final_period = 'AM'
        if final_hours == 0:
            final_hours = 12
 
    if days_passed == 0 :
        day_str = ''
    elif days_passed == 1:
        day_str = ' (next day)'
    else:
        day_str = f' ({days_passed} days later)' 
    
    if start_day is not None:
        start_day_lower = start_day.lower()
        day_index = (week_index[start_day_lower] + days_passed) % 7
        day = index_week[day_index].title()
        new_time = f"{final_hours}:{final_minutes:02} {final_period}, {day}{day_str}"
    else: 
        new_time = f"{final_hours}:{final_minutes:02} {final_period}{day_str}" 

    return new_time

print(add_time('3:30 PM', '0:00'))
