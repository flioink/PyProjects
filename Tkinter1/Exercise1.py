import re

from _decimal import Decimal, getcontext


def maskify(cc):
    size = len(cc)
    tmp = ""
    if size > 4:
        difference = size - 4
        filler = difference * "#"
        for i in range(size - 4, size):
            tmp += cc[i]
        cc = filler + tmp

    return cc


def descending_order(num):
    # Bust a move right here

    nums = [n for n in str(num)]
    converted = sorted(nums, reverse=True)
    output = int("".join(map(str, converted)))

    return output


def square_digits(num):
    # Your code here
    nums = [n for n in str(num)]
    results = []
    for i in range(len(nums)):
        tmp = int(nums[i]) ** 2
        results.append(tmp)

    output = int("".join(map(str, results)))
    return output


def xo(s):
    lower_case = s.lower()
    x_count = lower_case.count("x")
    o_count = lower_case.count("o")
    if x_count == o_count or (x_count == 0 and o_count == 0):
        return True
    else:
        return False


def find_uniq(arr):
    s = set(arr)
    for unique in s:
        if arr.count(unique) == 1:
            return unique


def solution(text, ending):
    diff = len(ending)
    if text[-diff:] == ending:
        return True
    else:
        return False


def array_diff(a, b):
    # your code here
    n = len(a)
    new_list = []
    for i in range(n):
        if a[i] not in b:
            new_list.append(a[i])
    return new_list


def digital_root(n):
    num_list = str(n)
    result = 0

    for i in range(len(num_list)):
        result += int(num_list[i])

    len_result = len(str(result))

    if len_result > 1:
        result = digital_root(result)

    return result


def solution(n):
    thousands = {"1": "M", "2": "MM", "3": "MMM"}
    hundreds = {"0": "", "1": "C", "2": "CC", "3": "CCC", "4": "CD", "5": "D", "6": "DC", "7": "DCC", "8": "DCCC",
                "9": "CM"}
    tens = {"0": "", "1": "X", "2": "XX", "3": "XXX", "4": "XL", "5": "L", "6": "LX", "7": "LXX", "8": "LXXX",
            "9": "XC"}
    ones = {"0": "", "1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "7": "VII", "8": "VIII",
            "9": "IX"}
    year = str(n)
    result = ""

    if len(year) == 1:
        result += ones[year[0]]
    elif len(year) == 2:
        result += tens[year[0]] + ones[year[1]]
    elif len(year) == 3:
        result += hundreds[year[0]] + tens[year[1]] + ones[year[2]]
    elif len(year) == 4:
        result += thousands[year[0]] + hundreds[year[1]] + tens[year[2]] + ones[year[3]]

    return result


##########

def plus(*args):
    return ["+", args[0]]


def minus(*args):
    return ["-", args[0]]


def times(*args):
    return ["*", args[0]]


def divided_by(*args):
    return ["/", args[0]]


def zero(*args):
    n = 0
    if args:
        x = args[0][1]
        actions = {"+": n + x, "-": n - x, "*": n * x, "/": "error"}
        return int(actions[args[0][0]])
    else:
        return n


def one(*args):  # your code here
    n = 1
    if args:
        x = args[0][1]
        actions = {"+": n + x, "-": n - x, "*": n * x, "/": n / x if x > 0 else 1}
        return int(actions[args[0][0]])
    else:
        return n


def two(*args):  # your code here
    n = 2
    if args:
        x = args[0][1]
        actions = {"+": n + x, "-": n - x, "*": n * x, "/": n / x if x > 0 else 1}
        return int(actions[args[0][0]])
    else:
        return n


def three(*args):  # your code here
    n = 3
    if args:
        x = args[0][1]
        actions = {"+": n + x, "-": n - x, "*": n * x, "/": n / x if x > 0 else 1}
        return int(actions[args[0][0]])
    else:
        return n


def four(*args):  # your code here
    n = 4
    if args:
        x = args[0][1]
        actions = {"+": n + x, "-": n - x, "*": n * x, "/": n / x if x > 0 else 1}
        return int(actions[args[0][0]])
    else:
        return n


