#if-else
'''a=5
b=10
if a<b:
    print("less")
else:
    print("false")'''

'''a=5
b=10
if a>b:
    print("less")
else:
    print("false")'''

    
'''a=4
b=8
if a!=b:
    print("not equal")
else:
    print("equal")'''

'''a=3
b=3
if a==b:
    print("equal")a=5
    
else:
    print("false")

a=7
b=11
if a<=b:
    print("less")
else:
    print("true")'''
#if else with logical operators

'''a=5
b=4
if a>b and a!=b:
    print("not equal")
else:
    print("equal")'''
'''a=6
b=12
if a!=b or a==b:
    print("not equal")
else:
    print("false")'''
'''a=5
b=4
if a!=b and not a<b:
    print("true")
else:
    print("false")'''
#if-else with identity operators
"""a=7.8
if type(a) is float:
    print("true")
else:
    print("false")"""

'''a=4,5,6,7,8,9,10
if 7 in a:
    print("true")
else:
    print("false")
    
a=4,5,6,7,8,9,10
if 15 not in a:
    print("true")
else:
    print("false")'''
#run time input
'''a=int(input())
b=int(input())
if a>b:
    print("true")
else:
    print("false")'''
'''a=4,5,6,7,8,9
b=int(input())
if b in a:
    print("element exists")
else:
    print("not exists")'''

#if-elif
'''a=8
b=16
if a<b:
    print("less")
elif b>a:
    print("greater")'''
'''a=8
b=16
if a>b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")'''

#if-elif-else
'''a=2
b=4
if b<a:
    print("less")
elif a==b:
    print("equal")
elif a>b:
    print("not equal")
else:
    print("true")'''

#multiple-if conditions
'''a=6
b=8
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")

a=6
b=8
if a<b:
    print("less")
if b<a:
    print("greater")
if a==b:
    print("not equal")'''

'''a=6
b=8
if a>b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''
#nested-if
'''a=3
b=2
if a>b:
    print("greater")
    if a==b:
        print("equal")'''
'''a=3
b=2
if a>b:
    print("greater")
    if a!=b:
        print("not equal")'''
'''a=3
b=2
if a<b:
    print("greater")
    if a!=b:
        print("equal")
a=3
b=2
if a<b:
    print("greater")
    if a!=b:
        print("equal")
else:
    print("false")'''
'''name=input("enter the name")
if name=="Vijaya":
    print("true")
elif name=="geetha":
    print("match")
elif name=="hari":
    print("false")
else:
    print("invalid")'''

a="pooja"
if a=="vijay":
    print("match")
