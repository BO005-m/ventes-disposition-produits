import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 1. Chargement des données (le résumé généré précédemment)
try:
    data = pd.read_csv("aisle_performance_summary.csv")
except FileNotFoundError:
    print("Erreur : Le fichier 'aisle_performance_summary.csv' est introuvable.")
    exit()

# 2. Modélisation Statistique (Régression Linéaire OLS)
# On veut savoir si l'ordre d'ajout (X1) et le ré-achat (X2) prédisent les ventes (y)
X = data[['add_to_cart_order', 'reordered']]
X = sm.add_constant(X)  # Obligatoire en Python pour ajouter l'interception (le 'b' dans ax+b)
y = data['total_sales']

model = sm.OLS(y, X).fit()

# Affichage du rapport statistique complet
print("\n" + "="*30)
print("RAPPORT DE RÉGRESSION LINÉAIRE")
print("="*30)
print(model.summary())

# 3. Visualisation : Matrice de Corrélation
plt.figure(figsize=(10, 6))
correlation_matrix = data[['total_sales', 'reordered', 'add_to_cart_order']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='RdBu_r', center=0, fmt=".2f")
plt.title("Corrélations entre Variables de Vente et Disposition")
plt.tight_layout()
plt.show()

# 4. Visualisation : Impact de la disposition sur les performances
plt.figure(figsize=(10, 6))
sns.regplot(data=data, x='add_to_cart_order', y='total_sales', 
            scatter_kws={'alpha':0.4, 'color':'teal'}, 
            line_kws={'color':'red', 'label':'Tendance'})
plt.title("Analyse de Performance : Disposition vs Volume de Ventes")
plt.xlabel("Position moyenne d'ajout au panier (Proxy de la disposition)")
plt.ylabel("Volume Total des Ventes")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()