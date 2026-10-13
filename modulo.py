def criar_tabuleiro():
  return [ ['1', '2', '3'], 
           ['4', '5', '6'], 
           ['7', '8', '9'] ]

def mostrar_tabuleiro(tabuleiro):
  print('--'*20)
  for l in tabuleiro:
    print(' | '.join(l).center(40))
    print(f'{"-"*9}'.center(40))
  print('--'*20)

def receber_jogada(player):
  while True:
    try:
      posicao = int(input(f'Player "{player}" escolha uma posição (1~9): '))
      if 1 <= posicao <= 9:
        return str(posicao)
      print('Erro! posicao incorreta, digite apenas numeros entre 1 e 9')
    except:
      print('Erro! digite apenas numero')
def atualizar_tabuleiro(tabuleiro, player, posicao):
  for l in range(3):
    for c in range(3):
      if posicao == tabuleiro[l][c]:
        tabuleiro[l][c] = player
        return tabuleiro
  print('>>> Erro! Posição ja escolhida pelo oponente')
  return None
def verificar_vencedor(tabuleiro, player):
  for linha in tabuleiro: #verificar linha
    if all(posicao == player for posicao in linha):
      return True
  for coluna in range(3): # verificar coluna
    if all(tabuleiro[linha][coluna] == player for linha in range(3)):
      return True
  if all(tabuleiro[i][i] == player for i in range(3)): # diagonal principal
    return True
  if all(tabuleiro[i][2-i] == player for i in range(3)): # Diagonal Secundaria
    return True
  return False
def escolher_modo():
  print('''[ 1 ] Jogar com Amigo
[ 2 ] Jogar contra Maquina
[ 3 ] Sair''')
  while True:
    try:
      opc = int(input('Sua Opção: '))
    except:
      print('Erro! Digite um valor Numerico')
    else:
      if 1 <= opc <= 3:
        return opc
      print('Erro! Digite apenaa umas das Opções')

def jogada_maquina(tabuleiro, player):
    from random import randint as r
    while True:
        posicao = r(1, 9) # Posicao
        for l in range(3):
            for c in range(3):
                if str(posicao) == tabuleiro[l][c]: # Verificar se Posicao esta Disponivel
                  tabuleiro[l][c] = player
                  return tabuleiro