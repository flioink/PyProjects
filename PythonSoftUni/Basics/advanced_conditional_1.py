# budget = float(input())
# category = input()
# number_of_people = int(input())
#
# percentage_transport = 0
# ticket_price = 0
#
# if category == "VIP":
#     ticket_price = 499.99
# elif category == "Normal":
#     ticket_price = 249.99
#
# if 1 <= number_of_people <= 4:
#     percentage_transport = 0.75
#
# elif 5 <= number_of_people <= 9:
#     percentage_transport = 0.60
#
# elif 10 <= number_of_people <= 24:
#     percentage_transport = 0.50
#
# elif 25 <= number_of_people <= 49:
#     percentage_transport = 0.40
#
# elif number_of_people > 50:
#     percentage_transport = 0.25
#
#
# transport_price = budget * percentage_transport
#
# total_ticket_price = ticket_price * number_of_people
#
# remaining_budget = budget - transport_price
#
#
# if remaining_budget > total_ticket_price:
#     print(f"Yes! You have {remaining_budget - total_ticket_price:.2f} leva left.")
#
# else:
#     print(f"Not enough money! You need {total_ticket_price - remaining_budget:.2f} leva.")


# num_junior_cyclists = int(input())
# num_senior_cyclists = int(input())
# race_type = input()
# total_cyclists_number = num_junior_cyclists + num_senior_cyclists
#
# juniors = {"trail": 5.50, "cross-country": 8, "downhill": 12.25, "road": 20}
# seniors = {"trail": 7, "cross-country": 9.50, "downhill": 13.75, "road": 21.50}
#
# juniors_sum = num_junior_cyclists * float(juniors[race_type])
# seniors_sum = num_senior_cyclists * float(seniors[race_type])
# total_sum = juniors_sum + seniors_sum
#
# if total_cyclists_number >= 50:
#     if race_type == "cross-country":
#         total_sum -= (total_sum * 0.25)
#
# final_sum = total_sum - (total_sum * 0.05)
#
# print(f"{final_sum:.2f}")

# marigold_number = int(input())
# rose_number = int(input())
# tulip_number = int(input())
# season = input()
# holiday = input()
# arrangement = 2
# total_flowers_number = marigold_number + rose_number + tulip_number
#
# spring = {"marigold": 2.00, "rose": 4.10, "tulip": 2.50}
# summer = {"marigold": 2.00, "rose": 4.10, "tulip": 2.50}
# autumn = {"marigold": 3.75, "rose": 4.50, "tulip": 4.15}
# winter = {"marigold": 3.75, "rose": 4.50, "tulip": 4.15}
#
# sum = 0
#
# if season == "Spring":
#     sum = marigold_number * spring["marigold"] + rose_number * spring["rose"] + tulip_number * spring["tulip"]
#
#     if tulip_number > 7:
#         sum -= sum * 0.05
#     if holiday == "Y":
#         sum += sum * 0.15
#
#
# elif season == "Summer":
#     sum = marigold_number * summer["marigold"] + rose_number * summer["rose"] + tulip_number * summer["tulip"]
#     if holiday == "Y":
#         sum += sum * 0.15
#
# elif season == "Autumn":
#     sum = marigold_number * autumn["marigold"] + rose_number * autumn["rose"] + tulip_number * autumn["tulip"]
#     if holiday == "Y":
#         sum += sum * 0.15
#
# elif season == "Winter":
#     sum = marigold_number * winter["marigold"] + rose_number * winter["rose"] + tulip_number * winter["tulip"]
#     if rose_number >= 10:
#         sum -= sum * 0.10
#     if holiday == "Y":
#         sum += sum * 0.15
#
# if total_flowers_number > 20:
#     sum -= sum * 0.20
#
# sum += arrangement
#
# print(f"{sum:.2f}")


# budget = float(input())
# season = input()
#
# price = 0
# car_class = ""
# budget_percentage = 0
# car_type = ""
#
# if budget <= 100:
#     car_class = "Economy class"
#     if season == "Summer":
#         car_type = "Cabrio"
#         budget_percentage = 0.35
#
#     elif season == "Winter":
#         car_type = "Jeep"
#         budget_percentage = 0.65
#
# elif 100 < budget <= 500:
#     car_class = "Compact class"
#
#     if season == "Summer":
#         car_type = "Cabrio"
#         budget_percentage = 0.45
#
#     elif season == "Winter":
#         car_type = "Jeep"
#         budget_percentage = 0.80
#
# elif budget > 500:
#     car_class = "Luxury class"
#     car_type = "Jeep"
#     budget_percentage = 0.9
#
# price = budget_percentage * budget
#
# print(car_class)
# print(f"{car_type} - {price:.2f}")


