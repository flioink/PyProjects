# volume = int(input())
# pipe_one_hr = int(input())
# pipe_two_hr = int(input())
# hrs_away = float(input())
#
# p1_total = pipe_one_hr * hrs_away
# p2_total = pipe_two_hr * hrs_away
#
# filled_volume = p1_total + p2_total
#
# percentage_filled = filled_volume / volume * 100
#
# p1_perc = p1_total / filled_volume * 100
# p2_perc = p2_total / filled_volume * 100
#
# if filled_volume <= volume:
#     print(f"The pool is {percentage_filled:.2f}% full."
#           f" Pipe 1: {p1_perc:.2f}%. Pipe 2: {p2_perc:.2f}%.")
#
# else:
#     print(f"For {hrs_away:.2f} hours the pool overflows with {filled_volume - volume:.2f} liters.")

# free_days = int(input())
#
# work_days = 365 - free_days
# play_norm = 30000
#
# work_day_play = work_days * 63
# free_days_play = free_days * 127
#
# total_play_time = free_days_play + work_day_play
#
# diff = play_norm - total_play_time
#
# hrs = abs(diff) // 60
# mins = abs(diff) % 60
#
# if diff >= 0:
#     print("Tom sleeps well")
#     print(f"{hrs} hours and {mins} minutes less for play")
#
# else:
#     print("Tom will run away")
#     print(f"{hrs} hours and {mins} minutes more for play")

# from math import ceil, floor
#
# x_sq_meters = int(input())
# grapes_per_sq_meter = float(input())
# needed_qty_wine = int(input())
# num_workers = int(input())
#
# grapes_needed_per_liter = 2.5
#
# perc_for_wine = 0.40
#
# total_grapes = x_sq_meters * grapes_per_sq_meter
#
# wine = (total_grapes * perc_for_wine) / grapes_needed_per_liter
# remaining_wine = abs(wine - needed_qty_wine)
#
# if wine >= needed_qty_wine:
#     print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
#     print(f"{ceil(wine - needed_qty_wine)} liters left -> {ceil(remaining_wine / num_workers)} liters per person.")
#
# else:
#     print(f"It will be a tough winter! More {floor(remaining_wine)} liters wine needed.")


# km = int(input())
# time_of_day = input()
#
# price = 0
#
# if km < 20:
#     if time_of_day == "day":
#         price = (0.79 * km) + 0.70
#     elif time_of_day == "night":
#         price = (0.90 * km) + 0.70
#
# elif 20 <= km < 100:
#     price = 0.09 * km
#
# elif km >= 100:
#     price = 0.06 * km
#
# print(f"{price:.2f}")

# from math import ceil, floor
#
# num_days = int(input())
# total_food_kg = int(input())
# dog_food_daily = float(input())
# cat_food_daily = float(input())
# turtle_food_daily_grams = float(input())
#
#
# dog_food = dog_food_daily * num_days
# cat_food = cat_food_daily * num_days
# turtle_food = (turtle_food_daily_grams * num_days) / 1000
#
# total_food_needed = dog_food + cat_food + turtle_food
#
# diff = abs(total_food_needed - total_food_kg)
#
#
# if total_food_needed <= total_food_kg:
#     print(f"{floor(diff)} kilos of food left.")
#
# else:
#     print(f"{ceil(diff)} more kilos of food are needed.")
# from math import ceil, floor
# magnolia = 3.25
# zumbul = 4
# rose = 3.50
# cactus = 8
# tax = 0.05
#
# magnolia_count = int(input())
# zumbul_count = int(input())
# rose_count = int(input())
# cactus_count = int(input())
# present_price = float(input())
#
# total_price = magnolia_count * magnolia + zumbul_count * zumbul + rose_count * rose + cactus_count * cactus
# total_price -= total_price * tax
#
# diff = abs(total_price - present_price)
#
# if total_price >= present_price:
#     print(f"She is left with {floor(diff)} leva.")
#
# else:
#     print(f"She will have to borrow {ceil(diff)} leva.")


# fuel_type = input()
# volume_in_tank = int(input())
# std_qty = 25
#
# fuel_type = fuel_type.lower()
#
# if fuel_type == "diesel" or fuel_type == "gasoline" or fuel_type == "gas":
#     if volume_in_tank >= std_qty:
#         print(f"You have enough {fuel_type}.")
#     else:
#         print(f"Fill your tank with {fuel_type}!")
#
# else:
#     print("Invalid fuel!")

gasoline = 2.22
diesel = 2.33
gas = 0.93

fuel_type = input()
fuel_volume = float(input())
card = input()

price = 0

if fuel_type == "Gas":
    if card == "Yes":
        gas -= 0.08
        price = gas * fuel_volume
    else:
        price = gas * fuel_volume

elif fuel_type == "Gasoline":
    if card == "Yes":
        gasoline -= 0.18
        price = gasoline * fuel_volume
    else:
        price = gasoline * fuel_volume

elif fuel_type == "Diesel":
    if card == "Yes":
        diesel -= 0.12
        price = diesel * fuel_volume
    else:
        price = diesel * fuel_volume

if 20 <= fuel_volume <= 25:
    price -= price * 0.08

elif fuel_volume > 25:
    price -= price * 0.10

print(f"{price:.2f} lv.")