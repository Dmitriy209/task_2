
N=int(input('Введите число: '))
spiral=[[0]*N for i in range(N)]
k=0
st=1
spiral[n//2][n//2]=N*N
for v in range(n//2):

    for i in range(N-k):
        spiral[v][i+v]=st
        st+=1

    for i in range(N-1):
        spiral[i+1][N-1]=last_simbol
        last_simbol += 1

    for i in range(N):
        spiral[N-1][-i-1]=down
        down+=1

    for i in range(N-2):
        spiral[-i-2][0]=spiral[-i-1][0]+1


print(spiral)


