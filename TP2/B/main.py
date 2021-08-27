def ReadMatrix(n,m):
  matrix = [[0]*(m+1) for i in range(n+2)]
  for i in range(n+1):
    row = input().split()
    for j in range(m):
        matrix[i][j] = int(row[j])
  return matrix

def main():
  n, m = map(int, input().split()) #n Restricoes │ m Variaveis
  matrix = ReadMatrix(n,m)
  vetM = [0]*n
  for i in range(n):
    if matrix[i+1][-1]>0:
      continue
    colS = -1
    valS = -1
    valM = -1
    for j in range(m):
      if matrix[i+1][j]==1 and (valS == -1 or matrix[0][j]<valS):
        colS = j
        valS = matrix[0][j]
      if matrix[i+1][j]==1 and (valM == -1 or matrix[0][j]<valM):
        valM = matrix[0][j]
    for j in range(n):
      matrix[j+1][-1] += matrix[j+1][colS]
    for j in range(m):
      matrix[0][j] -= valM*matrix[i+1][j]
    matrix[-1][colS] = 1
    vetM[i] = valM

  for i in range(m):
    print(matrix[-1][i],end=" ")
  print()
  for i in range(n):
    print(vetM[i],end=" ")

if __name__ == "__main__":
    main()