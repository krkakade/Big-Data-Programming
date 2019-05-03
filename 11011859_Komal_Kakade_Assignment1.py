#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 00:06:39 2019

@author: komal
"""

from itertools import combinations
S1=input("First String is :")
S2=input("Second String is :")

def longcommonstring(string1,string2):

    num1=len(string1)
    list1 = [combination for i in range(1,num1+1)
        for combination in combinations(string1, i)]

    num2=len(string1)
    list2 = [combination for i in range(1,num2+1)
        for combination in combinations(string2, i)]

    common_pattern=set(list1)&set(list2)

    maximum_length=max(map(len,common_pattern))

    final_list=[x for x in common_pattern if len(x) == maximum_length]

    return(','.join(''.join(i) for i in final_list))  
    
print("Largest Common strings observed:"+longcommonstring(S1,S2))

#string1="abcrqdpt"
#string2="ghabcqrjtp"