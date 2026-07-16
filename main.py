import os,sys
import json
from pathlib import Path


def hello_world(  ):
    print("hello world")
    x = {"key": "value","name":"test","number":12345}
    unused_var = 42
    return x

def add_numbers(a,b):
    result=a+b
    return result

def bad_formatting( ):
    data=[1,2,3,4,5]
    for i in range(len(data)):
      print(data[i])
    if True:
                print("deeply nested")
    return data

class MyClass:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name

if __name__=="__main__":
    obj = MyClass( "test" )
    hello_world( )
