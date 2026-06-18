## Data: 18/06/2026
## Jogo: Pedra-Papel-Tesoura
## Disciplina: PCAP

# Como jogar:

O jogador joga uma partida de 5 rodadas contra uma IA

O jogador escolhe entre pedra, papel ou tesoura;
A máquina faz uma escolha;
O vencedor é escolhido pelas regras;

# Regras do Jogo:

Pedra vence Tesoura;
Tesoura vence Papel;
Papel vence Pedra;
Escolhas iguais dão empate.

# Pilares e Conceitos Utilizados

Funções
ultiliza a função resultado() para organizar a lógica no jogo.

Estruturas Condicionais
O if, elif e else para saber o vencedor de cada rodada.

Laços de Repetição
Uso do for para controlar a quantidade de rodadas.

Listas
Armazenamento das opções válidas:

opcoes = ["pedra", "papel", "tesoura"]

Random
Usa o random para fazer escolhas aleatórias da máquina:

random.choice(opcoes)

Validação
valida as respostas do jogador para impedir entradas inválidas.

Variáveis
Controla o placar através das variáveis:
pontos_jogador
pontos_maquina

# Parte criada por eu mesma

Criei uma opção para jogar novamente usando comando while baseado em uma pergunta de sim ou não.

## 🎯 Autoavaliação
Conceito pretendido: [B]

Justificativa (ppt.py linhas 11-15 e 42-44):
O jogo funciona ............: ppt.py, linha 9 a 53
Trabalho com texto .........: ppt.py, linha 34(.lower().strip())
Documentação e Git .........: README.md criado e commits realizados no GitHub
Extensão/originalidade .....: ppt.py, linhas 24 a 26 Adaptação para ter opção jogar novamente

## Autor: Benício Cordeiro