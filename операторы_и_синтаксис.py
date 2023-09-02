# Программы состоят из модулей
# Модули содержать операторы,
# Операторы содержат выражения,
# Выражения создают и обрабатывают объекты

# распаковывающее присваивание
"""
name, age = ['lee', 20]"""
# python распаковывает список или кортеж и присваивает им ссылки
# слева на права name='lee' age=20
"""
print(name, age)"""
# расширенная распаковка последовательности
"""
*name, age, other = ('lee', 20, 'city', 'sbp', 10)"""
"""
print(name) """  # ['lee', 20, 'city']
"""
print(age)"""  # sbp
"""
print(other)  # 10
"""
# при помощи оператора * распаковки, переменная будет всегда содержать список
# остатков объектов независимо от положения *
"""
l = [1,2,3,4]
while l:
    front, *l = l
    print(front,l)"""
# 1 [2, 3, 4]
# 2 [3, 4]
# 3 [4]
# 4 []
"""
for (a,*b,c) in [(1,2,3,4), (5,6,7,8), (9,10,11,20,20,20)]:
    print(a,b,c)"""
# 1 [2, 3] 4
# 5 [6, 7] 8
# 9 [10, 11, 20, 20] 20


# функция print
# это форма перенаправления потока данных
# по умолчанию текст отправляется в стандартный поток вывода в той же программе в который выполняется
"""
import sys"""
# stdout - это место куда по умолчанию отправляется текстовый вывод программы
"""
sys.stdout.write('hello world\n')"""
"""
x = 'hello'
y = [1,2,3]
z = 12"""
# записал в файл datafile.txt hello...[1, 2, 3]...12
"""
print(x,y,z, sep='...', file=open('datafile.txt', 'w'))"""
# отображение текста файла
"""
print(open('datafile.txt').read())"""
# hello...[1, 2, 3]...12
# print всего лишь отправляет текст методу sys . stdout. write,
# длинный сценарий
"""
import sys
temp = sys.stdout"""  # сохранение текущего потока с целью его восстановления
"""
sys.stdout = open('datafile.txt', 'a')"""
"""
print('spam')"""  # запись в файл
"""
print(1, 2, 3)"""  # запись в файл
"""
sys.stdout.close() """ # сброс вывода на диск
"""
sys.stdout = temp"""  # восстановление исходного потока
"""
print('back here')"""  # back here
"""
print(open('datafile.txt').read())"""
# spam
# 1 2 3

# короткий сценарий
"""
x = 'hello'
y = [1,2,3]
z = 12
"""
"""
log = open('datafile.txt', 'w')"""
"""
print(x,y,z, sep='\n', file=log)"""  # запись в файл
"""
print(x,y,z)"""  # вывод в исходный stdout

# if - оператор потока управления
"""
def hello():
    return 'hello'
def sum():
    return 1+1

def default():
    return 'Not...function'

branch = {
    'greeting': hello,
    'sum': sum,
    'city': lambda: 'lambda function',
}

print(branch.get('city_', default)())
"""
"""
if ([] == [1,2] and
        {} == {1,2} or
        () == (1,2) or
        {'key': 'value'} == {'name': 'lee'}):
    print('Ok')
    """

"""
if 1: print('hello')"""
"""
a = ['false', 'true'][bool('')]
print(a)
"""