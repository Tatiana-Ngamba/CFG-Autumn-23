# 2.1    Write a function that takes in an input and checks to see if it’s an
# isogram. The function should return True or False.
#
# An isogram is a word where no letter is repeated.
# Examples include:
# ●"isogram"
# ●"uncopyrightable"
# ●“ambidextrously”

# Creating a function
def is_an_isogram(word):
    word = word.lower()  # using an inbuilt function to for case sensitivity
    is_isogram = True
    # creating a variable and assigning an inbuilt function to ensure there are no duplicate values
    seen = set()
    # using a for loop to look into each letter to ensure no duplicate
    for letter in word:
        if letter in seen:
            is_isogram = False
            break
        seen.add(letter)

    return is_isogram


# printing varieties of strings
print(is_an_isogram("isogram"))
print(is_an_isogram("uncopyrightable"))
print(is_an_isogram("ambidextrously"))
print(is_an_isogram("Tatiana"))
print(is_an_isogram("mississippi"))
print(is_an_isogram("QUAVERs!"))
print(is_an_isogram("t"))

# def is_an_isogram(word):
#     word = word.lower()
#
#     for letter in word:
#         if letter.count(letter) > 1:
#             return False
#     return True

"""    2.2   Make a new test file and write comprehensive unit tests for the
             function you wrote in 2.1
             For each test case add a comment stating why you chose that case."""
# see file - 'test_Section_2_Concept Questions_Tatiana_Ngamba'
