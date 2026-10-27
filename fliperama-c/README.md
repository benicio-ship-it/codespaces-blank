# Fliperama em C (MeuApp v3.0)

## O que é
É um jogo de fliperama em linguagem C com jogo adivinhação e cadastro de jogadores 
ele foi feito para a disciplina 2026-PCAP como evolução da versão em Python.

## Como compilar e rodar
gcc -Wall fliperama.c -o fliperama
./fliperama

## Arquivos
- fliperama.c: Código-fonte em C com o menu interativo, cadastro de jogadores, jogo de adivinhação e persistência de dados.
- jogadores.csv: Arquivo de texto que armazena os dados dos jogadores no formato "apelido quantidade_de_partidas".

## Python x C: o que mudou

| O que | No jogadores.py (linha) | No fliperama.c (linha) |
|---|---|---|
| guardar um jogador | jogadores.append(novo) (l. __) | strcpy(apelidos[qtd], novo); (l. 81) |
| comparar apelidos | == (l. __) | strcmp(...) == 0 (l. 56) |
| abrir sem arquivo | exists(ARQUIVO) (l. __) | fopen == NULL (l. 138) |

## O que o C me obrigou a decidir
Tive que gerenciar  o tamanho limite das strings e a capacidade máxima do vetor (`CAPACIDADE = 50`), enquanto no Python as listas e textos crescem dinamicamente.
Além disso, precisei controlar o consumo de entrada do `scanf` limpando o buffer em caso de digitação inválida.

## Autoavaliacao

| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git | Excelente | fliperama.c (l. 1-170) |
| 2. Cadastro: menu, funcoes e vetores | Excelente | fliperama.c (l. 63-84, l. 119-129) |
| 3. Jogo e partidas | Excelente | fliperama.c (l. 98-117) |
| 4. Persistencia | Excelente | fliperama.c (l. 131-157) |
| 5. Documentacao e comparacao | Excelente | README.md |