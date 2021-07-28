# TP1 PO-2020.1
 ## O Trabalho
  O Objetivo do trabalho prático é resolver programações lineares e encontrar os certificados que comprovam o resultado.
  Todas as programações lineares serão lidar a partir do input e estarão no seguinte formato:
  max c^t x
  sujeita a Ax ≤ b
  x ≥ 0
  A especificação completa do problema está no arquivo [TP1_PO.pdf](https://github.com/lipeph99/PO-2020.1/tree/main/TP1/TP1_PO.pdf)

 ## Implementação
  O trabalho foi desenvolvido em python e nenhuma biblioteca externa foi utilizada.

 ## Detalhes
  Para resolver o problema a matriz de entrada foi expandida para ter um registro de operação e variáveis de folga.
  Quando nescessário também foi usada uma matriz auxiliar para definir a viabilidade do problema.
  O código começa checando se o problema é viável e a partir de uma base viável começa a procurar pelo ótimo até chegar em um resultado.
  Sendo a PL ótima, ilimitada ou inviável é impresso o resultado e os certificados de acordo com o que foi pedido na especificação.

 ## Testes
  O programa foi testado com os casos de testes fornecidos pelo professor que se encontram tanto na especificação como na pasta [Tests](https://github.com/lipeph99/PO-2020.1/tree/main/TP1/Tests)
  Para todos os casos de teste fornecidos o resultado foi igual ao fornecido ou uma solução equivalente com uma base de colunas diferente, mas que não altera a corretude do programa.


 Philippe Santos Silva
 [lipeph99](https://github.com/lipeph99)
