"""
carteira.py

Script exploratório pra brincar com pandas + matplotlib.
Gera preços sintéticos de 4 ativos fictícios (random walk), calcula
retornos, volatilidade, correlação e evolução de uma carteira,
e plota tudo em um painel de gráficos.

Sem API externa, sem projeto formal — só pra testar/aprender.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------------------
# 1. Gerar dados sintéticos (preços diários de 4 ativos, 2 anos)
# -----------------------------------------------------------------
np.random.seed(42)

ativos = ["ACAO_A", "ACAO_B", "TITULO_C", "FUNDO_ESG"]
dias = pd.date_range(start="2024-01-01", end="2025-12-31", freq="B")  # dias úteis

# cada ativo tem um drift (tendência) e volatilidade diferentes
params = {
    "ACAO_A":    {"drift": 0.0006, "vol": 0.020, "preco_inicial": 50},
    "ACAO_B":    {"drift": 0.0003, "vol": 0.015, "preco_inicial": 30},
    "TITULO_C":  {"drift": 0.0002, "vol": 0.004, "preco_inicial": 100},
    "FUNDO_ESG": {"drift": 0.0005, "vol": 0.012, "preco_inicial": 20},
}

precos = pd.DataFrame(index=dias)
for ativo, p in params.items():
    retornos_diarios = np.random.normal(p["drift"], p["vol"], len(dias))
    precos[ativo] = p["preco_inicial"] * (1 + retornos_diarios).cumprod()

print("Preview dos preços:")
print(precos.head())
print(f"\nTotal de dias: {len(precos)}\n")

# -----------------------------------------------------------------
# 2. Retornos diários e estatísticas básicas
# -----------------------------------------------------------------
retornos = precos.pct_change().dropna()

print("Estatísticas dos retornos diários (%):")
stats = pd.DataFrame({
    "media_diaria_%": retornos.mean() * 100,
    "vol_diaria_%": retornos.std() * 100,
    "retorno_total_%": (precos.iloc[-1] / precos.iloc[0] - 1) * 100,
})
print(stats.round(3))
print()

# -----------------------------------------------------------------
# 3. Correlação entre os ativos
# -----------------------------------------------------------------
corr = retornos.corr()
print("Matriz de correlação:")
print(corr.round(2))
print()

# -----------------------------------------------------------------
# 4. Carteira: 30% ACAO_A, 20% ACAO_B, 30% TITULO_C, 20% FUNDO_ESG
# -----------------------------------------------------------------
pesos = {"ACAO_A": 0.30, "ACAO_B": 0.20, "TITULO_C": 0.30, "FUNDO_ESG": 0.20}
retorno_carteira = (retornos * pd.Series(pesos)).sum(axis=1)
valor_carteira = (1 + retorno_carteira).cumprod() * 10_000  # começa com R$10.000

# volatilidade móvel de 21 dias (~1 mês útil) anualizada
vol_movel = retorno_carteira.rolling(21).std() * np.sqrt(252) * 100

print(f"Valor final da carteira: R$ {valor_carteira.iloc[-1]:,.2f}")
print(f"Retorno total da carteira: {(valor_carteira.iloc[-1] / 10_000 - 1) * 100:.2f}%")

# -----------------------------------------------------------------
# 5. Painel de gráficos
# -----------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Exploração de Carteira — dados sintéticos", fontsize=14, fontweight="bold")

# preços normalizados (base 100)
ax = axes[0, 0]
(precos / precos.iloc[0] * 100).plot(ax=ax)
ax.set_title("Preços normalizados (base 100)")
ax.set_ylabel("Índice")
ax.legend(fontsize=8)

# valor da carteira ao longo do tempo
ax = axes[0, 1]
valor_carteira.plot(ax=ax, color="darkgreen")
ax.set_title("Evolução da carteira (R$ 10.000 iniciais)")
ax.set_ylabel("R$")

# heatmap de correlação
ax = axes[1, 0]
im = ax.imshow(corr, cmap="RdYlGn", vmin=-1, vmax=1)
ax.set_xticks(range(len(ativos)))
ax.set_yticks(range(len(ativos)))
ax.set_xticklabels(ativos, rotation=45, ha="right")
ax.set_yticklabels(ativos)
for i in range(len(ativos)):
    for j in range(len(ativos)):
        ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", fontsize=9)
ax.set_title("Correlação entre ativos")
fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

# volatilidade móvel anualizada da carteira
ax = axes[1, 1]
vol_movel.plot(ax=ax, color="crimson")
ax.set_title("Volatilidade móvel anualizada da carteira (21d)")
ax.set_ylabel("%")

plt.tight_layout()
plt.savefig("painel_carteira.png", dpi=130)
print("\nGráfico salvo em painel_carteira.png")
