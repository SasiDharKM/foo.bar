def answer(l):
    # your code here
    #the idea is to separate out multiples of 3 and its counter-part
    l.sort()
    l.reverse()
    a0 = [] 
    a2 = []
    a1 = []
    for i in l:
        if i % 3 == 0:
            a0.append(i)
        if i % 3 == 1:
            a1.append(i)
        if i % 3 == 2:
            a2.append(i)
    a1mod = int(len(a1)/3)
    a2mod = int(len(a2)/3)
    small = (len(a1)-(a1mod*3)) if (len(a1)-(a1mod*3))<(len(a2)-(a2mod*3)) else (len(a2)-(a2mod*3))
    for i in range(a1mod*3):
    	a0.append(a1[i])
    for i in range(a2mod*3): 
    	a0.append(a2[i])
    for i in range(small):
        a0.append(a1[i+(a1mod*3)])
        a0.append(a2[i+(a2mod*3)])
    a0.sort()
    a0.reverse()
    num = 0
    for i in range(len(a0)):
    	num += a0[i]*(10**(len(a0)-i-1))
    return num