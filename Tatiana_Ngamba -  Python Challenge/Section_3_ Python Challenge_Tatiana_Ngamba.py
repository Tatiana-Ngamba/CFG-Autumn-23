# Section 3: Python Challenge  [25 marks]
# You are tasked with calculating the minimum classes we need to have, so we know how
# many people to employ. Write a function which when given a number of students,
# calculates and prints out a string for your proposed number of classes, and a
# dictionary showing the allocation.
# Key Constraints:
# ●The maximum size of a class is 30
# ●There needs to be a minimum of 2 classes
# ●The distribution of each class should be as even as possible.
# ●We want to hire as little people as possible - so where possible focus on bigger
# classes, and less of them!
# Inputs/Outputs:
# ●If 31 was the input, the output would be:
# Proposed Allocation: 2 classes
# {'Class 1': 16, 'Class 2': 15}
# ●If 59 was the input, the output would be:
# Proposed Allocation: 2 classes
# {'Class 1': 30, 'Class 2': 29}
# ●If 87 was the input, the output would be:
# Proposed Allocation: 3 classes
# {'Class 1': 29, 'Class 2': 29, 'Class 3': 29}


# allocation values to constraints variable
max_class_size = 30
min_classes = 2


# Write a function which when given a number of students
def calculating_classes(number_of_students):
    # calculating number per class
    number_classes = min(min_classes, number_of_students // max_class_size) + 1
    allocation_class = {}
    # using an if & else statement with while
    if number_of_students <= max_class_size:
        allocation_class['Class 1'] = number_of_students
    else:
        for i in range(number_classes):
            allocation_class[f'Class {i + 1}'] = number_of_students // number_classes

            remaining_students = number_of_students % number_classes
            i = 1
            while remaining_students > 0:
                allocation_class[f'Class {i}'] += 1
                i += 1
                remaining_students -= 1
        # printing values
        print("Proposed Allocation: {} classes".format(number_classes))
        print(allocation_class)


# calling the function with parameters
calculating_classes(31)
# calculating_classes(59)
# calculating_classes(87)
