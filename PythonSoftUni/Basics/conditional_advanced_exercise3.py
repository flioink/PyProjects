# screening_type = input()
# rows = int(input())
# columns = int(input())
#
# income = 0
# cinema_cap = rows * columns
#
# if screening_type == "Premiere":
#     income = cinema_cap * 12.00
# elif screening_type == "Normal":
#     income = cinema_cap * 5.00
# elif screening_type == "Discount":
#     income = cinema_cap * 5.00
#
# print(f"{income:.2f} leva")


# degrees = int(input())
# time_of_day = input()
#
# outfit = ""
# shoes = ""
#
# if 10 <= degrees <= 18:
#     if time_of_day == "Morning":
#         outfit = "Sweatshirt"
#         shoes = "Sneakers"
#     elif time_of_day == "Afternoon":
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif time_of_day == "Evening":
#         outfit = "Shirt"
#         shoes = "Moccasins"
#
# if 18 < degrees <= 24:
#     if time_of_day == "Morning":
#         outfit = "Shirt"
#         shoes = "Moccasins"
#     elif time_of_day == "Afternoon":
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     elif time_of_day == "Evening":
#         outfit = "Shirt"
#         shoes = "Moccasins"
#
# if degrees >= 25:
#     if time_of_day == "Morning":
#         outfit = "T-Shirt"
#         shoes = "Sandals"
#     elif time_of_day == "Afternoon":
#         outfit = "Swim Suit"
#         shoes = "Barefoot"
#     elif time_of_day == "Evening":
#         outfit = "Shirt"
#         shoes = "Moccasins"
#
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

# ROSES = 5
# DAHLIAS = 3.80
# TULIPS = 2.80
# NARCISSUS = 3
# GLADIOLUS = 2.50
#
# flower_type = input()
# num_flowers = int(input())
# budget = int(input())
#
# price = 0
#
# if flower_type == "Roses":
#     price = ROSES * num_flowers
#     if num_flowers > 80:
#         price -= price * 0.10
#
# if flower_type == "Dahlias":
#     price = DAHLIAS * num_flowers
#     if num_flowers > 90:
#         price -= price * 0.15
#
# if flower_type == "Tulips":
#     price = TULIPS * num_flowers
#     if num_flowers > 80:
#         price -= price * 0.15
#
# if flower_type == "Narcissus":
#     price = NARCISSUS * num_flowers
#     if num_flowers < 120:
#         price += price * 0.15
#
# if flower_type == "Gladiolus":
#     price = GLADIOLUS * num_flowers
#     if num_flowers < 80:
#         price += price * 0.20
#
# if budget >= price:
#     print(f"Hey, you have a great garden with {num_flowers} {flower_type} and {budget - price:.2f} leva left.")
# else:
#     print(f"Not enough money, you need {price - budget:.2f} leva more.")


# budget = int(input())
# season = input()
# num_fishermen = int(input())
#
# price = 0
#
# if season == "Spring":
#     price = 3000
# elif season == "Summer" or season == "Autumn":
#     price = 4200
# elif season == "Winter":
#     price = 2600
#
# if num_fishermen <= 6:
#     price -= price * 0.10
# elif 7 < num_fishermen <= 11:
#     price -= price * 0.15
# elif num_fishermen >= 12:
#     price -= price * 0.25
#
# if season != "Autumn" and num_fishermen % 2 == 0:
#     price -= price * 0.05
#
#
# if budget >= price:
#     print(f"Yes! You have {budget - price:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {price - budget:.2f} leva.")


# budget = float(input())
# season = input()
#
# destination = None
# place = None
#
# price = 0
#
# if budget <= 100:
#     destination = "Bulgaria"
#     if season == "summer":
#         price = budget * 0.30
#         place = "Camp"
#
#     elif season == "winter":
#         price = budget * 0.70
#         place = "Hotel"
#
# elif budget <= 1000:
#     destination = "Balkans"
#     if season == "summer":
#         price = budget * 0.40
#         place = "Camp"
#
#     elif season == "winter":
#         price = budget * 0.80
#         place = "Hotel"
#
# elif budget > 1000:
#     destination = "Europe"
#     place = "Hotel"
#     price = budget * 0.90
#
# print(f"Somewhere in {destination}" )
# print(f"{place} - {price:.2f}")

