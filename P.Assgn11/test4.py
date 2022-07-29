#binary or not string

a = '01101111'
b = {'0','1'}
t = set(a)

if b == t or t == {'0'} or t == {'1'}:
    print(" binary string")
else:
    print(" not binary string")
