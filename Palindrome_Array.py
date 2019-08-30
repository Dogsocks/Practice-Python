"""
https://practice.geeksforgeeks.org/problems/palindromic-array/1
Given a Integer array A[] of n elements.
Your task is to complete the function PalinArray.
Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

Input:
number of test cases
test case x size of the array
the array of potential palindromes in case x
"""


def palin_array(source):
    with open(source) as inp:
        data = inp.read().splitlines()
        noPalin = data.pop(0)
        print("There are " + noPalin + " test cases present")
        newlist = []
        for i in data:
            if len(i) > 2:
                newlist.append(i)
        print(newlist)
        x = []
        for i in newlist:
            x.append((i.split()))
        #print(x)
        count = 0
        for i in x:
           for z in i:
               #print(z)
               if z == (z[:: -1]):
                    count += 1
                    #print("count", count)
           if count != len(i):
                print("0")
           else:
                print("1")
           count = 0



palin_array("example palindrome2.txt")
