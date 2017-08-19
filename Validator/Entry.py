class Entry(object):
    def __init__(self, new_empid, new_gender, new_age, new_sales, new_bmi, new_salary, new_birthday):
        self.empid = new_empid
        self.gender = new_gender
        self.age = new_age
        self.sales = new_sales
        self.bmi = new_bmi
        self.salary = new_salary
        self.birthday = new_birthday

    def to_string(self):
        return self.empid + " " + self.gender + " " + self.age + " " + self.sales + " " + self.bmi + " " + self.salary + " " + self.birthday

    def get_empid(self):
        return self.empid

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_sales(self):
        return self.sales

    def get_bmi(self):
        return self.bmi

    def get_salary(self):
        return self.salary

    def get_birthday(self):
        return self.birthday