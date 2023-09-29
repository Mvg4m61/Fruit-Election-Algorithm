def favFruit():
    n,m = [int(x) for x in input().split()]
    arrprefer = []
    for i in range(m):
        peepsarr = list(map(int, input().split()))
        arrprefer.append(peepsarr)
    fruits = [int(x) for x in range(1,n+1)]
    score = []
    count = 0
    while len(fruits)!=1:
        
        for el in fruits:
            for person in arrprefer:
                if el == person[0]:
                    count = count + 1
            score.append(count)
            count = 0
        minval = min(score)
        for i in range(len(score)):
            
            if score[i]==minval:
                
                z = fruits.pop(i)
                
                for person in arrprefer:
                    try:
                        person.remove(z)
                    except:
                        pass
    
                break
        score = []
        
                    
    else:
        return fruits[0]
            
#main environment
s = favFruit()
print("\nFav Fruit: ",s)