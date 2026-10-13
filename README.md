# Jogo da Velha em Python

Um projeto clássico de **Jogo da Velha (Tic-Tac-Toe)** desenvolvido em Python, executado diretamente pelo terminal/console. Permite partidas locais para dois jogadores ou contra uma inteligência artificial simples.

---

## Funcionalidades

- **Modo de Jogo 1:** Jogar com um amigo (Dois jogadores no mesmo computador: Player 1 `X` contra Player 2 `O`).
- **Modo de Jogo 2:** Jogar contra a máquina (O jogador `X` enfrenta jogadas aleatórias automáticas da máquina `O`).
- **Validação de Jogadas:** O sistema verifica se a posição escolhida (1 a 9) é válida, se está dentro do tabuleiro e se já não foi ocupada.
- **Detecção Automática:** Identifica automaticamente linhas, colunas ou diagonais vencedoras, além de detectar empates (velha).
- **Opção de Reinício:** Permite reiniciar uma nova partida após o término do jogo ou encerrar a execução.

---

## Tecnologias Utilizadas

- **Python 3.x**
- Biblioteca padrão `random` (utilizada para gerar as jogadas da máquina).

---

## Estrutura do Projeto

O projeto está dividido em dois arquivos principais:

```text
├── tabuleiro.py         # Arquivo principal que gerencia o fluxo do jogo e o loop das partidas
└── funcoes_tabuleiro.py # Contém as funções lógicas, validações, renderização e regras do jogo
```

---

## Pré-requisitos

Para executar este projeto, você precisa ter instalado em sua máquina:
- **Python 3** (versão recomendada: 3.x)

---

## Como Executar

1. Certifique-se de que os arquivos `tabuleiro.py` e `funcoes_tabuleiro.py` estão na mesma pasta.
2. Abra o terminal (ou prompt de comando) na pasta onde os arquivos estão salvos.
3. Execute o comando abaixo:

```bash
python tabuleiro.py
```

---

## Exemplo de Uso

Ao iniciar o programa, o menu principal será exibido:

```text
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
             JOGO DA VELHA              
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Tabuleiro
----------------------------------------
                 1 | 2 | 3                
             ---------
                 4 | 5 | 6                
             ---------
                 7 | 8 | 9                
----------------------------------------
[ 1 ] Jogar com Amigo
[ 2 ] Jogar contra Maquina
[ 3 ] Sair
Sua Opção: 
```

Basta digitar o número correspondente à opção desejada e seguir as instruções na tela escolhendo as posições de `1` a `9`.