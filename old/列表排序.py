# list1 = ["boy", "cat", "apple"]
# list1.sort()
# list1.reverse()
# print(list1)


# list2 = ["boy", "cat", "apple"]
# list2.reverse()
# print(list2)

# list3 = ["boy", "cat", "apple"]
# # sorted(list3, reverse = False)
# print(sorted(list3, reverse = False))

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
a = sorted(student_tuples, key=lambda student_tuples: student_tuples[2])   # sort by age
print(a)