students =( ("Swuidward","F",60),
           ("Sandy","A",33),
           ("Patrick","B",20),
           ("Sppngebob","D",20),
           ("Mr.krabs","C",78))

grade = lambda grades:grades[2]
# students.sort(key=age)
sorted_students = sorted(students,key=grade)
for i in sorted_students:
    print(i)
