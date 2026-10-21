
import csv
import random
from pathlib import Path
from datetime import datetime

PASTA = Path(__file__).resolve().parent

# Modelos de respostas para combinar e variar.
INICIOS = [
    "Na minha opinião,",
    "Eu considero que",
    "Acredito que",
    "Pelo que entendi,",
    "Pensando melhor,",
    "Na prática,",
    "De modo geral,",
    "Analisando a situação,",
    "Pelo meu ponto de vista,",
    "Considerando o contexto,"
]

ASSUNTOS = [
    "essa proposta",
    "essa experiência",
    "essa ideia",
    "essa atividade",
    "esse resultado",
    "essa solução",
    "esse tema",
    "essa iniciativa",
    "essa possibilidade",
    "esse processo"
]

COMPLEMENTOS = [
    "pode trazer bons resultados.",
    "merece ser analisado com atenção.",
    "é uma oportunidade de aprender.",
    "pode ser melhorado com planejamento.",
    "tem pontos positivos e aspectos a melhorar.",
    "depende dos objetivos e das necessidades.",
    "pode contribuir para novas ideias.",
    "precisa ser avaliado com cuidado.",
    "pode funcionar bem em diferentes situações.",
    "é interessante e merece mais discussão."
]

JUSTIFICATIVAS = [
    "Isso ajuda a entender melhor o contexto.",
    "O importante é considerar diferentes perspectivas.",
    "A organização faz diferença no resultado.",
    "Cada situação pode apresentar desafios próprios.",
    "Uma boa análise ajuda na tomada de decisões.",
    "É importante observar os detalhes.",
    "O planejamento pode facilitar o processo.",
    "A experiência também contribui para o aprendizado.",
    "Os resultados dependem de vários fatores.",
    "Revisar as possibilidades pode ser útil."
]


def gerar_respostas(quantidade=300):
    respostas = set()

    # As combinações possíveis são suficientes para 300 respostas.
    while len(respostas) < quantidade:
        inicio = random.choice(INICIOS)
        assunto = random.choice(ASSUNTOS)
        complemento = random.choice(COMPLEMENTOS)
        justificativa = random.choice(JUSTIFICATIVAS)

        resposta = (
            f"{inicio} {assunto} {complemento} "
            f"{justificativa}"
        )

        respostas.add(resposta)

    return list(respostas)


def salvar_arquivos(respostas):
    data = datetime.now().strftime("%Y%m%d_%H%M%S")

    arquivo_txt = PASTA / f"respostas_{data}.txt"
    arquivo_csv = PASTA / f"respostas_{data}.csv"

    with arquivo_txt.open("w", encoding="utf-8") as arquivo:
        for numero, resposta in enumerate(respostas, start=1):
            arquivo.write(f"{numero}. {resposta}\n\n")

    with arquivo_csv.open(
        "w", newline="", encoding="utf-8-sig"
    ) as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow(["Número", "Resposta"])

        for numero, resposta in enumerate(respostas, start=1):
            escritor.writerow([numero, resposta])

    return arquivo_txt, arquivo_csv


def main():
    print("=" * 50)
    print("       BOT GERADOR DE RESPOSTAS")
    print("=" * 50)

    quantidade = 300
    respostas = gerar_respostas(quantidade)

    print(f"\nGerando {quantidade} respostas...")
    for numero, resposta in enumerate(respostas, start=1):
        print(f"{numero:03d} - {resposta}")

    arquivo_txt, arquivo_csv = salvar_arquivos(respostas)

    print("\n" + "=" * 50)
    print(f"Concluído! {len(respostas)} respostas geradas.")
    print(f"Arquivo TXT: {arquivo_txt.name}")
    print(f"Arquivo CSV: {arquivo_csv.name}")
    print("=" * 50)


if __name__ == "__main__":
    main()
