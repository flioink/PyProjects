def discount(percent, price):
    return (percent * price) / 100


def tickets():
    company_name = input("Please enter the name of the air carrier name: ")
    number_of_adults = int(input("Enter the number of adults: "))
    number_of_kids = int(input("Enter the number kids: "))
    net_ticket_price = float(input("Enter the ticket net price: "))
    service_fare = float(input("Enter the service fare: "))

    kids_discount = 70
    profit_margin = 20

    kids_tickets_net_price = number_of_kids * net_ticket_price
    kids_tickets_net_price -= discount(kids_discount, kids_tickets_net_price)
    kids_tickets_final_price = kids_tickets_net_price + (service_fare * number_of_kids)
    # 15 5 120 40
    adults_tickets_final_price = number_of_adults * (net_ticket_price + service_fare)
    total_price = kids_tickets_final_price + adults_tickets_final_price
    profits = round(discount(profit_margin, total_price), 2)

    print(f"The profit of your agency from {company_name} tickets is {profits} lv.")


def cat_walk():
    minutes_walking = int(input("Please enter number of minutes for the cat walk: "))
    number_of_walks = int(input("Please enter cat walks per day: "))
    calorie_intake = int(input("Please enter the daily caloric intake of your cat: "))
    calorie_burn_per_minute = 5

    total_daily_walk_minutes = minutes_walking * number_of_walks
    burned_calories = total_daily_walk_minutes * calorie_burn_per_minute
    half_daily_calories = discount(50, calorie_intake)

    if burned_calories > half_daily_calories:
        print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
    else:
        print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")

    # 30 3 600


def vending():
    drinks_type = input("Please enter the type of the drink. You can enter 1 for'espresso', 2 for'cappuccino' or 3 for"
                        "'tea': ")
    drinks_sugar_level = input("Enter sugar amount for the drink. You can enter 1 for 'without', 2 for 'normal' or 3 "
                               "for 'extra': ")
    drinks_number = int(input("Enter the number of drinks. Can be between 1 and 50: "))

    drinks_dict = {"1": "espresso", "2": "cappuccino", "3": "tea"}

    espresso_price = {"1": 0.9, "2": 1, "3": 1.20}
    cappuccino_price = {"1": 1, "2": 1.20, "3": 1.60}
    tea_price = {"1": 0.5, "2": 0.6, "3": 0.7}

    espresso_discount = 25
    no_sugar_discount = 35
    final_price = 0
    over_sum_discount = 20

    if drinks_dict[drinks_type] == "espresso":
        if drinks_number >= 5:
            disc = (discount(espresso_discount, espresso_price[drinks_sugar_level]))
            # print(disc)
            final_price = (espresso_price[drinks_sugar_level] - disc) * drinks_number
        else:
            final_price = espresso_price[drinks_sugar_level] * drinks_number

    elif drinks_dict[drinks_type] == "cappuccino":
        final_price = cappuccino_price[drinks_sugar_level] * drinks_number

    elif drinks_dict[drinks_type] == "tea":
        final_price = tea_price[drinks_sugar_level] * drinks_number

    if drinks_sugar_level == "1":
        disc = discount(no_sugar_discount, final_price)
        final_price -= disc

    if final_price > 15:
        final_disc = discount(over_sum_discount, final_price)
        final_price -= final_disc

    final_price = round(final_price, 2)

    print(f"You bought {drinks_number} cups of {drinks_dict[drinks_type]} for {final_price} lv.")


def climbers():
    members_per_group = []
    total_climbers = 0

    peaks = {"Musala": 0, "Montblanc": 0, "Kilimanjaro": 0, "K2": 0, "Everest": 0}

    groups_numbers = int(input("Enter number of groups: "))
    for i in range(groups_numbers):
        var = (int(input("Enter number of climbers: ")))
        members_per_group.append(var)
        total_climbers += var
        if 0 < var < 6:
            peaks["Musala"] += var
            # print(peaks)

        elif 6 <= var <= 12:
            peaks["Montblanc"] += var
            # print(peaks)

        elif 13 <= var <= 25:
            peaks["Kilimanjaro"] += var
            # print(peaks)

        elif 26 <= var <= 40:
            peaks["K2"] += var
            # print(peaks)

        elif var >= 41:
            peaks["Everest"] += var
            # print(peaks)

    print(members_per_group, total_climbers, peaks)

    for key, value in peaks.items():
        percentage = (value / total_climbers) * 100
        percentage = round(percentage, 2)

        print(f"{percentage}% are going to {key}. ")
    # 10 10 5 1 100 12 26 17 37 40 78
    # 11gr


def stars():
    actors = {}
    budget = float(input("Please enter the budget: "))
    actor_name = ""
    while budget > 0:
        actor_name = str(input("Enter the name of the actor: "))
        if actor_name == "ACTION":
            break
        if len(actor_name) > 15:
            actor_salary = discount(20, budget)
        else:
            actor_salary = float(input("Enter the salary of the actor: "))
        actors[actor_name] = actor_salary
        budget -= actor_salary

    budget = round(budget, 2)
    if budget > 0:
        print(f"We are left with {budget} leva.")
    else:
        print(f"We need {abs(budget)} leva for our actors.")


def basketball():
    results = []
    tournament_info = {}
    total_number_of_games = 0
    while True:
        tournament_name = str(input("Enter the name of the tournament: "))
        if tournament_name == "END":
            break

        number_of_games = int(input("Enter the number of games: "))
        for i in range(number_of_games):
            desi_team_score = int(input("Enter the points scored by Desi's team: "))
            other_team_score = int(input("Enter the points scored by the other team team: "))
            results.append((desi_team_score, other_team_score))

        tournament_info[tournament_name] = results
        total_number_of_games += number_of_games
        results = []

    wins = 0
    for key, value in tournament_info.items():
        for j, k in enumerate(value):
            if k[0] > k[1]:
                print(f"Game {j + 1} of tournament {key}: win with {k[0] - k[1]} points")
                wins += 1
            elif k[1] > k[0]:
                print(f"Game {j + 1} of tournament {key}: lose with {k[1] - k[0]} points")
            else:
                print(f"Game {j + 1} of tournament {key}: DRAW")

    wins_percentage = wins / total_number_of_games * 100
    loss_percentage = (total_number_of_games - wins) / total_number_of_games * 100
    wins_percentage = round(wins_percentage, 2)
    loss_percentage = round(loss_percentage, 2)

    print(f"{wins_percentage}% matches won.")
    print(f"{loss_percentage}% matches lost.")


# Dunkers
# 2
# 75
# 65
# 56
# 73
# Fire Girls
# 3
# 67
# 34
# 83
# 98
# 66
# 45
basketball()
