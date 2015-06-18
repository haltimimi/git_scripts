def partial_reverse(A,start,end):
    result = []
    partial = A[start:end]
    p_reverse = reversed(partial) 
    l1= A[:start]
    l2= A[end:]
    l3 = l1.extend(partial)
    result = l3.extend(l2)
    

    return result 

        
A = [ 'a', 'b', 'c', 'd', 'e', 'f' ]        
#getlist(A)
partial_reverse(A, 2 ,4)
