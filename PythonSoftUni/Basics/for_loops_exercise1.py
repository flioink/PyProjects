# volume_in_bottle = 750
# num_bottles = int(input())
#
# total_detergent = num_bottles * volume_in_bottle
# wash_volume = 0
# plate_vol = 5
# pot_volume = 15
# counter = 0
# volume_used = 0
# num_plates = 0
# num_pots = 0
#
# while True and total_detergent >= 0:
#     batch = input()
#     if batch == "End":
#         break
#     counter += 1
#     batch = int(batch)
#
#     if counter % 3 == 0:
#         num_pots += batch
#         volume_used = batch * pot_volume
#
#     else:
#         num_plates += batch
#         volume_used = batch * plate_vol
#
#     total_detergent -= volume_used
#
# if total_detergent >= 0:
#     print("Detergent was enough!")
#     print(f"{num_plates} dishes and {num_pots} pots were washed.")
#     print(f"Leftover detergent {total_detergent} ml.")
#
# else:
#     print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")


# counter = 0
# total_sum = 0
# cash_drafts = 0
# credit_drafts = 0
# cash_info = 0
# credit_info = 0
#
# expected_sum = int(input())
#
# while True:
#     input_info = input()
#     if input_info == "End":
#         print("Failed to collect required money for charity.")
#         break
#
#     else:
#         input_info = int(input_info)
#     counter += 1
#
#     if counter % 2 != 0:
#         if input_info <= 100:
#             cash_drafts += 1
#             cash_info += input_info
#             print("Product sold!")
#             total_sum += input_info
#
#         else:
#             print("Error in transaction!")
#
#     elif counter % 2 == 0:
#         if input_info >= 10:
#             credit_drafts += 1
#             credit_info += input_info
#             print("Product sold!")
#             total_sum += input_info
#
#         else:
#             print("Error in transaction!")
#
#     if total_sum >= expected_sum:
#         print(f"Average CS: {cash_info / cash_drafts:.2f}")
#         print(f"Average CC: {credit_info / credit_drafts:.2f}")
#         break

# letter_c = 0
# letter_o = 0
# letter_n = 0
# sum_letters = ""
# final_word = ""
# num_words = 0
#
# while True:
#     letter = input()
#
#     if letter == "End":
#         break
#
#     if letter.isalpha():
#
#         if letter == "c" and letter_c == 0:
#             letter_c = 1
#             letter = ""
#
#         elif letter == "o" and letter_o == 0:
#             letter_o = 1
#             letter = ""
#
#         elif letter == "n" and letter_n == 0:
#             letter_n = 1
#             letter = ""
#
#         if letter_c != 0 and letter_o != 0 and letter_n != 0:
#             letter = " "
#             letter_c = 0
#             letter_o = 0
#             letter_n = 0
#             num_words += 1
#
#         sum_letters += letter
# ls = sum_letters.split(" ")
# final_word = " ".join(ls[:num_words])
#
# print(final_word)

# for i in range(1, 100):
#     if i % 3 == 0:
#         print(i)

# num_1 = int(input())
#
# value = 0
#
# for i in range(num_1):
#     num_2 = int(input())
#     value += num_2
#
# print(f"{value / num_1:.2f}")

total_days = int(input())
total_money_raised = 0
total_days_won = 0

for i in range(total_days):
    daily_money_raised = 0
    daily_wins = 0
    daily_losses = 0

    while True:
        sport = input()
        if sport == "Finish":
            break
        result = input()

        if result == "win":
            daily_money_raised += 20
            daily_wins += 1
        elif result == "lose":
            daily_losses += 1

    if daily_wins > daily_losses:
        daily_money_raised *= 1.10
        total_days_won += 1

    total_money_raised += daily_money_raised

if total_days_won > total_days / 2:
    total_money_raised *= 1.20
    print(f"You won the tournament! Total raised money: {total_money_raised:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money_raised:.2f}")
