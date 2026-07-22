# 📊 Explorando Pandas

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.0-150458?style=flat&logo=pandas&logoColor=white)
![matplotlib](https://img.shields.io/badge/matplotlib-3.8-11557C?style=flat)

Script exploratório em Python (`pandas` + `matplotlib`) simulando uma carteira de investimentos com dados sintéticos: retornos, correlação entre ativos e volatilidade móvel. Sem projeto formal, feito pra treinar as ferramentas na prática.

## 🧠 O que o script faz

- Gera preços sintéticos de 4 ativos fictícios (random walk) com `numpy`
- Calcula retornos diários, volatilidade e retorno total com `pandas`
- Monta uma carteira ponderada (30/20/30/20) e acompanha sua evolução
- Calcula volatilidade móvel anualizada (janela de 21 dias)
- Plota um painel 2x2 com `matplotlib`: preços normalizados, evolução da carteira, heatmap de correlação e volatilidade móvel

## 🚀 Como rodar

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

python carteira.py
```

Gera o arquivo `painel_carteira.png` na mesma pasta.

## 🔧 Pra brincar

- Muda `np.random.seed(42)` pra ver outros cenários
- Ajusta os `pesos` da carteira (linha ~68)
- Troca os parâmetros de `drift`/`vol` de cada ativo pra simular cenários diferentes

## 🔮 Próximos passos possíveis

- Trocar dados sintéticos por preços reais via `yfinance`
- Trocar `matplotlib` por `plotly` pra gráficos interativos
- Adicionar métricas de Sharpe ratio e drawdown máximo

---

© 2026 Gabriel Teramae Chan
