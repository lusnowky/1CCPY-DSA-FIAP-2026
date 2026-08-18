# Busca Linear

def busca_sequencial(lista, procurado):
  for i in range(len(lista)):
    if lista[i] == procurado:
      return i
  return -1

nome = ["Gabriela", "Lucas", "João", "Laura", "Caio", "Isabella"]
posicao = busca_sequencial(nome, "João")
print posicao
