from AbstractValidator import AbstractValidator


class AgeValidator(AbstractValidator):
    def __init__(self, value):
        super().__init__(value)
        self.lengthLower = 2
        self.lengthUpper = 2

    def validate(self):
        if self.check_length() is False:
            return False
        if self.check_characters() is False:
            return False
        if self.check_special_cases() is False:
            return False
        return True

    def check_characters(self):
        bad_chars = ""
        for char in self.value:
            if char not in self.numericalChars:
                bad_chars += char

        if bad_chars == "":
            return True
        else:
            return False

    def check_special_cases(self):
        if self.value == "00":
            return False
        return True
        # Also check for employees under a certain age.
        # People younger than a certain age shouldn't work for us or too old.