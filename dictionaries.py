# Python3 code to demonstrate 
# each occurrence frequency using 
# dict.get()
  
# initializing string 
test_str = "Mississippi"
  
# using dict.get() to get count 
# of each element in string 
res = {}
  
for keys in test_str:
    res[keys] = res.get(keys, 0) + 1
  
# printing result 
print ("Count of all characters in Mississippi is : \n"
                                             +  str(res))
