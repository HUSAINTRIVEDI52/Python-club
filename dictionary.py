capitals={'USA' :'Washington DC',
        'INDIA':'New delhi',
        'China':'Beijing',
        'Russia':'Moscow'   }

# print(capitals['germany'])
# print(capitals.get("germany"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key,value in capitals.items():
#     print(key,value)

capitals.update({'Germany':'Berlin'})
capitals.update({'INDIA':'Rajkot'})
capitals.pop('China')
print(capitals)