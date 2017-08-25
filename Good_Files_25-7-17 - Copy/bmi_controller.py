from bmi_format import BMIFormat, nt

class BMIController:

    def __init__(self):
        self.new_list = nt.dict_to_array(nt.counts)

    def make_list(self, new_list):
        new_list2 = [[new_list[0][0], new_list[1][0], new_list[2][0], new_list[3][0]],
                     [new_list[0][1], new_list[0][1], new_list[0][1], new_list[0][1]]]
        return new_list2

jc = BMIController()
print(jc.make_list(jc.new_list))
