#qst1
my_list=[]
#qst2
my_list.append("10")
print(my_list)
my_list.append("20")
print(my_list)
my_list.append("30")
print(my_list)
my_list.append("40")
print(my_list)
#qst3
my_list.insert(1, "15")
print(my_list)

my_list2=["50", "60", "70"]
print(my_list2)

#qst4
my_list.extend(my_list2)
print(my_list)

#qst5
my_list.remove("70")
print(my_list)

#qst6
my_list.sort()
print(my_list)

#qst7
index_of_30 = my_list.index("30")
print(f"The index of '30' is: {index_of_30}")

