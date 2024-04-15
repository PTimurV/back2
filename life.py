import numpy as np
with open('input.txt') as file:
    m = int(file.readline())
    data = []
    for rows in file: 
        data.append(list(map(int, rows.split())))
data = np.array(data)
n=len(data[1])

def close(i, j):
    sum = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            sum += data[(i + x) % n, (j + y) % n]
    return sum

for a in range(m-1):
    new_data = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if data[i,j]==0: 
                if(close(i,j))==3:
                        new_data[i,j]=1
                else: new_data[i,j] = data[i,j]
            else:
                if close(i,j)!=3 and close(i,j)!=2:
                        new_data[i,j]=0
                else: new_data[i,j] = data[i,j]
    data=new_data


with open('output.txt', 'w') as file:
    for row in data:
        file.write(' '.join(map(str, row)) + '\n')  

                
                
    
           


            



                
                

                

