# Q1
def number_of_above_average(n,m,A):
    count = 0
    for i in range(n):
        count += sum(A[i])
    average  = count / (n*m)


    count2 =0
    for i in range(n):
        for j in range(m):
            if A[i][j] > average:
                count2 +=1
    return count2

print(number_of_above_average(2,2,[[1,1],[2,4]]))
print(number_of_above_average(2,3,[[1,2,3],[4,5,6]]))
