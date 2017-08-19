from AbstractValidator import AbstractValidator


class BirthdayValidator(AbstractValidator):
    def __init__(self, value, age):
        super().__init__(value)
        self.age = age
        self.day = None
        self.month = None
        self.year = None

    def validate(self):
        # self.split_date_up()
        return True # So far just return true. Work on it later.

    def split_date_up(self):
        pass

    def check_characters(self):
        pass

    def check_special_cases(self):
        pass

        # Must match Age value.
        # Year value (dictating age) must be realistic.
        #       -Must not be in the future
        #       -Must be of a reasonable age to be employed. Not too young or too old.
        #       -Must fit with date requirements. Eg no feb 31.