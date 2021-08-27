def readMatrix(n,m):
  matrix = [[0]*(n+2*m+1) for i in range(n-1+m)]

  for i in range(n+1):
    row = input().split()
    for j in range(len(row)):
        if (i==0):
          matrix[n-1+j][-1] = int(row[j])
        elif (i==1):
          matrix[0][n+j] = int(row[j])
        elif (i<n):
          matrix[i-1][n+j] = int(row[j])

  for i in range(m):
    matrix[n-1+i][n+i]=1
    matrix[n-1+i][n+m+i]=1

  return matrix

def pivot(matrix,n,m):
  colP = -1

  #Acha primeira coluna com c negativo para ser pivoteada
  for i in range(2*m):
    if (matrix[0][n+i]<-0.0001):
      if (colP==-1):
        colP = i
      elif (matrix[0][n+i]<matrix[0][n+colP]):
        colP = i

  if (colP == -1):
    return False,colP

  #Acha a coluna com min b/a && a>0 para pivotear
  linP = -1;
  minP = 0;
  for i in range(n-2+m):
    if (matrix[i+1][n+colP]>0.0001):
      if (linP == -1):
        linP = i
        minP = matrix[i+1][-1]/matrix[i+1][n+colP]
      elif (matrix[i+1][-1]/matrix[i+1][n+colP] < minP):
        linP = i
        minP = matrix[i+1][-1]/matrix[i+1][n+colP]
  
  if (linP == -1):
    return False,colP
  #Transforma a linha para o pivot valer 1
  valP = matrix[linP+1][colP+n]
  for i in range(n+2*m+1):
    matrix[linP+1][i] = matrix[linP+1][i]/valP

  #Pivoteia a linha pra cima e pra baixo
  for i in range(n-1+m):
    if ((matrix[i][colP+n]>0.0001 or matrix[i][colP+n]<-0.0001) and i-1!=linP):
      ratP = matrix[i][colP+n]
      for j in range(n+2*m+1):
        matrix[i][j] = matrix[i][j] - ratP*matrix[linP+1][j]

  return True,colP

def checkB(matrix,n,m):
  for i in range(len(matrix)-1):
    if (matrix[i+1][-1]<-0.0001):
      return False
  return True

def checkC(matrix,n,m):
  for i in range(len(matrix[0])-n-1):
    if (matrix[0][n+i]<-0.0001):
      return False
  return True

def main():
  #Ler input e printar matriz
  import copy

  n, m = map(int, input().split()) #n Restricoes │ m Variaveis
  matrix = readMatrix(n,m)
  auxM = copy.deepcopy(matrix)

  while (checkC(matrix,n,m) == False):
    pivot(matrix,n,m)

  print(round(matrix[0][-1]))
  fluxo=[]
  for j in range(m):
    aux = 0
    linP = -1
    for i in range(n-2+m):
      if (round(matrix[i+1][j+n])!=0):
        aux += 1
        if (aux>1):
          break
        if (round(matrix[i+1][j+n])==1):
          linP = i
    if (aux!=1):
      fluxo.append(0)
      print ("0",end=" ")
    else:
      fluxo.append(round(matrix[linP+1][-1]))
      print(round(matrix[linP+1][-1]),end=" ")
  print()

  corte = [0]*n
  corte[0]=1
  cut = []
  cut.append(0)
  while len(cut):
    for i in range(m):
      if auxM[cut[0]][i+n]==-1:
        for j in range(n-1):
          if auxM[j][i+n]==1 and corte[j]==0:
            if fluxo[i]==auxM[n+i-1][-1]:
              break
            corte[j]=1
            cut.append(j)
    corte[cut[0]]=-1
    cut.pop(0)
  for i in range(len(corte)):
    print (-corte[i],end=" ")
  print()

if __name__ == "__main__":
    main()