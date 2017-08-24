# import entry
import array

class Thing:

    def __init__(self):
        self.normal = 0
        self.overweight = 0
        self.obesity = 0
        self.underweight = 0
        self.keys = ['Normal', 'Overweight', 'Obesity', 'Underweight']
        self.values3 = []
        #self.bmi_count = []
        #self.bmi_count[0][0] = 'Normal'
        #self.bmi_count[0][1] = 'Overweight'
        #self.bmi_count[0][2] = 'Obesity'
        #self.bmi_count[0][3] = 'Underweight'

        self.counts = {'Normal': self.normal, 'Overweight': self.overweight,
                  'Obesity': self.obesity, 'Underweight': self.underweight}

        self.counts2 = {'Normal': 0, 'Overweight': 0,
                  'Obesity': 0, 'Underweight': 0}


    array_items = ['Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight',
                   'Normal', 'Overweight', 'Obesity', 'Underweight', ]

    def get_bmi_count(self, array_items):
        for key in array_items:
            print("loop iteration begin..")
            self.counts2[key] += 1

#    def sort_stuff(self):



            #self.bmi_count[0][0], [0][1], [0][2], [0][3] = \
        #    'Normal', 'Overweight', 'Obesity', 'Underweight'



        #for items in array_items:
        #    if items == 'Normal':
        #        self.normal += 1
        #    elif items == 'Overweight':
        #        self.overweight += 1
        #    elif items == 'Obesity':
        #        self.obesity += 1
        #    elif items == 'Underweight':
        #        self.underweight += 1

#        self.bmi_count[1][0] = self.normal
#        self.bmi_count[1][1] = self.overweight
#        self.bmi_count[1][2] = self.obesity
#        self.bmi_count[1][3] = self.underweight




nt = Thing()
nt.get_bmi_count(nt.array_items)
print(nt.counts2)

print (dict.values(nt.counts2))
print('\n')
print (dict.keys(nt.counts2))
print("words")
#print(dict.keys(nt.keys)
#dict.values(nt.counts2))
#print('\n keys')
#print(nt.key)
#print('\n values3')
#print(nt.values3)
#print('\n counts')
#print(nt.counts)
