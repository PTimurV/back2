import numpy as np

my_set = {1,2,3,4,5,6,7,8,9}

with open('sudoku.txt') as file:
    
    data = []
    for rows in file:
        data.append(list(map(int, rows.split())))
data = np.array(data)

while (1!=0):
    a=0
    for i in range (9):
        for j in range (9):
            my_set1 = set()
            if data[i][j] == 0:
                a = a+1
                my_set1.update(data[i])
                my_set1.update(data[:, j])
                if (i<3 and j <3):
                    my_set1.update(data[:3,:3].flatten())
                elif (i<6 and j <3):
                    my_set1.update(data[3:6,:3].flatten())
                elif (i<9 and j <3):
                    my_set1.update(data[6:9,:3].flatten())

                elif (i<3 and j <6):
                    my_set1.update(data[:3,3:6].flatten())
                elif (i<6 and j <6):
                    my_set1.update(data[3:6,3:6].flatten())
                elif (i<9 and j <6):
                    my_set1.update(data[6:9,3:6].flatten())

                elif (i<3 and j <9):
                    my_set1.update(data[:3,6:9].flatten())
                elif (i<6 and j <9):
                    my_set1.update(data[3:6,6:9].flatten())
                elif (i<9 and j <9):
                    my_set1.update(data[6:9,6:9].flatten())
                
                my_set2=my_set-my_set1
                if(len(my_set2)==1):
                    data[i][j]=my_set2.pop()
    if(a==0):
        break


with open('sudoku_output.txt', 'w') as file:
    for row in data:
        file.write(' '.join(map(str, row)) + '\n')  
                
                

                