# budget = float(input())
# season = input()
#
# location = ""
# placement = ""
# perc_budget = 0
# price = 0
#
# if budget <= 1000:
#     placement = "Camp"
#     if season == "Summer":
#         location = "Alaska"
#         perc_budget = 0.65
#     elif season == "Winter":
#         location = "Morocco"
#         perc_budget = 0.45
#
# elif 100 < budget <= 3000:
#     placement = "Hut"
#     if season == "Summer":
#         location = "Alaska"
#         perc_budget = 0.80
#     elif season == "Winter":
#         location = "Morocco"
#         perc_budget = 0.60
#
# elif budget > 3000:
#     placement = "Hotel"
#     if season == "Summer":
#         location = "Alaska"
#         perc_budget = 0.90
#     elif season == "Winter":
#         location = "Morocco"
#         perc_budget = 0.90
#
# price = budget * perc_budget
#
# print(f"{location} - {placement} - {price:.2f}")


# season = input()
# kilometers_per_month = float(input())
#
# price_per_1_km = 0
# salary = 0
#
# if season == "Spring":
#     if kilometers_per_month <= 5000:
#         price_per_1_km = 0.75
#     elif 5000 < kilometers_per_month <= 10000:
#         price_per_1_km = 0.95
#     elif 10000 < kilometers_per_month <= 20000:
#         price_per_1_km = 1.45
#
# elif season == "Autumn":
#     if kilometers_per_month <= 5000:
#         price_per_1_km = 0.75
#     elif 5000 < kilometers_per_month <= 10000:
#         price_per_1_km = 0.95
#     elif 10000 < kilometers_per_month <= 20000:
#         price_per_1_km = 1.45
#
# elif season == "Summer":
#     if kilometers_per_month <= 5000:
#         price_per_1_km = 0.90
#     elif 5000 < kilometers_per_month <= 10000:
#         price_per_1_km = 1.10
#     elif 10000 < kilometers_per_month <= 20000:
#         price_per_1_km = 1.45
#
# elif season == "Winter":
#     if kilometers_per_month <= 5000:
#         price_per_1_km = 1.05
#     elif 5000 < kilometers_per_month <= 10000:
#         price_per_1_km = 1.25
#     elif 10000 < kilometers_per_month <= 20000:
#         price_per_1_km = 1.45
#
# salary = price_per_1_km * kilometers_per_month
# salary -= salary * 0.10
# salary *= 4
#
# print(f"{salary:.2f}")


# boys_hotel_fees = {"Winter": 9.60, "Spring": 7.20, "Summer": 15}
# girls_hotel_fees = {"Winter": 9.60, "Spring": 7.20, "Summer": 15}
# mixed_group_hotel_fees = {"Winter": 10, "Spring": 9.50, "Summer": 20}
#
# girls_group_sports = {"Winter": "Gymnastics", "Spring": "Athletics", "Summer": "Volleyball"}
# boys_group_sports = {"Winter": "Judo", "Spring": "Tennis", "Summer": "Football"}
# mixed_group_sports = {"Winter": "Ski", "Spring": "Cycling", "Summer": "Swimming"}
#
# season = input()
# group_type = input()
# num_students = int(input())
# num_days = int(input())
#
# practiced_sport = ""
# price = 0
# discount = 0
#
# if group_type == "mixed":
#     practiced_sport = mixed_group_sports[season]
#     price = num_days * mixed_group_hotel_fees[season] * num_students
#
#     if num_students >= 50:
#         discount = 0.50
#         price -= price * discount
#
#     elif 20 <= num_students < 50:
#         discount = 0.15
#         price -= price * discount
#
#     elif 10 <= num_students < 20:
#         discount = 0.05
#         price -= price * discount
#
#
# elif group_type == "boys":
#     practiced_sport = boys_group_sports[season]
#     price = num_days * boys_hotel_fees[season] * num_students
#
#     if num_students >= 50:
#         discount = 0.50
#         price -= price * discount
#
#     elif 20 <= num_students < 50:
#         discount = 0.15
#         price -= price * discount
#
#     elif 10 <= num_students < 20:
#         discount = 0.05
#         price -= price * discount
#
#
# elif group_type == "girls":
#     practiced_sport = girls_group_sports[season]
#     price = num_days * girls_hotel_fees[season] * num_students
#
#     if num_students >= 50:
#         discount = 0.50
#         price -= price * discount
#
#     elif 20 <= num_students < 50:
#         discount = 0.15
#         price -= price * discount
#
#     elif 10 <= num_students < 20:
#         discount = 0.05
#         price -= price * discount
#
# print(f"{practiced_sport} {price:.2f} lv.")


# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# x = float(input())
# y = float(input())
#
# if x == x1 or x == x2:
#     if y1 <= y <= y2:
#         print("Border")
#     else:
#         print("Inside / Outside")
#
#
# elif y == y1 or y == y2:
#     if x1 <= x <= x2:
#         print("Border")
#     else:
#         print("Inside / Outside")
#
# else:
#     print("Inside / Outside")

# for i in range(0, 10):
#     print(i + 1)


# while True:
#     num = float(input())
#     if num >= 0:
#         result = num * 2
#         print(f"Result: {result:.2f}")
#     else:
#         print("Negative number!")
#         break





