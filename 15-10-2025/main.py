# Task 1

# def count_overtime(hours):
#     if hours == 0:
#         print("Invalid Input")
#         return
#     count = 0
#     for i in range(0,len(hours),1):
#         if hours[i] > 8 :
#             count += 1
#     print(count)

# count_overtime([9, 7, 8, 10, 6, 9])
# count_overtime([8, 8, 9, 10, 7])
# count_overtime([])

# def count_overtime(hours_list):
#     if len(hours_list) == 0 or all(hour == 0 for hour in hours_list):
#         print("Invalid Input")
#         return
#     count = 0
#     for hour in hours_list:
#         if hour > 8:
#             count += 1
#     print(count)

# count_overtime([9, 7, 8, 10, 6, 9])
# count_overtime([8, 8, 9, 10, 7])
# count_overtime([0])