from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numbers(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", middle_name="", last_name="", nickname="", title="", company="", address="",
                    phone_home="", phone_mobile="", phone_work="", fax="", email_1="", email_2="", email_3="",
                    homepage="", address_2="", phone_2="", notes="")] + [
               Contact(first_name=random_string("first name", 10), middle_name=random_string("middle name", 10),
                       last_name=random_string("last name", 10), nickname=random_string("nickname", 10),
                       title=random_string("title", 5), company=random_string("company", 10),
                       address=random_string("address", 20), phone_home=random_numbers("22", 7),
                       phone_mobile=random_numbers("22", 7), phone_work=random_numbers("22", 7),
                       fax=random_numbers("22", 7), email_1=random_string("email1", 10),
                       email_2=random_string("email2", 10), email_3=random_string("email2", 10),
                       homepage=random_string("homepage", 10), address_2=random_string("address2", 10),
                       phone_2=random_numbers("22", 7), notes=random_string("notes", 20))
               for i in range(n)
           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
