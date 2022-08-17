"""Задача 1. 50 баллов
Видосик по Замыканиям просмотреть
и повторить за автором.
мне скинуть файлик с повтором или своим примером"""

def one():
    x = ['one', 'two']
    def inner():
        print(x)
        print(id(x))
    return inner

a = one()
o = a.__closure__[0].cell_contents
o.append('asdf')
a()
