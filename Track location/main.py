# Here we install librabry called phone numbers in terminal. After installing we import carrier
from phonenumbers import carrier
import phonenumbers
# parse is used to get phone numbers from phonenumbers library
from phonenumbers.phonenumberutil import parse
from test import number  # importing number variable from test.py file

from phonenumbers import geocoder
# Here C is for Country and H is for History
ch_number = phonenumbers.parse(number, "CH")
# geocoder library is used for getting location
print(geocoder.description_for_number(ch_number, "en"))

# RO is a package of python utilities with an emphasis on cross-platform support
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))  # en is english
