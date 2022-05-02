"""
author Name : Shishir 
author FB Link : facebook.com/shishirislam80
author github link : github.com/Devsabirul
"""
# creating an empty list
lists = []
# number of elemetns as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
    ele = int(input())
    lists.append(ele)  # adding the element

# Calculate Normalization

print("------------------------------")
print("Normalization Value Is : ")


def normalization(x, list):
    a = x - min(list)
    b = max(list) - min(list)
    return a / b


for i in lists:
    print(normalization(i, lists))