def five(*args):  # your code here
    n = 5
    if args:
        x = args[0][1]
        actions = {"+": n + x, "-": n - x, "*": n * x, "/": n / x if x > 0 else 1}
        return int(actions[args[0][0]])
    else:
        return n


def six(*args):  # your code here
    n = 6
    if args:
        x = args[0][1]
        actions = {"+": n + x, "-": n - x, "*": n * x, "/": n / x if x > 0 else 1}
        return int(actions[args[0][0]])
    else:
        return n


def seven(*args):  # your code here
    n = 7
    if args:
        x = args[0][1]
        actions = {"+": n + x, "-": n - x, "*": n * x, "/": n / x if x > 0 else 1}
        return int(actions[args[0][0]])
    else:
        return n


def eight(*args):  # your code here
    n = 8
    if args:
        x = args[0][1]
        actions = {"+": n + x, "-": n - x, "*": n * x, "/": n / x if x > 0 else 1}
        return int(actions[args[0][0]])
    else:
        return n


def nine(*args):
    n = 9
    if args:
        x = args[0][1]
        actions = {"+": n + x, "-": n - x, "*": n * x, "/": n / x if x > 0 else 1}
        return int(actions[args[0][0]])
    else:
        return n


def rot13(message):
    offset = 13
    encoded = ""
    beg_lower = 96
    end_lower = 123
    msg = message.lower()

    for i in msg:
        if i.isalpha():
            tmp = ord(i) + offset

            if beg_lower < tmp < end_lower:
                encoded += chr(tmp)
            else:
                tmp = beg_lower + (tmp - end_lower) + 1
                encoded += chr(tmp)
        else:
            encoded += i

    result = ""

    for index, (a, b) in enumerate(zip(message, encoded)):
        if a.isupper():
            result += b.upper()
        else:
            result += b

    return result


# def strip_comments(text, markers):
#
#     output = ""
#
#     for index, i in enumerate(text):
#         if i == markers[0]:
#             left = text[0:index-1]
#             limit = text.find("\n")
#             right = text[limit:]
#             output = left + right
#         elif i == markers[1]:
#             left = output[0: index]
#             limit = output.find(markers[1])
#             right = output[limit:]
#             # print("right", right)
#             output = left[:limit-1]
#
#     return output

def strip_comments(text, markers):
    char1 = markers[0]
    pattern1 = char1 + r"(.*?)(?=\n)"
    char2 = markers[1]
    pattern2 = r"(\$.*)" if markers[1] == "$" else f"{char2}(.*)$"

    found1 = re.search(pattern1, text)
    output = text.replace(found1.group(0), "")
    found2 = re.search(pattern2, output)
    output = output.replace(found2.group(0), "")
    output_formatted = ""

    for i in range(len(output) - 1):
        if i > 0 and output[i] == " ":
            continue
        else:
            output_formatted += output[i]

    return output_formatted


def increment_string(s):
    if len(s) == 1:
        if s[0].isdigit():
            is_num = True

    elif s[-1].isdigit():
        is_num = True
    result = ""

    if is_num:

        end_number = ""
        first_index = 0

        for item in reversed(s):
            if item.isdigit():
                end_number += item
                first_index += 1
            else:
                break

        end_number = end_number[::-1]
        end_str = str(int(end_number) + 1).zfill(len(end_number))

        result += s[:-first_index] + end_str

        return result

    else:
        result = s + "1"
        return result


def make_readable(seconds):
    # if seconds <= 359999:
    #     hours = seconds // 3600
    #     minutes = (seconds % 3600) // 60
    #     seconds = seconds % 60 # gpt answer
    # return f'{hours:02}:{minutes:02}:{seconds:02}'
    # else:
    # return "Invalid input"
    #

    if seconds <= 359999:
        minutes = seconds / 60
        rem_seconds = "0." + str(minutes).split(".")[1]
        rem_seconds = round(float(rem_seconds) * 60, 2)
        rem_seconds = str(int(rem_seconds)).zfill(2)

        hrs = minutes / 60
        rem_hrs = str(int(hrs)).zfill(2)

        rem_minutes = "0." + str(hrs).split(".")[1]
        rem_minutes = round(float(rem_minutes) * 60, 2)
        rem_minutes = str(int(rem_minutes)).zfill(2)
        new_time = f"{rem_hrs}:{rem_minutes}:{rem_seconds}"

        return new_time


