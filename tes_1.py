from functools import wraps
from multiprocessing import Process
from test.api_server import app
# def twrap(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print(11)
#         return func(*args,**kwargs)
#     return wrapper
# @twrap
def func():
    print("func")


if __name__ == '__main__':

    p=Process(target=func())
    p.start()
    # p.join()