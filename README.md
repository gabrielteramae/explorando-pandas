# Explorando Pandas — carteira sintética

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.0+-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26+-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8+-11557C?logo=matplotlib&logoColor=white)

Script que gera preços diários de quatro ativos fictícios por random walk, calcula retorno, correlação e o valor de uma carteira com pesos fixos, e grava um painel em PNG. Não consulta preço de mercado. Não é recomendação de investimento.

## Stack

- Python 3.12, fixado no workflow
- pandas >= 2.0, NumPy >= 1.26, Matplotlib >= 3.8
- backend Matplotlib `Agg`, para gravar o PNG sem janela gráfica

## Estrutura

```
.
├── carteira.py                          # série sintética, métricas e painel
├── requirements.txt                     # numpy, pandas, matplotlib
└── .github/workflows/python-app.yml    # Python 3.12 e flake8
```

Os ativos são `ACAO_A`, `ACAO_B`, `TITULO_C` e `FUNDO_ESG`, em dias úteis de 2024-01-01 a 2025-12-31, com `np.random.seed(42)`. A carteira é 30/20/30/20 e começa em R$ 10.000. A volatilidade móvel é o desvio de 21 dias anualizado com √252.

## Como rodar

```bash
git clone https://github.com/gabrielteramae/explorando-pandas.git
cd explorando-pandas
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python carteira.py
```

O script imprime média, volatilidade, retorno total e a matriz de correlação, e salva `painel_carteira.png` no diretório atual.

## Testes realizados

Não há suíte de testes. O workflow instala as dependências e roda flake8: erros E9, F63, F7 e F82 quebram o job; o restante termina com `--exit-zero`.

---

© 2026 Gabriel Teramae Chan
