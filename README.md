# Jogo Pedra, Papel, Tesoura ✊✋✌️

Este é um jogo simples de **Pedra, Papel e Tesoura**, jogável no terminal, com duas opções de modo:

- **1x1**: Dois jogadores humanos se enfrentam.
- **IA**: Um jogador humano joga contra o computador.

## Como jogar

Execute o jogo diretamente pelo terminal ou utilize o arquivo executável localizado na pasta `dist`.

### Executando pelo terminal (modo desenvolvedor)

1. Certifique-se de ter o Python instalado (versão 3.6 ou superior).
2. No terminal, execute:

```bash
python main.py
```

### Executando o arquivo `.exe`

Se você estiver em um sistema Windows, é possível rodar o jogo sem precisar instalar o Python.

- Navegue até a pasta `dist` e execute o arquivo:

```
dist/pedra_papel_tesoura.exe
```

## Estrutura do Projeto

```
.
├── biblioteca.py                # Funções auxiliares do jogo (lógica de vitória, empate etc.)
├── main_otimizado.py            # Código principal do jogo
├── dist/
│   └── pedra_papel_tesoura.exe  # Arquivo executável do jogo
```

## Regras

- Pedra ganha da Tesoura
- Tesoura ganha do Papel
- Papel ganha da Pedra
- Jogadas iguais resultam em empate

## Créditos

Desenvolvido como um projeto de prática de Python.

---

Divirta-se jogando!