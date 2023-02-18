def sum_list(lst):
    return sum(lst)

n = int(input("Enter the length of the list: "))

lst = []
for i in range(n):
    elem = int(input("Enter element {}: ".format(i+1)))
    lst.append(elem)

sum_of_list = sum_list(lst)

print("The sum of the list is:", sum_of_list)
