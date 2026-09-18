===================================================================
ARQUIVO   : README-meujogo.md
Autor     : Benício Cordeiro
Data      : 2026.09.18
===================================================================

## Objetivo do jogo
O objetivo do caca a toupeira é acertar 5 toupeiras seguidas. 
Quando o jogo começa, vão aparecendo uns buracos vazios na tela e você não pode apertar nada nessa hora, se apertar qualquer tecla antes da hora você perde.

Quando a toupeira aparecer, você tem que apertar ENTER no tempo de 0.8 segundos, se demorar mais que isso voce perde.

O jogo tem um sistema pra limpar o teclado, assim ninguém consegue trapacear se ficar apertando enter sem parar antes da toupeira aparecer.

## Tabela de Reúso dos Módulos

* ler_texto() (modulos.py): Usada no jogar_toupeira() para pedir o apelido do jogador.
* titulo()    ( telas.py ): Usada para mostrar o título do jogo.
* linha()     ( telas.py ): Usada para colocar as linhas de separação ao terminar o jogo.