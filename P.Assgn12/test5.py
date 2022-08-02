#insertion at the beginning in OrderedDict


from collections import OrderedDict
 
iniordered_dict = OrderedDict([('ario', '1'), ('sam', '2')])
 

iniordered_dict.update({'dan':'3'})
iniordered_dict.move_to_end('dan', last = False)
 

print (str(iniordered_dict))