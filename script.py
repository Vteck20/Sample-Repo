import sys
import requests
from os import rename
import math

print (sys.version)
print(sys.executable)


def greet(hi_greet):
   
    greeting = "hello, {}".format(hi_greet)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)
