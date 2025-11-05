str1="surya"
str2="chintuu"

print(str1+" "+str2)                    #string concatenation.
k=len(str2)                             # string length.
print(k)
#STRING SLICING-------------------------------------------
#syntax : str_name[start_ind:end_ind] 
"""str="suryachowdary07"      
print(str[0:7])                         #string slicing ... 
print(str[:7])                          #string slicing 2...                      
print(str[1:])                           #string slicing 3...

s="APPLE"                                  #A P P L E
print(s[-5:-2])  """                       #-5-4-3-2-1 

#STRING FUNCTIONS------------------------------------------

str="i am a Coder."                                    # 1. str.endswith("x")--> true or false.
print(str.endswith("er."))   

str=str.capitalize() # or print(str.capitalize())       # 2. str.capitalize() --> captilises first character.
print(str)

print(str.replace("c","o"))                             # 3. str.replace("x","y")--> replaces x with y.

print(str.find("coder"))                                # 4.str.find("x") --> return s first index.

print(str.count("am"))                                  # 5.str.count("xyz") --> retunrs the count of substring


#---------------------------------------------------------- 

# LISTS --> It stores set of values of different data types(int,char,float,strin..etc)------------------------
#syntax---- marks=[x,y,q,v,n,....]

marks=[12,25,32,14,56,99]               # (zero) 0 based index
print(marks)
print(marks[5])
print(len(marks))
data=["surya",7,"chintu",7.7]       #different data types..
print(data)

#in string the values cannot be changed but in lists the values an be changed;
"""str3=["surya"]
str[0]='h'
print(str)   """ # it gives us a error(immutable-cannot be changed)

list=["surya",7,"chintu"]
list[0]="garapati"
print(list)       # it does not gives us error;(mutable--can be changed)

#LIST SLICING------------------------------------------------------------------------
# syntax  : list_name[start_ind:end_ind]

marks1=[10,20,30,40,50,60]
print(marks1[1:4])


#LIST FUNCTIONS-----------------------------------------------------------------------

list=[5,2,3,7,8]
# 1-list.appedn(x)
list.append(10)
print(list)

# 2-list.sort()
list.sort()
print(list)

# 3-list.sort(reverse=True)
list.sort(reverse=True)     # sorted in descending order and T should be capital.. (True,False,,)
print(list)

# 4-list.reverse()
list.reverse()
print(list)

# 5-list.insert(index,x)
list.insert(2,4)
print(list)

# 6-list.remove(x) -- removes the first occurances of x;
list.remove(2)
print(list)

# 7-list.pop(index) -- del the element at index;
list.pop(2)
print(list)

#TUPLES-------------------------------------------------------------------------------
#The built in datatype that lets us to create immutable(cannot be changed) equences of values
# SYNTAX-- tupple_name=(a,b,c,d,e,f...)
#tupple_name[x]=y    //** not allowed
tup=(2,1,5,4,7,8)
print(tup)
print(tup[4])

# TUPLE SLICING :-----------------------------------------------------------
print(tup[1:5])

#TUPLE METHODS---------------------------------------------------------------------

# 1-tup.index(x)  --- returns the index of first element
print(tup.index(7))

# 2- tup.count(x) --- count total occurances
print(tup.count(7))

#DICTIONARIES----------------------------------------------------------
#dictionaries are used to store the data values in key-value pairs
# they are unordered , mutable and dont allow duplicates
#dict["key"]="value"
dict={
    "key":"value",
    "name":"surya",
    "cgpa":9,
    "marks1":[12,56,89,34,99],
}
print(dict) 
print(dict["name"])
print(dict["marks1"])
dict["name"]="chintu"
print(dict["name"])
dict["gender"]="male"         # you can add(mutable)
print(dict)

 # NESTED DICTIONARIES:-----------------------------------------------------------
student={
    "name" : "surya",
    "subjects" :{
        "phy" : 99,
        "che" : 89,
        "mat" : 92,
    }
}
print(student)
print(student["subjects"]) 
print(student["subjects"]["phy"])

# dictioniaries functions-----------------------------------------------------------

# 1- dict.keys()
print(student.keys())

# 2- dict.values()
print(student.values())
 
# 3-dict.items()         -- return all key, val pairs
print(student.items()) 
  
# 4- dict.get("key")
print(student.get("name"))

# 5- dict.update("key","value")
student.update({"prof":"B-tech"})
print(student)
   # OR
new_dict={"PProf" : "btech"}
student.update(new_dict)
print(student)


# SETS :----------------------------------------------------------------------------------
# sets is a collection of unordered items and each elmnt in set is unique nd immutable--

#syntax== set={a,b,c,d.....}

set={1,2,2,5,7,7,7,"surya","chintu",7.07,"chintu"}
print(set)
print(len(set)) 

#  SET FUNCTIONS------------------------------------------------------------------------

# 1-set.add(x)    -- adds the element
set.add(9)
print(set)

# 2-set.remove(x)  -- removes the element with the value of x
set.remove(7)
print(set)

# 3-set.clear() -- claers the set
#set.clear()

# 4.set.pop()  -- removes a random element
print(set);

# SET METHOD ------------------------------------------------------------

# 1) set.union(set2) --- combines both the set values and returns the new set..
 
set1={1,2,3}
set2={2,4,5}

print(set1.union(set2)) 
print(set1)
print(set2)

# 2) set.intersection -- gives the comman elements 

print(set1.intersection(set2))

#FOR LOOP ITERATION USING LOOP----------------------
list2=[1,2,3,4,5]
# for i in list2:
#     print(i)

# FOR LOOP WITH ELSE ----------------------------------
for i in list2:
    print(i) 
else :
    print("end")


#PASS STATEMENT - pass is a null tatement that does nothing .it is used as a placeholder for futture code
for i in range(5):
    pass
print("---end")

#====================================================================================================
# import numpy as np
# M1=np.array([[2,4,6,8,10],[3,6,9,-12,-15],[4,8,12,16,-20],[5,-10,15,-20,25]])
# print(M1)
# print(M1[:,1]) 
# print(M1[:,-1])

#====================================================================================================
# use of numpy for matrix operations
# import numpy 
# x=numpy.array([[1,2],[3,4]])
# y=numpy.array([[7,8],[9,10]])
# # add() for add matrices
# print(numpy.add(x,y))
# # subtract()
# print(numpy.subtract(x,y))
# # divide()
# print(numpy.divide(x,y))
# # multiply()
# print(numpy.multiply(x,y))
# # dot()
# print(numpy.dot(x,y))
# # sqrt()
# print(numpy.sqrt(x))
# print(numpy.sqrt(y))
# # pow(x,int)
# print(numpy.pow(x,2))

#================================================================================
# arange()
# import numpy as np
# a=np.arange(10,20,1)
# print(a)
# print(a[:10])
# print(a[:])
# print(a[0:])
# print(a[-1:-11:-1])

# import numpy as np
# a=np.arange(10,20,1)
# print(a)
# print(a[4::-1])
# print(a[4:-11:-1])
# print(a[-6::-1])
# print(a[-6:-11:-1])
#==================================================================================
1
