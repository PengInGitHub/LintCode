def swapIntegers(p, index1, index2):
    if index1>=len(p) or index2>=len(p) or index1<=-len(p) or index2<=-len(p) :
        return
    p[index1], p[index2] = p[index2], p[index1]


def swapIntegers2(p, index1, index2):
    p[index1], p[index2] = p[index2], p[index1]
    
a = [1,3,4,2]
swapIntegers2(a,-1,2) 
print a

    	
