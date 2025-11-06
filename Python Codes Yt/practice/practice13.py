"""write a function called has_duplicates that thakes a list 
and returns True if there ia any element that appears more 
than once . It should not modify the original list"""

"""here we have to check weather the list has duplicate values"""

def has_duplicates(lst):
    return len(set(lst)) != len(lst)
print(has_duplicates([1,2,2,3]))