# n1 = int(input())
# n2 = int(input())
# oper = input()
# result = 0
#
# if oper == "+":
#     result = n1 + n2
#     print(f"{n1} {oper} {n2} = {result} - " + ("even" if result % 2 == 0 else "odd"))
#
# elif oper == "-":
#     result = n1 - n2
#     print(f"{n1} {oper} {n2} = {result} - " + ("even" if result % 2 == 0 else "odd"))
#
# elif oper == "*":
#     result = n1 * n2
#     print(f"{n1} {oper} {n2} = {result} - " + ("even" if result % 2 == 0 else "odd"))
#
# elif n2 == 0:
#     print(f"Cannot divide {n1} by zero")
#
# elif oper == "/":
#     result = n1 / n2
#     print(f"{n1} {oper} {n2} = {result:.2f}")
#
# elif oper == "%":
#
#    result = n1 % n2
#    print(f"{n1} {oper} {n2} = {result}")


# month = input()
# num_nights = int(input())
#
# studio_price = 0
# apartment_price = 0
#
# full_price_studio = 0
# full_price_apt = 0
#
# if month == "May" or month == "October":
#     studio_price = 50
#     apartment_price = 65
#
#     if num_nights > 14:
#         studio_price -= studio_price * 0.30
#         apartment_price -= apartment_price * 0.10
#
#     elif num_nights > 7:
#         studio_price -= studio_price * 0.05
#
#     full_price_apt = num_nights * apartment_price
#     full_price_studio = num_nights * studio_price
#
# if month == "June" or month == "September":
#     studio_price = 75.20
#     apartment_price = 68.70
#
#     if num_nights > 14:
#         studio_price -= studio_price * 0.20
#         apartment_price -= apartment_price * 0.10
#
#     full_price_apt = num_nights * apartment_price
#     full_price_studio = num_nights * studio_price
#
# if month == "July" or month == "August":
#     studio_price = 76
#     apartment_price = 77
#
#     if num_nights > 14:
#         apartment_price -= apartment_price * 0.10
#
#     full_price_apt = num_nights * apartment_price
#     full_price_studio = num_nights * studio_price
#
# print(f"Apartment: {full_price_apt:.2f} lv.")
# print(f"Studio: {full_price_studio:.2f} lv.")


# exam_hours = int(input())
# exam_minutes = int(input())
# student_hours = int(input())
# student_minutes = int(input())
#
# exam_total_minutes = exam_hours * 60 + exam_minutes
# student_total_minutes = student_hours * 60 + student_minutes
#
# time_diff = exam_total_minutes - student_total_minutes
#
# if time_diff > 30:
#     print("Early")
#
# elif time_diff < 0:
#     print("Late")
#
# else:
#     print("On time")
#
# hours = abs(time_diff)// 60
# mins = abs(time_diff) % 60
#
# result = ""
#
# if hours > 0:
#     result = f"{hours}:{mins:02d} hours"
#
# elif mins > 0:
#     result = f"{mins} minutes"
#
# if time_diff > 0:
#     result += " before the start"
#
# elif time_diff < 0:
#     result += " after the start"
#
# print(result)

days_stay = int(input())
room_type = input()
review = input()

nights_stay = days_stay - 1

single_room = 18
apartment = 25
pres_apt = 35

price = 0

if room_type == "room for one person":
    price = single_room * nights_stay

elif room_type == "apartment":
    price = apartment * nights_stay
    if days_stay < 10:
        price -= price * 0.30

    elif 10 < days_stay <= 15:
        price -= price * 0.35

    elif days_stay > 15:
        price -= price * 0.50


elif room_type == "president apartment":
    price = pres_apt * nights_stay
    if days_stay < 10:
        price -= price * 0.10

    elif 10 < days_stay <= 15:
        price -= price * 0.15

    elif days_stay > 15:
        price -= price * 0.20

if review == "positive":
    price += price * 0.25

elif review == "negative":
    price -= price * 0.10

print(f"{price:.2f}")





















