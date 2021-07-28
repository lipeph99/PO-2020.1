# -*- coding: utf-8 -*-

def readMatrix(n,m):
  matrix = [[0]*(m+2*n+1) for i in range(n+1)]

  row = input().split()
  for i in range(len(row)):
      matrix[0][i+n] = int(row[i]) * -1

  for i in range(n):
    row = input().split()
    for j in range(len(row)-1):
        matrix[i+1][j+n] = int(row[j])
    matrix[i+1][-1]=int(row[-1])

  for i in range(n):
    for j in range(n):
      aux=0
      if (j==i):
        aux=1
      matrix[i+1][m+n+j]=aux
      matrix[i+1][j]=aux
  return matrix

def pivot(matrix,n,m):
  colP = -1

  #Acha primeira coluna com c negativo para ser pivoteada
  for i in range(n+m):
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
  for i in range(n):
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
  for i in range(m+2*n+1):
    matrix[linP+1][i] = matrix[linP+1][i]/valP

  #Pivoteia a linha pra cima e pra baixo
  for i in range(n+1):
    if ((matrix[i][colP+n]>0.0001 or matrix[i][colP+n]<-0.0001) and i-1!=linP):
      ratP = matrix[i][colP+n]
      for j in range(m+2*n+1):
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

def auxMatrix(matrix,n,m):
  matrixAux = [[0]*(m+3*n+1) for i in range(n+1)]
  for i in range (n+1):
    for j in range (m+2*n):
      if (i==0):
        matrixAux[i][j] = 0
      else:
        if (matrix[i][-1]<0):
          matrixAux[i][j] = -matrix[i][j]
        else:
          matrixAux[i][j] = matrix[i][j]
        matrixAux[0][j] -= matrixAux[i][j]
  matrixAux[0][-1] = 0
  for i in range (n+1):
    for j in range (n):
      if (i==0):
        matrixAux[i][m+n+n+j] = 0
      else:
        if (i-1 == j):
          matrixAux[i][m+n+n+j] = 1
    matrixAux[i][-1] = matrix[i][-1]
    if (matrix[i][-1]<0):
      matrixAux[i][-1] = -matrix[i][-1]
    matrixAux[0][-1] -= matrixAux[i][-1]
  #for i in range(n+1):
    #print(' '.join('{:+.2f}'.format(f) for f in matrixAux[i]))

  while (checkC(matrixAux,n,m) == False):
    aa = pivotAux(matrixAux,n,m)
    #print(aa)
    #for i in range(n+1):
      #print(' '.join('{:+.2f}'.format(f) for f in matrixAux[i]))
  #print("----")
  if(matrixAux[0][-1]>-0.0001 and matrixAux[0][-1]<0.0001):
    for i in range (n+1):
      for j in range (m+2*n):
        if (i==0):
          if (j>n):
            matrix[i][j] += matrixAux[i][j]
        else:
          matrix[i][j] = matrixAux[i][j]
      matrix[i][-1] = matrixAux[i][-1]
    return True
  else:
    for i in range (n):
      matrix[0][i]=matrixAux[0][i]
    return False

def pivotAux(matrix,n,m):
  colP = -1

  #Acha primeira coluna com c negativo para ser pivoteada
  for i in range(n+m+n):
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
  for i in range(n):
    if (matrix[i+1][n+colP]>0.0001): #and matrix[i+1][n+colP]*matrix[i+1][-1]>=0):
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
  for i in range(m+3*n+1):
    matrix[linP+1][i] = matrix[linP+1][i]/valP

  #Pivoteia a linha pra cima e pra baixo
  for i in range(n+1):
    if ((matrix[i][colP+n]>0.0001 or matrix[i][colP+n]<-0.0001) and i-1!=linP):
      ratP = matrix[i][colP+n]
      for j in range(m+2*n+1+n):
        matrix[i][j] = matrix[i][j] - ratP*matrix[linP+1][j]

  return True,colP

def main():
  #Ler input e printar matriz
  n, m = map(int, input().split()) #n Restricoes │ m Variaveis
  matrix = readMatrix(n,m)
  #for i in range(n+1):
    #print(matrix[i])
  #print()

  auxNeed = True
  if checkB(matrix,n,m)==False:
    auxNeed = auxMatrix(matrix,n,m)
  if (auxNeed == True):
    while (checkC(matrix,n,m) == False):
      #time.sleep(1)
      limit = pivot(matrix,n,m)
      #print(limit)
      #for i in range(n+1):
        #print(' '.join('{:+.2f}'.format(f) for f in matrix[i]))
      if (limit[0]==False):
        print ("ilimitada")
        for i in range(m):
          if (i==limit[1]):
            print ("+0.00000",end=" ")
          else:
            oneCount = 0
            zeroCount = 0
            line = -1
            for j in range (n):
              if (matrix[j+1][n+i]>-0.0001 and matrix[j+1][n+i]<0.0001):
                zeroCount += 1
              elif(matrix[j+1][n+i]>0.9999 and matrix[j+1][n+i]<1.0001):
                oneCount += 1
                line = j
            if (oneCount == 1 and oneCount+zeroCount == n):
              print('{:+.5f}'.format(matrix[line+1][-1]),end=" ")
            else:
              print("+0.00000",end=" ")
        print()
        for i in range(m):
          if (i==limit[1]):
            print ("+1.00000",end=" ")
          else:
            oneCount = 0
            zeroCount = 0
            line = -1
            for j in range (n):
              if (matrix[j+1][n+i]>-0.0001 and matrix[j+1][n+i]<0.0001):
                zeroCount += 1
              elif(matrix[j+1][n+i]>0.9999 and matrix[j+1][n+i]<1.0001):
                oneCount += 1
                line = j
            if (oneCount == 1 and oneCount+zeroCount == n):
              print('{:+.5f}'.format(-matrix[line+1][n+limit[1]]),end=" ")
            else:
              print("+0.00000",end=" ")
        break
  else:
    print("inviavel")
    print(' '.join('{:+.5f}'.format(matrix[0][i]) for i in range(n)))
  if (auxNeed==True and limit[0]==True):
    print("otima")
    print('{:+.5f}'.format(matrix[0][-1]))
    for i in range(m):
      if (matrix[0][n+i]>0.0001):
        print("+0.00000",end=" ")
      else:
        oneCount = 0
        zeroCount = 0
        line = -1
        for j in range (n):
          if (matrix[j+1][n+i]>-0.0001 and matrix[j+1][n+i]<0.0001):
            zeroCount += 1
          elif(matrix[j+1][n+i]>0.9999 and matrix[j+1][n+i]<1.0001):
            oneCount += 1
            line = j
        if (oneCount == 1 and oneCount+zeroCount == n):
          print('{:+.5f}'.format(matrix[line+1][-1]),end=" ")
        else:
          print("+0.00000",end=" ")
    print()
    print(' '.join('{:+.5f}'.format(matrix[0][i]) for i in range(n)))
  return

if __name__ == "__main__":
    main()