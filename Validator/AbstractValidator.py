from abc import ABCMeta, abstractmethod
from array import array


class AbstractValidator(metaclass=ABCMeta):
    lengthLower = None
    lengthUpper = None
    alphabetChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
    numericalChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def validate(self):
        pass

    def check_length(self):
        if len(self.value) >= self.lengthLower:
            if len(self.value) <= self.lengthUpper:
                return True
        return False

    @abstractmethod
    def check_characters(self):
        pass

    @abstractmethod
    def check_special_cases(self):
        pass
