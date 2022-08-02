#Python Dictionaries by Key or Value



def dic():
    a = key = {}
    
    a[4] = 5452
    a[3] = 986
    a[2] = 98696
    a[1] = 33
    
    
    print(a)
    
    for i in sorted(a.keys()):
        print(i, end="   ")
        
    
    
def main():
    dic()
    
    
    
if __name__ == '__main__':
    main()    