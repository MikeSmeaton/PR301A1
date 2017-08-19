from Validator import Validator


test = Validator("aaa", "m", "18", "200", "normal", "21", "20-01-1990")

print(test.validate().get_age())

# if test.validate() is True:
#     print("True")
# else:
#     print("False")