#!/usr/bin/python3
mydict={}
mydict['a']="first"
mydict['b']="second"
mydict['3']="third"
mydict['4']="fourth"
print ('Keys without sort:')
print (mydict.keys())
print ('Dictionary without sort:')
print (mydict)
test={}
test=mydict
print ('Keys sort:')
print (sorted(test.keys()))
print ('Values sort:')
print (sorted(test.values()))
