t = "232151293111716119"

numList = list(t)

for i in range(len(t)):
    
    a = 1
    
    if i == 17:
        a = 0
    
    num = (t[i]+t[i+a])
    num1 = int(num)
    
    primeDetect = 0
    primeNums = 0
    
    
    
    for i in range(1, num1+1):
        if num1 % i == 0:
            primeDetect += 1
            
            if primeDetect > 2:
                primeNums += 1

print(primeNums)
