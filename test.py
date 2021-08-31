# from datetime import date

# def period_is_late(last,today,cycle_length):
#     last = 2021-8-1
#     today = date.today()
#     cycle_length = 28
#     if today - last > 28:
#         print("false")
#     else:
#         print("true")

# def period_is_late(last, today, cycle_length):
#     delta = today - last
#     return delta.days > cycle_length

def period_is_late(last, today, cycle_length):
    return (today - last).days > cycle_length