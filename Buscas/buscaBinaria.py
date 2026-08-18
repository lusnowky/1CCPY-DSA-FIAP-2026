# BUSCA BINARIA

def busca_binaria(lista, valor)
  inicio = 0
  fim = len(lista) - 1
  while inicio <= fim:
    meio = (inicio + fim) // 2
    if lista[meio] == valor:
      return meio
    elif lista[meio] < valor:
      inicio = meio + 1
    else:
      fim = meio - 1

  return - 1

numeros = [2, 8, 10, 16, 25, 28, 32, 43, 51, 55, 63]
posicao = busca_binaria(numeros, 10)
print(posicao)
      
