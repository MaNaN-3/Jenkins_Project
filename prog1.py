#!/usr/bin/python3
def vowel(s):
    arr=['a','e','i','o','u']
    ans=0
    for i in enumerate(s):
        if i[1] in arr:
            ans+=1
    return ans
