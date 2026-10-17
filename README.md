# Controle de Níveis de Água

Sistema simples de monitoramento de um reservatório de água, executado no terminal. O programa exibe mensagens de alerta com cores diferentes, de acordo com o nível de água do reservatório.

## Funcionalidades

- Armazena os cinco níveis do reservatório em uma lista
- Define a cor da mensagem de acordo com o nível, por meio de uma função
- Exibe a situação do reservatório no terminal com a cor correspondente
- Restaura o estilo padrão do terminal após a exibição
- Simula o monitoramento com valores definidos no código (sem entrada de dados)

## Níveis e cores

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## Tecnologias

- Python 3
- Biblioteca [colorama](https://pypi.org/project/colorama/)

## Como executar

1. Clone ou baixe este projeto.
2. Instale a biblioteca colorama:

   ```
   pip install colorama
   ```

3. Execute o programa:

   ```
   python app.py
   ```

## Exemplo de saída

```
=== Monitoramento do Reservatório ===

Nível 1 - Muito baixo (Crítico)
Nível 2 - Baixo
Nível 3 - Médio
Nível 4 - Alto
Nível 5 - Muito alto (ALERTA)
```

Cada linha aparece no terminal com a cor indicada na tabela acima.

## Estrutura do código

- `niveis`: lista com as mensagens de cada nível, do mais baixo ao mais alto
- `definir_cor(nivel)`: recebe o nível e retorna a cor correspondente do colorama
- `exibir_situacao(nivel)`: busca a mensagem na lista e a imprime com a cor definida
- `Style.RESET_ALL`: devolve o terminal ao estilo padrão