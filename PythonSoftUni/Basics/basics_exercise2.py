# usd = float(input())
#
# course = 1.79549
# bgn = usd * course
#
# print(bgn)

# from math import pi
#
# radians = float(input())
#
# degrees = radians * 180 / pi
#
# print(degrees)

# deposit = float(input())
# period = int(input())
# percent = float(input()) / 100
#
# sum = deposit + period * ((deposit * percent) / 12)
#
# print(sum)

# number_of_pages = int(input())
# pages_per_hour = int(input())
# number_of_days = int(input())
#
# time_per_book = number_of_pages // pages_per_hour
# hours_per_day = time_per_book // number_of_days
#
# print(hours_per_day)

# PENS_PACKET_PRICE = 5.80
# MARKERS_PACKET_PRICE = 7.20
# FLUID_PRICE_LITER = 1.20
#
# num_pen_packets = int(input())
# num_markers_packets = int(input())
# liters_fluid = int(input())
# discount_percent = int(input())
#
# discount_multiplier = discount_percent / 100
#
# pen_price = num_pen_packets * PENS_PACKET_PRICE
# markers_price = num_markers_packets * MARKERS_PACKET_PRICE
# fluid_price = liters_fluid * FLUID_PRICE_LITER
#
# total_price = pen_price + markers_price + fluid_price
# discount = total_price * discount_multiplier
# total_price -= discount
#
# print(total_price)

# NYLON_SQ_METER = 1.50
# PAINT_LITER = 14.50
# THINNER_LITER = 5.00
#
# additional_nylon = 2
# paint_added_percent = 0.10
# bags = 0.40
# workers_budget_percent = 0.30
#
# total_nylon = int(input())
# liters_paint = int(input())
# liters_thinner = int(input())
# hours_work = int(input())
#
# nylon_sum = (total_nylon + additional_nylon) * NYLON_SQ_METER
# paint_added = liters_paint * PAINT_LITER * paint_added_percent
#
# paint_sum = (liters_paint * PAINT_LITER) + paint_added
# thinner_sum = liters_thinner * THINNER_LITER
#
# total_price = nylon_sum + paint_sum + thinner_sum + bags
#
#
# workers_sum = total_price * workers_budget_percent * hours_work
#
# final_price = total_price + workers_sum
#
# print(final_price)


# CHICKEN_MENU = 10.35
# FISH_MENU = 12.40
# VEGAN_MENU = 8.15
# DELIVERY = 2.50
#
# number_chicken_menus = int(input())
# number_fish_menus = int(input())
# number_vegan_menus = int(input())
#
# dessert_perc = 0.20
#
# chicken_sum = number_chicken_menus * CHICKEN_MENU
# fish_sum = number_fish_menus * FISH_MENU
# vegan_sum = number_vegan_menus * VEGAN_MENU
#
# total_price = chicken_sum + fish_sum + vegan_sum
#
# dessert_price = total_price * dessert_perc
#
# final_price = total_price + dessert_price + DELIVERY
#
# print(final_price)


# price_per_year = int(input())
#
# trainers_perc = price_per_year * 0.40
# trainer_price = price_per_year - trainers_perc
# # print(trainer_price)
# equip_perc = trainer_price * 0.20
# equip_price = trainer_price - equip_perc
# # print(equip_price)
# basketball_price = equip_price / 4
# # print(basketball_price)
# basketball_accessories = basketball_price / 5
# # print(basketball_accessories)
# total_price = price_per_year + trainer_price + equip_price + basketball_price + basketball_accessories
#
# print(total_price)


length = int(input())
width = int(input())
height = int(input())
percent = float(input())

percent_volume = percent / 100

total_volume = width * height * length
total_volume_liters = total_volume / 1000
# print(total_volume_liters)
needed_volume = total_volume_liters * (1 - percent_volume)
print(needed_volume)



















