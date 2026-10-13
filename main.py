from modulo import *
from time import sleep as tp

def main():
    while True:
        tabuleiro = criar_tabuleiro()  # Reinicializa o tabuleiro
        print('-='*20)
        print('JOGO DA VELHA'.center(40))
        print('-='*20)
        print('Tabuleiro')
        mostrar_tabuleiro(tabuleiro)

        opc = escolher_modo()
        if opc == 1:  # Jogar com Amigo
            print('--'*20)
            print('-> Player 1: X')
            print('-> Player 2: O')
            print('--'*20)
            c = 0  # Reinicializa o contador
            while True:
                player = 'X'
                c += 1
                while True:
                    posicao = receber_jogada(player)
                    Tabuleiro = atualizar_tabuleiro(tabuleiro, player, posicao)
                    if Tabuleiro is None:
                        continue
                    break
                print('-='*20)
                print('Atualizando Jogada'.center(40))
                mostrar_tabuleiro(tabuleiro)
                if verificar_vencedor(tabuleiro, player):
                    print(f'Player {player} Venceu!')
                    break
                if c == 9:
                    print('O JOGO DEU EMPATE')
                    break

                tp(0.7) #tempo de raciocinio antes da vez do outro jogador    
                player = 'O' 
                while True:
                    posicao = receber_jogada(player)
                    Tabuleiro = atualizar_tabuleiro(tabuleiro, player, posicao)
                    if Tabuleiro == None:
                        continue
                    break
                c += 1
                print('-='*20)
                print('Atualizando Jogada'.center(40))
                mostrar_tabuleiro(tabuleiro)
                if verificar_vencedor(tabuleiro, player):
                    print(f'Player {player} Venceu!')
                    break

        elif opc == 2:  # Jogar contra Máquina
            print('--'*20)
            print('-> Player 1: X')
            print('-> Maquina : O')
            print('--'*20)
            c = 0
            while True:
                player = 'X'
                c += 1
                while True: #Valida a jogada do Player X
                    posicao = receber_jogada(player)
                    Tabuleiro = atualizar_tabuleiro(tabuleiro, player, posicao)
                    if Tabuleiro is None:
                        continue
                    break
                #Valida se ha um Ganhador    
                print('-='*20)
                print('Atualizando Jogada'.center(40))
                mostrar_tabuleiro(tabuleiro)
                if verificar_vencedor(tabuleiro, player):
                    print(f'Player {player} Venceu!')
                    break
                if c == 9:
                    print('O JOGO DEU EMPATE')
                    break 
   
                tp(0.7)
                player = 'O'
                print('Vez da Maquina Jogar')
                Tabuleiro = jogada_maquina(tabuleiro, player) # Jogada da Maquina
                
                c += 1
                print('-='*20)
                print('Atualizando Jogada'.center(40))
                mostrar_tabuleiro(tabuleiro)
                if verificar_vencedor(tabuleiro, player):
                    print(f'Player {player} Venceu!')
                    break 
                    
        else:
            print('Saindo...')
            break

        print('-='*20)
        print('FIM DE JOGO'.center(40))
        print('-='*20)

        # Pergunta se quer jogar de novo
        while True:
            opc = input('Jogar de Novo? (S/N): ').lower()[0]
            if opc in 'sn':
                if opc == 's':
                    break  # Reinicia o jogo
                elif opc == 'n':
                    print('--'*20)
                    print('Programa Encerrado'.center(40))
                    print('--'*20)
                    return  # Encerra o programa
            print('Erro! Digite apenas SIM ou NÃO')

main()