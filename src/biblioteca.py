def resultado(nome_jogador1, nome_jogador2, escolha_ia, escolha_jogador1, escolha_jogador2, lista_resultados):
    jogada = {"pedra": "tesoura", "tesoura": "papel", "papel": "pedra"} 
    if escolha_jogador2 == None: 
        escolha_oponente = escolha_ia
        oponente = "IA"
    else: 
        escolha_oponente = escolha_jogador2
        oponente = nome_jogador2    

    if jogada[escolha_jogador1] == escolha_oponente: 
        print(f"{nome_jogador1} venceu a rodada!")
        print(f"Escolha {nome_jogador1}: {escolha_jogador1}")
        print(f"Escolha {oponente}: {escolha_oponente}") 
        lista_resultados[nome_jogador1] += 1 
    elif escolha_jogador1 == escolha_oponente: 
        print(f"Escolha {nome_jogador1}: {escolha_jogador1}")
        print(f"Escolha {oponente}: {escolha_oponente}")
        print("Empate!")
        lista_resultados["empate"] += 1 
    else: 
        print(f"{oponente} venceu a rodada!" )
        print(f"Escolha {nome_jogador1}: {escolha_jogador1}")
        print(f"Escolha {oponente}: {escolha_oponente}")
        lista_resultados[oponente] += 1 

    return oponente 