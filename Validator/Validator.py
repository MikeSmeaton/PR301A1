from EMPIDValidator import EMPIDValidator
from GenderValidator import GenderValidator
from AgeValidator import AgeValidator
from SalesValidator import SalesValidator
from BMIValidator import BMIValidator
from SalaryValidator import SalaryValidator
from BirthdayValidator import BirthdayValidator
from Entry import Entry


class Validator(object):
    def __init__(self, new_empid, new_gender, new_age, new_sales, new_bmi, new_salary, new_birthday):
        self.empid = new_empid
        self.gender = new_gender
        self.age = new_age
        self.sales = new_sales
        self.bmi = new_bmi
        self.salary = new_salary
        self.birthday = new_birthday

    def validate(self):
        if self.do_validation() is False:
            return None
        return Entry(self.empid, self.gender, self.age, self.sales, self.bmi, self.salary, self.birthday)

    def do_validation(self):
        if EMPIDValidator(self.empid).validate() is False:
            return False
        if GenderValidator(self.gender).validate() is False:
            return False
        if AgeValidator(self.age).validate() is False:
            return False
        if SalesValidator(self.sales).validate() is False:
            return False
        if BMIValidator(self.bmi).validate() is False:
            return False
        if SalaryValidator(self.salary).validate() is False:
            return False
        if BirthdayValidator(self.birthday, self.age).validate() is False:
            return False
        return self.empid + " " + self.gender + " " + self.age + " " + self.sales + " " + self.bmi + " " + self.salary + " " + self.birthday
