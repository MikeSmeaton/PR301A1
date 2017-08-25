import array


class BmiFormat:

    def __init__(self):
        # self.values = [] maybe be unnecessary

        self.values = []
        self.counts = {'Normal': 0, 'Overweight': 0,
                       'Obesity': 0, 'Underweight': 0}

    array_items = ['Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight', ]

    def get_bmi_count(self, array_items):
        print("get_bmi_count method initializing")
        for key in array_items:
            self.counts[key] += 1

    @staticmethod
    def dict_to_array(counts):
        return list(dict.items(counts))


#################################
# ##########   Tests   ##########
#################################

nt = BmiFormat()
nt.get_bmi_count(nt.array_items)

# does this go in controller variable or class instance variable?
new_list = nt.dict_to_array(nt.counts)

print(new_list)
print(new_list[0][0] + " " + str(newlist[0][1]))
print(new_list)
print(new_list)
