"""Задача 1. 50 баллов
Написать функцию которая будет добавлять код страны
к номеру телефона с помощью замыкания
внешний вид вызова функции.
my_number = user_telephone('+044')
my_number('838372893')
+044838372893 результат."""
# create a function
def full_telephone_number(code):
    # create another function in the body of the first function
    def country_code(number):
        # the result of the function is the addition of two inputs
        return code + number
    # making a closure
    return country_code

# output the result of the function by substituting the values into it
print(full_telephone_number('+044')('838372893'))
