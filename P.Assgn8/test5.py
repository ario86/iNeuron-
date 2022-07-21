# Remove Punctuation From a String

String = "ario's game."

punc = "'."

no_punc = " "

for i in String:
    if i not in punc:
        
        no_punc = no_punc + i

print(no_punc)