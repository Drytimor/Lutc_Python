class MyError(Exception): pass

def oops(): raise MyError

def call_oops():
    try:
        oops()
    except IndexError:
        print('caught')

