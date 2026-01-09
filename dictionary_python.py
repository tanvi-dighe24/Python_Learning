Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
item={'dosa':100,'idly':50,'poori':80,'vada':60} #creating_dictionary
item
{'dosa': 100, 'idly': 50, 'poori': 80, 'vada': 60}
#accessing_in_dictionary
#syntax= variable_name[key]
item['poori']
80
item['vada']
60
#accessing_only_key_part
print(item.keys())
dict_keys(['dosa', 'idly', 'poori', 'vada'])
#modifying_in_dictionary
#syntax= variable_name[key]=new_value
item['dosa']=120
item
{'dosa': 120, 'idly': 50, 'poori': 80, 'vada': 60}
#Rule: 1)keys must be unique
      #2)Dictionary is mutable
      #3)keys should be immutable(strings,tuple)
      #4)keys cant be duplicate
#Operations_on_Dictionary
#delete_elemen
#syntax: del dict_name[key]
del item['poori']
item
{'dosa': 120, 'idly': 50, 'vada': 60}
#pop() will delete key & its value but also returns/prints corrosponding value
#syntax: dict_name.pop(key)
item.pop(vada)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    item.pop(vada)
NameError: name 'vada' is not defined
>>> item.pop('vada')
60
>>> item
{'dosa': 120, 'idly': 50}
>>> #checking for existence
>>> #syntax: key_name in dict_name
>>> 'vada' in item
False
>>> 'dosa' in item
True
>>> #dictionary funtions and methods
>>> #len() syntax: len(dict_name)
>>> len(item)
2
>>> #2)clear() method
>>> #syntax: dict_name.clear()
>>> #clear() makes empty dictionary
>>> #3)get() method
>>> #syntax: dictionary_name.get(key,[default])
>>> item.get('idly')
50
>>> #keys() syntax: dictionary_name.keys()
>>> item.keys()
dict_keys(['dosa', 'idly'])
>>> #items() returns all items in dictionary
>>> #dict_name.items()
>>> item.item()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    item.item()
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
>>> item.items()
dict_items([('dosa', 120), ('idly', 50)])
>>> #6)values() syntax: dictionary_name.values()
>>> item.values()
dict_values([120, 50])
