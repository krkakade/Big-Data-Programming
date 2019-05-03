#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:08:37 2019

@author: komal
"""
from itertools import permutations
S1=input("First String is :")
S2=input("Second String is :")

allcombi=[]
S1_char=list(set(S1))

# function to find out the maximum  
# repeating character in given string 
def maxRepeating(str):   
    n = len(str) 
    count = 0
    cur_count = 1
  
    # Traverse string except  
    # last character 
    for i in range(n): 
          
        # If current character  
        # matches with next and with "."
        if (i < n - 1 and 
            str[i] == str[i + 1] and str[i] == "." ): 
            cur_count += 1

        # If doesn't match, update result 
        # (if required) and reset count 
        else: 
            if cur_count > count: 
                count = cur_count 
               # res = str[i] 
            cur_count = 1
    return count +1

for j in range(maxRepeating(str)):
    permut=permutations(S1_char,j)
    allcombi=allcombi+list(permut)
    A=",".join(["".join(x) for x in allcombi])
    allcombilist=A.split(",")
    while("" in allcombilist) : 
            allcombilist.remove("")
    
#from itertools import combinations

if (len(S1)==0 and len(S2)==0) or (len(S1)>0 and len(S2)==0) or (len(S1)==0 and len(S2)>0):
    print (False)

if not "*" in S2:
    if len(S1)>len(S2):
        print("False")
    elif len(S1)<=len(S2) :
        for i in range(len(allcombilist)):
                h=[]
                lst=[]
                lst.append(S2.replace(".","".join(allcombilist[i])))
                h.append(any(S1 in mystring for mystring in lst))

        if True in h:
                print(True)
        else:    
                print(False)
 
            
