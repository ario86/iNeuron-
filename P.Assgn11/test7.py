#special character in string


import re


a = "Hello$"
 
special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')


if(special_char.search(a) == None):
    print('no special characters')
else:
    print('it has special characters')