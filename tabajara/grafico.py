import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

df = pd.read_excel("produtos.xlsx")

cores = ("#4118e7", "#0080ff","#76a3f7", "#A0F4FF")
fig. ax = plt.subplot(figsize=(9, 7))
wedges, texts, autotexts = ax.pie(
    df["valor"],
    autopct ="%1.1%%",
    colors = cores,
    startangle = 140,
    pctdistance = 0.75,
    wedgeprops = dict(edgecolor= "white", linewidth = 3, widt = 0.6))

total = df["valor"].sum()

ax.text(0,0, f"total\nR${total:,.0f}", ha = "center", va = "center", fontsize= 14,fontweight= "bold")

ax.set_title("Distribuição de Produtor por Valor", fontsize = 16, fontweight= "bold")

plt.tight_layout()

plt.savefig("grafico_donut.png", dpi = 150)

print(df)

plt.show()