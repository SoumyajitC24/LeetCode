def matrix_dot_vector(a:list[list[int|float]] , b:list[int|float])-> list[int|float]:
  #a -> input
  #b -> multiplier
  
  c = [] #Output list
  print(len(a[0]))
  for a_i in range(len(a)):
    sumVal = 0 #Sum of each list in a * b
    if (len(a[a_i]) != len(b)): #Dot priduct not possible, return -1
     return -1
    for b_i in range(len(b)):
     sumVal += (a[a_i][b_i] * b[b_i])
    c.append(sumVal)
    print(c)
        
  return c
    
    
print(matrix_dot_vector([[1,2,3],[2,4,5],[6,8,9]],[1,2,3]))
