# Function that is capable of pulling every other item out of a list and
# creating a new list out of those items.  Using a for loop, len method Using
# the modulo operator.

def every_other(sort_list):
    new_list=[]

    for i in range (len(sort_list)):
        if i % 2==0:
            new_list.append (sort_list[i])

    return new_list

# Test list function call:

sorted_list=every_other(["This","is","a","test","list"])

print(sorted_list)
