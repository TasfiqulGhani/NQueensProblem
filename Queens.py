
#TasfiqulGhani 1410112042
#Number of queens
print ("Enter No Of Queens")
N = int(input())

#here i am creating a board for N it will assign number dynamically .

myChessBoard = [[0] * N for _ in range(N)]

def is_attacking(i, j):
    #here i am checking the row
    for k in range(0,N):
        if myChessBoard[i][k]==1 or myChessBoard[k][j]==1:
            return True
    #here i am checking whether there is qween in the diagonal or not
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if myChessBoard[k][l]==1:
                    return True
    return False

def operation(n):

    if n==0:
        print("Hahaah very easy solution = 0")
        return True
    for i in range(0,N):
        for j in range(0,N):

            if (not(is_attacking(i, j))) and (myChessBoard[i][j] != 1):
                myChessBoard[i][j] = 1
                #now checking if we can add other here in same arrangement
                if operation(n - 1)==True:
                    return True
                myChessBoard[i][j] = 0

    return False

operation(N)
for i in myChessBoard:
    print (i)