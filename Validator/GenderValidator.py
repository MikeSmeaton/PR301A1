from AbstractValidator import AbstractValidator


class GenderValidator(AbstractValidator):
    def __init__(self, value):
        super().__init__(value)
        self.lengthLower = 1
        self.lengthUpper = 1

    def validate(self):
        self.value = self.value.upper()
        self.change_words_to_chars()
        if self.check_characters() is False:
            return False
        return True

    def change_words_to_chars(self):
        if self.value == "MALE":
            self.value = "M"
        if self.value == "FEMALE":
            self.value = "F"

    def check_characters(self):
        if self.value != "M":
            if self.value != "F":
                return False
        return True

    def check_special_cases(self):
        pass
        # There is more than two genders. However to keep it simple we will limit this to two genders.