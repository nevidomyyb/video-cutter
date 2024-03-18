def string_to_acceptable_list(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    delta = (hours, minutes, seconds)
    return delta