import itertools


def top_3_words(text):
    invalid_chars = "./;:,@#$%^&*()_-+=1234567890!?"
    tr_table = str.maketrans(invalid_chars, len(invalid_chars) * " ")

    lowered = text.lower()
    modified = lowered.translate(tr_table)
    words_list = modified.split()
    words_filtered = []

    for index, word in enumerate(words_list):
        if any(char.isalpha() for char in word):
            words_filtered.append(word)

    word_set = set(words_filtered)
    results = {key: 1 for key in word_set}

    for i in words_filtered:
        if i in results.keys():
            results[i] += 1
    sorted_dict = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

    if len(sorted_dict) > 3:
        first_3 = list(itertools.islice(sorted_dict.keys(), 3))
    else:
        first_3 = list(sorted_dict.keys())

    return first_3


# programiz solution
def get_permutation(string, i=0):
    if i == len(string):
        print("".join(string))

    for j in range(i, len(string)):
        words = [c for c in string]

        # swap
        words[i], words[j] = words[j], words[i]

        get_permutation(words, i + 1)


def score(dice):
    num_counts = {}
    for number in dice:
        if number in num_counts:
            num_counts[number] += 1
        else:
            num_counts[number] = 1

    result = 0
    for key, value in num_counts.items():
        print("key", key, "value", value)
        if key == 1:
            if value >= 3:
                while value >= 3:
                    result += 1000
                    value -= 3
            if value < 3:
                result += (value * 100)

        elif key == 2:
            if value >= 3:
                while value >= 3:
                    result += 200
                    value -= 3
            if value < 3:
                result += 0

        elif key == 3:
            if value >= 3:
                while value >= 3:
                    result += 300
                    value -= 3
            if value < 3:
                result += 0

        elif key == 4:
            if value >= 3:
                while value >= 3:
                    result += 400
                    value -= 3
            if value < 3:
                result += 0

        elif key == 5:
            if value >= 3:
                while value >= 3:
                    result += 500
                    value -= 3
            if value < 3:
                result += (value * 50)

        elif key == 6:
            if value >= 3:
                while value >= 3:
                    result += 600
                    value -= 3
            if value < 3:
                result += 0

    return result


# Chat GPT solution
# def score(dice):
#     num_counts = {}
#     for number in dice:
#         num_counts[number] = num_counts.get(number, 0) + 1
#
#     result = 0
#     for num, count in num_counts.items():
#         if num == 1:
#             result += (count // 3) * 1000 + (count % 3) * 100
#         elif num == 5:
#             result += (count // 3) * 500 + (count % 3) * 50
#         else:
#             result += (count // 3) * num * 100
#
#     return result

def pick_peaks(arr):
    tmp = {"pos": [], "peaks": []}
    if len(arr) == 1:
        return 0
    print(arr)

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] >= arr[i + 1]:
            tmp["pos"].append(i)
            tmp["peaks"].append(arr[i])

    return tmp


def pick_peaks_answer(arr):
    peak, pos = [], []
    res = {"peaks": [], "pos": []}

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            peak, pos = [arr[i]], [i]

        elif arr[i] < arr[i - 1]:
            res["peaks"] += peak
            res["pos"] += pos
            peak, pos = [], []


def pick_peaks_gpt(arr):
    peaks = {"pos": [], "peaks": []}
    plateau_start = None  # Variable to track the start of a plateau

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            plateau_start = i  # Start of a potential plateau
        elif arr[i] < arr[i - 1] and plateau_start is not None:
            peaks["pos"].append(plateau_start)
            peaks["peaks"].append(arr[plateau_start])
            plateau_start = None  # Reset the plateau start

    return peaks


def sum_strings(x, y):
    if x == "0" and y == "0":
        return "0"
    getcontext().prec = 900
    num_x = Decimal(x) if x != "" else 0

    num_y = Decimal(y) if y != "" else 0

    result = num_x + num_y

    result = "{:f}".format(result)
    return result


def prime(n):
    factors = []
    z = 2
    while z * z <= n:

        if n % z == 0:
            n /= z
            factors.append(z)
        else:
            z += 1
    if n > 1:

        factors.append(int(n))

    print(factors)

prime(64)