from random import randint

def createMatrix(fila, col, a, b):
    if fila <= 0 or col <= 0:
        print("Deve ter pelo menos uma fila")
        matriz = [None]
    else:
        matriz = [None] * fila
        for i in range(fila):
            matriz[i] = [None] * col
        for i in range(fila):
            for j in range(col):
                matriz[i][j] = randint(a, b)
    return matriz

def printMatrix(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            elemento_formatado = "{:.2f}".format(matriz[i][j])
            # Espaço adicional para alinhar os elementos corretamente
            elemento_formatado = elemento_formatado.rjust(7)
            print(elemento_formatado, end="   ")
            if j == len(matriz[i]) - 2:
                print("|", end="   ")
        print()   


def doOne(matriz, piv, a, col):
    if a != 0:
        for j in range(col):
            matriz[piv][j] = matriz[piv][j] / a
    else:
        print("Não pode fazer divisão por zero")

def doZero(matriz, piv, fila, col):
    for i in range(fila):
        if i != piv:
            b = matriz[i][piv]
            for j in range(col):
                matriz[i][j] = matriz[i][j] - b * matriz[piv][j]

def testMatriz(matriz, fila, col):
    for i in range(fila):
        if matriz[i][i] == 0:
            return False
    return True

def getGaussJordanMatrix(matriz, fila, col, debug):
    for i in range(fila):
        a = matriz[i][i]
        doOne(matriz, i, a, col)
        doZero(matriz, i, fila, col)
        if debug == 1:
            print("Cria pivor, zero em cima e embaixo")
            printMatrix(matriz)
def calculateSolutions(matriz, fila):
    solucoes = []
    for i in range(fila):
        solucao = matriz[i][-1]  # O último elemento de cada linha
        solucoes.append(solucao)
    return solucoes

def main():
    fila = 4
    col = fila + 1
    a = -9
    b = 9

    matriz = [[3,-2, 1, 4, 10],
    [2, 3, - 2, -1 , 5],
    [4, - 1, 2, 3, 3],
    [1, 2, - 3, 2, 8]]

    print("Matriz original")
    printMatrix(matriz)

    isCandidateMatrix = testMatriz(matriz, fila, col)

    if isCandidateMatrix:
        getGaussJordanMatrix(matriz, fila, col, 1)

        print("Matriz final")
        printMatrix(matriz)
        print("\n");
        print("Solução:")
        solucoes = calculateSolutions(matriz, fila)
        for i, solucao in enumerate(solucoes):
            print(f"x{i+1} = {solucao:.2f}")
        print("\n");
    else:
        print("Não é possível aplicar o método Gauss-Jordan nesta matriz")
    

if __name__ == "__main__":
    main()
