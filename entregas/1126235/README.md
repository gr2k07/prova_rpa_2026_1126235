# 📐 Pasta _MODELO — Molde de Entrega (contrato)

> **Esta pasta NÃO é uma entrega e é ignorada pelo CI e pelo flake8.**

Aqui estão os **contratos** de cada questão: as assinaturas, docstrings e o que
cada arquivo deve fazer — **sem a lógica implementada**. Cabe a você escrever o
corpo de cada rotina.

## Como usar
1. Crie a sua pasta de RA: `entregas/SEU_RA/`.
2. Copie os arquivos deste molde para lá.
3. **Implemente** cada função/rotina. Cada arquivo tem um
   `raise NotImplementedError` que você deve remover ao terminar.
4. Rode localmente antes de entregar. Enquanto houver `NotImplementedError`,
   o arquivo falha de propósito — esse é o sinal de que ainda falta implementar.

## Por que só o contrato?
O objetivo da prova é você **entender e escrever** a solução, não corrigir um
vermelho que a IDE já apontou. O molde te dá a estrutura esperada; o raciocínio
e o código são seus.

## Arquivos
- `config_conexao.py` — Questão 1
- `monitor_sensores.py` — Questão 2
- `mod_estoque.py` + `main.py` — Questão 3
- `importador_notas.py` + `notas.csv` — Questão 4
- `AVALIACAO_PROCESSO.md` — Questão 5 (ficha PDD)
