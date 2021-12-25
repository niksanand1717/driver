import re

class Security():
    securepattern=r''

class PhoneNumber(Security):
    securepattern = r'[0-9]{10}'

class Name(Security):
    securepattern = r'[^0-9]'
