DICTIONARIES AND STRUCTURING DATA

Dictionary:
- mutable collection
- index can be any value, not just integer like list (i know it, it's "key:value pair collection ")
- '{}'
- KeyError for accessing item not present 
Dict vs Lists
- Dict. are *UNORDERED*
    - That affects comparison, 2 dicts are the same, if key-value pairs match in both no matter the "position"
    - thus slices does not work like in list

Methods keys(), values(), items()
- return is list like values as metnioned
    - good for looping with for
    - if I want return saved as list: `list(dict_name.keys())` or similar
    - good practice -> multiple assignment for k,v in dict.items():

Existence of item with `in` and `not in`

Method get()
- returning value if key is in Dict
- 2args method: 1st key to check value exists , if not return 2nd default value (save checking value in Dict)    

Method setdefault()
- set default value for particular key
- 2args: 1st is key, 2nd default value

Pretty Prenting - pprint() and pformat()
- it pretty prints dict values :D

Data structure to model real world things (chess) with lists and dicts

Nested Dicts and Lists

