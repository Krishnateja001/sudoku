sudo_map = [[0,0,0,0,0,4,0,9,0],[8,0,2,9,7,0,0,0,0],[9,0,1,2,0,0,3,0,0],
            [0,0,0,0,4,9,1,5,7],[0,1,3,0,5,0,9,2,0],[5,7,9,1,2,0,0,0,0],
            [0,0,7,0,0,2,6,0,3],
            [0,0,0,0,3,8,2,0,5],
            [0,2,0,5,0,0,0,0,0]]
#read row
#read column
#read box

def solve(row,column,number):
    for i in range(0,9):
        if number==sudo_map[row][i]:
            return False
    for j in range(0,9):
        if number==sudo_map[j][column]:
            return False
    val1=(row//3) * 3
    val2=(column//3) * 3
    
    for i in range(0,3):
        for j in range(0,3):
            if sudo_map[i+val1][j+val2] == number:
                return False


def main():
    for i in range(0,9):
        for j in range(0,9):
            if sudo_map[i][j] == 0:
                for num in range(1,10):
                    if solve(i,j,num):
                        sudo_map[i][j] = num
                        solve(i,j,num)
                        sudo_map[i][j] = 0 #did not understood

test()