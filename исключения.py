def fetcher(obj, index):
    print(obj[index])

def catcher():
    try:
        fetcher('a',4)
    except IndexError:
        print('got exception')
    print('continuing')

# catcher()

"""
class AlreadyGotOne(Exception): pass

def grail():
    raise AlreadyGotOne()

try:
    grail()
except AlreadyGotOne:
    print('got exception')
    """

"""
try:
    fetcher('a', 0)
finally:
    print('after fetch')
    
    """

def after():
    try:
        fetcher('a', 3)
    finally:
        print('after fetch')  # поток перейдет в блок finally после исключения
    print('after try?')  # при исключении стандартный поток не возобновиться



# try/except/else
# после выполнения блока except поток управления возобновляется ниже полного оператора try
def new():
    try:
        fetcher('a', 3)  # оператор выполняемый первым (главное действие)
    except IndexError:  # выполняется если сгенерировалось исключение IndexError
        print('IndexError')
    except (KeyError, ValueError):  # выполняется если сгенерировалось исключение KeyError или ValueError
        print('KeyError, ValueError')
    except:  # выполняется если сгенерировалось любое исключение
        print('All exception')
    else:  # выполняется если в блоке try исключение не сгенерировалось
        print('Else exception')


def kaboom(x, y):
    print(x + y)
def new_():
    try:
        kaboom('123',[1,2])  # возвратиться в код который сгенерировал ошибку возможности нет
    except TypeError:
        print('Hello world!')
    print('resuming here')

# try/finally

class MyError(Exception): pass

def stuff(file):
    raise MyError()

def new__():
    file = open('datafile.txt', 'w')
    try:
        stuff(file)
    finally:
        file.close()
    print('not reached')


# try/except/else/finally


"""
try:
    главный поток
except:
    обработчик
else:
    обработчик в случаи отсутствия исключения
finally:
    охватывает все остальное
"""

sep = '-' * 45 + '\n'

def exc1():
    print(sep + 'EXCEPTION raised and caught')
    try:
        x = 'spam'[99]
    except IndexError:
        print('except run')
    finally:
        print('finally run')
    print('after run')

def exc2():
    print(sep + 'NO EXCEPTION raised')
    try:
        x = 'spam'[1]
    except IndexError:
        print('except run')
    finally:
        print('finally run')
    print('after run')

def exc3():
    print(sep + 'NO EXCEPTION raised, WITH ELSE')
    try:
        x = 'spam'[1]
    except IndexError:
        print('except run')
    else:
        print('else run')
    finally:
        print('finally run')
    print('after run')


def exc4():
    print(sep + 'NO EXCEPTION raised BUT NOT CAUGHT')
    try:
        x = 1/0
    except IndexError:
        print('except run')
    finally:
        print('finally run')
    print('after run')
#
# exc1()
# exc2()
# exc3()
# exc4()

# raise
"""
raise IndexError
raise IndexError()
"""
"""
exc = IndexError()
raise exc
"""
"""
excs = [IndexError, ValueError]
raise excs[0]
"""
"""
class MyExc(Exception): pass


try:
    raise MyExc('spam')
except MyExc as X:
    print(X.args)
"""
"""
x = 99

try:
    1 / 0
except Exception as x:"""  # python локализует переменную х и удаляет ее при выходе
""" print(x)"""
""" 
print(x)"""  # NameError: name 'x' is not defined
"""
try:
    1/0
except Exception as E:
    raise TypeError('bad') from E
"""


def f(x):
    assert x < 0, 'x must be negative'
    return x**2
"""
with open('datafile.txt') as f1, open('datafile2.txt') as f2:
    for (line_num, (line1, line2)) in enumerate(zip(f1, f2)):
        print(line_num, line1, line2)
"""


"""
class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser1(): raise General()
def raiser2(): raise Specific1()
def raiser3(): raise Specific2()

for func in raiser1, raiser2, raiser3:
    try:
        func()
    except General:
        import sys
        print(f"caught {sys.exc_info()[:]}")"""  # caught (<class '__main__.Specific2'>, Specific2(), <traceback object at 0x1098dc340>)
"""
class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser1(): raise General()
def raiser2(): raise Specific1()
def raiser3(): raise Specific2()

for func in raiser1, raiser2, raiser3:
    try:
        func()
    except General as x:
        import sys
        print(f"caught {x.__class__}") """  # caught <class '__main__.General'>



class FormatError(Exception):
    logfile = 'logfile.txt'
    def __init__(self, line, file):
        self.line = line
        self.file = file
    def logerror(self):
        log = open(self.logfile, 'a')
        print(f'Error at {self.file}, {self.line}', file=log)

def parser():
    raise FormatError(1, 'datafile.txt')

def main_name():
    try:
        parser()
    except FormatError as exc:
        exc.logerror()



def action2():
    print(1 + [])  # при генерации исключения в try/except
    # поток управления передается только первому блоку try

def action1():
    try:
        action2()
    except TypeError:
        print('inner try')  # inner try
def action3():
    try:
        action1()
    except TypeError:
        print('outer try')

def action4():
    try:
        try:
            action2()
        except TypeError:
            print('inner try')  # inner try
    except TypeError:
        print('oter try')

def raise1(): raise IndexError
def noraise():return
def raise2(): raise SyntaxError

def raise5():
    for func in raise1, noraise, raise2:  # выполняется блок finally независимо возникло исключение или нет
        print(f"{func.__name__}")
        try:
            try:
                func()
            except IndexError:
                print('cought IndexError')
        finally:
            print('finally run')
        print('...')


# прерывание множества вложенных циклов "безусловный переход"

class ExitLoop(Exception): pass

def exc_1():
    try:
        while True:
            while True:
                for i in range(10):
                    if i > 3: raise ExitLoop  # исключение прерывает все вложенные циклы
                    # и переходит сразу в блок except
                    #  если вместо raise вставить оператор break выход произойдет только
                    # из последнего вложенного цикла - будет бесконечный цикл

                    print(f'loop3:{i}')
                print('loop2')
            print('loop1')
    except ExitLoop:
        print('continuing')  # continuing
    print(i)  # 4

def exc_2():
    while True:
        try:
            line = input()
        except EOFError:
            break
        else:
            print('stop')


# выполнение условий с помощью raise

class Found(Exception): pass

def searcher():
    if True:
        raise Found
    else:
        return
def searcher2():
    try:
        searcher()
    except Found:
        print('element found')
    else:
        print('element ton found')



# такая структура используется когда функция не может возвратить индикаторное значение обозначающее успех или неудачу

class Failure(Exception):
    def method(self):
        print('get use')

def searcher3():
    if True:
        return 'element found'
    else:
        raise Failure()
def searcher4():
    try:
        item = searcher3()
    except Failure:
        print('element not found')
    else:
        'use element'

# полиморфизм к исключениям

try:
    ...
except Failure as instance:
    instance.method()  # выполнение действий над данной экземпляром


# регистрация ошибок

import traceback

def inverse(x):
    return 1/x
def exc_4():
    try:
        inverse(0)
    except Exception:
        traceback.print_exc(file=open('badly.exc', 'w'))  # выводит данные об ошибке в файл
    print('Bay')




