def get_day_name(x):
    match x:
        case 1:
            return "monday"
        case 2:
            return "tuesday"
        case 3:
            return "wednesday"
        case _: return "unknown day"
        
r = get_day_name("saturday")
print(r)