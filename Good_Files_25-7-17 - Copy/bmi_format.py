import array


class BMIFormat:

    def __init__(self):
        # self.values = [] maybe be unnecessary

        self.values = []
        self.counts = {'Normal': 0, 'Overweight': 0,
                       'Obesity': 0, 'Underweight': 0}

    array_items2 = ['Normal', 'Overweight', 'Obesity', 'Underweight',
                    'Normal', 'Overweight', 'Obesity', 'Underweight',
                    'Normal', 'Overweight', 'Obesity', 'Underweight',
                    'Normal', 'Overweight', 'Obesity', 'Underweight',
                    'Normal', 'Overweight', 'Obesity', 'Underweight',
                    'Normal', 'Overweight', 'Obesity', 'Underweight',
                    'Normal', 'Overweight', 'Obesity', 'Underweight', ]

    array_items = ['Normal', 'Normal', 'Normal', 'Normal',
                   'Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Normal', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Normal', 'Obesity', 'Underweight',
                   'Normal', 'Normal', 'Normal', 'Underweight',
                   'Normal', 'Overweight', 'Normal', 'Normal', ]

    def get_bmi_count(self, array_items):
        print("get_bmi_count method initializing")
        print('\n')
        for key in array_items:
            self.counts[key] += 1

    @staticmethod
    def dict_to_array(counts):
        return list(dict.items(counts))

#################################
# ##########   Tests   ##########
#################################

nt = BMIFormat()
nt.get_bmi_count(nt.array_items)
new_list = nt.dict_to_array(nt.counts)

new_list2 = [[new_list[0][0], new_list[1][0], new_list[2][0], new_list[3][0]],
             [new_list[0][1], new_list[0][1], new_list[0][1], new_list[0][1]]]

# new_list = nt.dict_to_array(nt.counts)
# new_list2 = [[new_list[0][0], new_list[1][0], new_list[2][0], new_list[3][0]], [new_list[0][1], new_list[0][1], new_list[0][1], new_list[0][1]]]

print('\n')
print("printing ... nt.counts")
print(nt.counts)
print('\n')
print("printing ... new_list")
print(new_list)
print('\n')
print("printing ... plotly array.. ")
print(new_list2)

# does this go in controller variable or class instance variable?

# delete this example section when done #
# a = [(1, 7), (2, 7), (3, 7), (4, 7)]
# print("print ... a")
# print(a)
# print('\n')
# print("printing ... b")
# b = [[a[0][0], a[1][0], a[2][0], a[3][0]], [a[0][1], a[0][1], a[0][1], a[0][1]]]
# print(b)
# #######################################





#
# print(new_list)
# print('\n')
# print(" ' " + new_list[0][0] + " ' " + " " + str(new_list[0][1]))
# print(new_list[1][0] + " " + str(new_list[1][1]))
# print(new_list[2][0] + " " + str(new_list[2][1]))
# print(new_list[3][0] + " " + str(new_list[3][1]))
#
# print(new_list)
# print('\n')
# print(new_list[0][0] + " " + str(new_list[0][1]))
# print(new_list[1][0] + " " + str(new_list[1][1]))
# print(new_list[2][0] + " " + str(new_list[2][1]))
# print(new_list[3][0] + " " + str(new_list[3][1]))
