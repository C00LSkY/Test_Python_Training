# -*- coding: utf-8 -*-

import os.path
import jsonpickle
import getopt
import sys
from model.contacts import Anketa
import random
import string


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of users", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a




def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits_string(prefix, maxlen):
    symbols_num = string.digits
    return prefix + "".join([random.choice(symbols_num) for i in range(random.randrange(maxlen))])


testdata = [
            Anketa(firstname=random_string("firstname", 10), midlename=random_string("midlename", 10),
                   lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                   company=random_string("company", 10), address=random_string("address", 10),
                   home_tel=random_digits_string("+", 10), mobile_tel=random_digits_string("+", 10),
                   work_tel=random_digits_string("+", 10), email=random_string("@", 10), email2=random_string("@", 10),
                   email3=random_string("@", 10), byear=random_digits_string("", 4), address2=random_string("address2", 15))
             for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
