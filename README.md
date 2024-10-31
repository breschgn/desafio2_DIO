# Calculadora de Partida Rankeada

Este projeto consiste em um script Python que calcula o nível de um jogador com base na quantidade de vitórias e derrotas informadas pelo usuário. Os níveis variam de "Ferro" até "Imortal", dependendo da quantidade de vitórias.

## Funcionalidades

- Solicita ao usuário a quantidade de vitórias e derrotas.
- Calcula o saldo entre vitórias e derrotas.
- Retorna um nível de classificação com base no número de vitórias.

## Observação

Particularmente eu eu teria feito o cálculo mais aprimorado, considerando uma proporcionalidade mais complexa entre vitórias e derrotas (perder menos, vencer mais). Dessa forma, seria mais preciso ao definir se um herói é, de fato, considerado "Lendário", "Diamante", "Ouro", entre outros, considerando não só o número absoluto de vitórias, mas também uma relação proporcional que avalia o desempenho do jogador de forma mais justa.

## Exemplo de Uso

```python
Informe a quantidade de vitórias: 40
Informe a quantidade de derrotas: 10
O herói tem saldo de 30 e está no nível de Prata
