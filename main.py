
# if File Not Found:

object = "a_file.txt"
a = [1, 2, 3]
a_dictionary = {"key": "value"}

# The key in handling errors/exceptions is:
# have clear idea that all cases that you want to detect, and
# case by case you raise each exception to have yourself knowing better
# what's going on now.
try:
    file = open(object, "w")
    # print(a[3])
    # print(a_dictionary["sdhjfgk"])

# And By raising exceptions, have thinking about except printing out the
# error that we face, Let's try fixing the code at the same time, and
# printing out the notification to the user of the status now,
# ex: you are asking the lasting version, but there's no new updated version,
# so we gonna roll back the last version to use.
except FileNotFoundError as error_message:
    print(f"{error_message}")
    # file = open(object, "w")
    # file.write("anything")

except KeyError as error_message:
    print(f"That key {error_message} does not exist")

except IndexError as error_message:
    print(f"{error_message} ")
else:
    # if "try" succeed, the next step is "else"
    file.write("Anything")

finally:
    # These codes will run no matter what happened
    file.close()
    print("file closed.")

    # you can raise your own exceptions,
    # ex:
    raise TypeError("This is an error made up by developer")


# ----------------------------let's do another example-----------------------------------------


# Let's try raising an error whenever we need to detect where there may be an error happen:

import math


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Please insert reasonable number. ")

bmi = math.floor(weight / height ** 2)
print(bmi)


# ----------------------------------------------------------------------------------------------


fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    # 0 <= index <= (len(fruit) -1)
#     fruit = fruits[index]
#     try:
#         pass
#
#     except IndexError as message:
#
#         print(f"{message}\nIt's just an ordinary Fruit Pie")
#
#     else:
#         print(fruit + " pie")
#
#     finally:
#         print(f"We have these many elements only: {len(fruits)}")
#
#
# make_pie(3)

    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + "pie")


make_pie(1)

# ------------------------------KeyError Handling---------------------------------------------

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        # total_likes = total_likes + 0
        pass
    # else:
    #     print(total_likes)
print(total_likes)


# ---------------------------Nato Phonetic Alphabet Project-----------------------------------

import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)
# nato_dict = nato_data.to_dict()
# print(nato_dict)

nato_dict = {row.letter: row.code for(index, row) in nato_data.iterrows()}

game = True
while game:
    name = input(f"Enter a word: ").upper()

    try:
        name_char = [f"{char}: {nato_dict[char]}" for char in name]
    except KeyError:
        print("Please input only alphabet. ")
    else:

        # nato_list = [row.code for (index, row) in nato_data.iterrows() if row.letter in name_char]
        # print(nato_list)
        print(f"{name_char}")
    finally:
        continue

        # name = input(f"Enter a word: ").upper()
        # name_char = [char for char in name]
        # result = {n for letter, code in }

        # result = [code for char in name if letter == char for letter, code in nato_dict.items()]
        # print(result)

# ---------------------------------Going back to the Password Manager App---------------------












