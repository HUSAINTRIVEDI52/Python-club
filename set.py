utensils={"Fork","Spoon","Knife"}
dishes={"Bowl","Plate","Cup","Knife"}

utensils.add("Napkin")
utensils.remove("Spoon")
utensils.update(dishes)

# dinner_tsble=utensils.union(dishes)

# for i in dinner_tsble:
#     print(i)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))