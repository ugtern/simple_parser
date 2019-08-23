import time
import functools


def test_func(numb):
    print('started')
    while True:
        value = yield
        if numb % value == 0:
            print(value)
        else:
            print('you number "{}" is not % to {}'.format(value, numb))


# print(time.time())
# cor = test_func(100)
# cor.send(None)
# time.sleep(2)
# print(time.time())
# time.sleep(5)
# cor.send(11)
# time.sleep(5)
# cor.send(18)
# time.sleep(5)
# cor.send(20)
# cor.close()


def coro(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res.send(None)
        return res
    return wrapper


@coro
def test_deco_coro(numb):
    print('start')
    while True:
        value = yield
        if numb % value == 0:
            print(value)


cor = test_deco_coro(100)
cor.send(10)
cor.send(10)
cor.send(10)
cor.close()