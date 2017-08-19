from AbstractValidator import AbstractValidator


class BMIValidator(AbstractValidator):
    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        self.value = self.value.upper()
        if self.check_characters() is False:
            return False
        return True

    def check_characters(self):
        if self.value != "NORMAL":
            if self.value != "OVERWEIGHT":
                if self.value != "OBESITY":
                    if self.value != "UNDERWEIGHT":
                        return False
        return True

    def check_special_cases(self):
        pass

        # No special cases.
        # Must be one of the four options.