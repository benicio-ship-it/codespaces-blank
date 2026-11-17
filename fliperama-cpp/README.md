# Fliperama em C++ (MeuApp v4.0)

## O que é
Um sistema de fliperama no terminal desenvolvido para a disciplina 2026-PCAP, que permite cadastrar jogadores, rodar o jogo "Adivinhe o Número" contabilizando partidas e salvar o progresso automaticamente em arquivo. O projeto é a evolução (v4.0) do antigo programa em C, agora refatorado para C++ usando `vector` e `string` dinâmicos.

## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivos
- fliperama.cpp : Código-fonte principal em C++ contendo o menu interativo
- jogadores.csv : Arquivo de texto onde a primeira coluna guarda o apelido e a segunda guarda o total de partidas jogadas.

## C x C++: o que mudou

| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |

| guardar um jogador    | `strcpy(apelidos[qtd], novo)` (74)     | `apelidos.push_back(novo)`                      (87) |
| comparar apelidos     | `strcmp(...) == 0`            (49)     | `apelidos[i] == procurado`                      (54) |
| a funcao que cadastra | `int cadastrar(..., int qtd)` (56)     | `void cadastrar(vector<string> &apelidos, ...)` (81) |

## O que o C++ decidiu por mim

Em C, eu precisava definir um tamanho máximo fixo para o array de jogadores e controlar manualmente a variável `qtd` a cada inserção; em C++, o `std::vector` gerencia a alocação de memória e cresce dinamicamente sozinho através do `.push_back()`. Além disso, o tipo `std::string` e a biblioteca `fstream` eliminaram a necessidade de manipular ponteiros de `char`, tamanhos de buffer e chamadas manuais de `fclose()` ao final do escopo das funções.

## Autoavaliacao

| Criterio | Status | Prova (arquivo e linha) |

| Menu com validacao             | Concluido | `fliperama.cpp` (28-40) |
| Cadastro dinamico com `vector` | Concluido | `fliperama.cpp` (81-90) |
| Contagem de partidas no jogo   | Concluido | `fliperama.cpp` (128)   |
| Salvar e carregar em arquivo   | Concluido | `fliperama.cpp` (60-79) |