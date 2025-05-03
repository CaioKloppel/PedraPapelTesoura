from random import choice
import os
from biblioteca import resultado

modo_jogo = "" 

while modo_jogo not in ("1x1", "ia"):
    modo_jogo = input("Qual modo de jogo você quer jogar (1x1 ou IA): ").lower().strip() 
    if modo_jogo not in ("1x1", "ia"):
        print("Você digitou errado, digite novamente!")

stop = "" 
jogadas = ("pedra", "papel", "tesoura") 
rodada = 1 
nome_jogador1 = "" 
nome_jogador2 = ""

while nome_jogador1 == "" or not any(char.isalpha() for char in nome_jogador1): 
    nome_jogador1 = input("Qual seu nome: ").title().strip() if modo_jogo == "ia" else input("Qual seu nome (jogador 1): ").title().strip() 
    if nome_jogador1 == "" or not any(char.isalpha() for char in nome_jogador1):
        print("""É necessário que o jogador tenha um nome para continuar.
Seu nome deve conter ao menos uma letra.""")
        
if modo_jogo == "1x1": 
    while nome_jogador2 == "" or nome_jogador1 == nome_jogador2 or not any(char.isalpha() for char in nome_jogador2):
        nome_jogador2 = input("Qual seu nome (jogador 2): ").title().strip()
        if nome_jogador1 == "" or nome_jogador2 == "" or nome_jogador1 == nome_jogador2 or not any(char.isalpha() for char in nome_jogador2):
            print("É necessário que o segundo jogador tenha um nome, e ele deve ter ao mínimo uma letra e um caratere diferente do jogador 1.")
        
lista_resultados = {nome_jogador1: 0, nome_jogador2: 0, "IA": 0, "empate": 0} 

while stop != "parar":
    print(f"RODADA {rodada}\n")
    escolha_ia = choice(jogadas) 
    escolha_jogador1 = "" 
    escolha_jogador2 = None 
    while escolha_jogador1 not in jogadas: 
        escolha_jogador1 = input(f"Qual sua jogada {nome_jogador1}(pedra, papel ou tesoura): ").lower().strip()
        if escolha_jogador1 not in jogadas:
            print("Você digitou errado, digite novamente.")
    os.system('cls' if os.name == 'nt' else 'clear') 
    if modo_jogo == "1x1": 
        while escolha_jogador2 not in jogadas:
            escolha_jogador2 = input(f"Qual sua jogada {nome_jogador2}(pedra, papel ou tesoura): ").lower().strip()
            if escolha_jogador2 not in jogadas:
                print("Você digitou errado, digite novamente.")
        os.system('cls' if os.name == 'nt' else 'clear')
    print(f"RODADA {rodada}\n")
    oponente = resultado(nome_jogador1, nome_jogador2, escolha_ia, escolha_jogador1, escolha_jogador2, lista_resultados)
    rodada += 1 

    stop = ""
        
    while stop not in ("parar", "continuar"): 
        stop = input("Você deseja CONTINUAR ou PARAR: ").lower().strip()
        if stop not in ("parar", "continuar"):
            print("Você deve escolher uma das opções. (CONTINUAR, PARAR)!")
    
    os.system('cls' if os.name == 'nt' else 'clear')

print(f"""
RESULTADOS!
        
Vitórias {nome_jogador1}: {lista_resultados[nome_jogador1]}
Empates: {lista_resultados["empate"]}
Vitórias {oponente}: {lista_resultados[oponente]}""") 