def registration():
    username = input()

    while True:
        command = input()
        if command == "Registration":
            break

        main_command = command.split()[0]

        if main_command == "Letters":
            setting = command.split()[1]

            if setting == "Lower":
                username = username.lower()
            elif setting == "Upper":
                username = username.upper()

            print(username)

        if main_command == "Reverse":
            test = ""
            start = int(command.split()[1])
            end = int(command.split()[2])
            if 0 <= start < len(username) and 0 <= end < len(username):
                test = username[start: end + 1][::-1]
                print(test)

        if main_command == "Substring":
            substr = command.split()[1]

            if substr in username:
                username = username.replace(substr, '')
                print(username)
            else:
                print(f"The username {username} doesn't contain {substr}.")

        if main_command == "Replace":
            symbol = command.split()[1]
            username = username.replace(symbol, "-")
            print(username)

        if main_command == "IsValid":
            symbol = command.split()[1]
            if symbol in username:
                print("Valid username.")
            else:
                print(f"{symbol} must be contained in your username.")


def destination_mapper():
    destinations = input()

    valid = []

    for i in range(len(destinations)):
        if (destinations[i] == "=" or destinations[i] == "/") and i < len(destinations) - 1:
            j = i + 1

            if j < len(destinations):

                if destinations[j].isalpha() and destinations[j].isupper():
                    while True:
                        j += 1
                        if destinations[j].isalpha():
                            continue

                        elif destinations[j] == destinations[i] and j - (i + 1) >= 3:
                            valid.append(destinations[i + 1: j])
                            break
                        else:
                            break

    travel_points = 0

    if len(valid) > 0:
        for i in range(len(valid)):
            travel_points += len(valid[i])

    print("Destinations:", ", ".join(valid))
    print(f"Travel Points: {travel_points}")


def bakery_shop():
    foods = dict()
    sold = 0

    while True:

        command = input()
        if command == "Complete":
            break

        main_command = command.split()[0]

        if main_command == "Receive":
            qty = int(command.split()[1])
            food = command.split()[2]
            if qty > 0:
                if food not in foods:
                    foods[food] = qty
                else:
                    foods[food] += qty

        if main_command == "Sell":
            qty = int(command.split()[1])
            food = command.split()[2]
            if food not in foods:
                print(f"You do not have any {food}.")
            else:
                current_qty = foods[food]
                if current_qty - qty < 0:
                    print(f"There aren't enough {food}. You sold the last {current_qty} of them.")
                    sold += current_qty
                    del foods[food]

                else:
                    foods[food] -= qty
                    print(f"You sold {qty} {food}.")
                    sold += qty
                    if foods[food] == 0:
                        del foods[food]

    for key, value in foods.items():
        print(f"{key}: {value}")

    print(f"All sold: {sold} goods")
