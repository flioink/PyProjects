
# day = int(input())
# days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
#
# if 1 <= day <= 7:
#     print(days[day])
# else:
#     print("Error")


# days = {"Monday": "Working day", "Tuesday": "Working day", "Wednesday": "Working day", "Thursday": "Working day",
#         "Friday": "Working day", "Saturday": "Weekend", "Sunday": "Weekend"}
#
# day = input()
# if day in days:
#     print(days[day])
#
# else:
#     print("Error")


# animals = {"dog": "mammal", "crocodile": "reptile", "tortoise": "reptile", "snake": "reptile"}
# animal = input()
#
# if animal in animals:
#     print(animals[animal])
# else:
#     print("unknown")

sofia = {"coffee": 0.50, "water": 0.80, "beer": 1.20, "sweets": 1.45, "peanuts": 1.60}
plovdiv = {"coffee": 0.40, "water": 0.70, "beer": 1.15, "sweets": 1.30, "peanuts": 1.50}
varna = {"coffee": 0.45, "water": 0.70, "beer": 1.10, "sweets": 1.35, "peanuts": 1.55}

product = input()
city = input()
quantity = float(input())

if city == "Sofia":
    price = quantity * sofia[product]
    print(price)
elif city == "Plovdiv":
    price = quantity * plovdiv[product]
    print(price)
elif city == "Varna":
    price = quantity * varna[product]
    print(f"{price:.2f}")


# work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#
# hour = int(input())
# day = input()
#
# if 10 <= hour <= 18 and day in work_days:
#     print("open")
#
# else:
#     print("closed")
