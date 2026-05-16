import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile

# ==========================================
# 1. CHARGEMENT ET NETTOYAGE (Python/Pandas)
# ==========================================
# dézipper le dossier instacart-market-basket-analysis.zip
# Chemin du fichier ZIP à extraire
chemin_zip = r"data\instacart_market_basket_analysis.zip"

# Dossier de destination où extraire les fichiers
dossier_destination = r"data"

# Ouverture et extraction du fichier ZIP
with zipfile.ZipFile(chemin_zip, 'r') as mon_zip:
    mon_zip.extractall(dossier_destination)

print("Extraction terminée avec succès !")
# Chargement des fichiers
# Note : Utilisez nrows pour tester sur un échantillon si le fichier est trop lourd
products = pd.read_csv(r'data\products.csv')
aisles = pd.read_csv(r'data\aisles.csv')
orders_prior = pd.read_csv(r'data\order_products__prior.csv', nrows=1000000)

# Jointures pour lier les ventes aux rayons (Aisles)
df = orders_prior.merge(products, on='product_id')
df = df.merge(aisles, on='aisle_id')

# Suppression des colonnes inutiles pour optimiser la mémoire
df = df.drop(['product_id', 'aisle_id', 'department_id'], axis=1)

# ==========================================
# 2. CALCUL DES KPI DE PERFORMANCE
# ==========================================

# Calcul par allée (aisle) : 
# - Volume total de ventes
# - Taux de ré-achat (reorder rate)
# - Position moyenne d'ajout au panier (indicateur de flux)
aisle_analysis = df.groupby('aisle').agg({
    'order_id': 'count',
    'reordered': 'mean',
    'add_to_cart_order': 'mean'
}).rename(columns={'order_id': 'total_sales'}).reset_index()

# Tri par volume de ventes
aisle_analysis = aisle_analysis.sort_values(by='total_sales', ascending=False)

print("--- Top 10 des allées les plus performantes ---")
print(aisle_analysis.head(10))

# ==========================================
# 3. VISUALISATION (Matplotlib / Seaborn)
# ==========================================

plt.figure(figsize=(14, 7))

# Graphique 1 : Volume de ventes par Allée (Top 15)
plt.subplot(1, 2, 1)
sns.barplot(data=aisle_analysis.head(15), x='total_sales', y='aisle', palette='viridis')
plt.title('Top 15 des Allées par Volume de Ventes')
plt.xlabel('Nombre de Ventes')

# Graphique 2 : Relation entre Position au panier et Ré-achat
# Utile pour identifier les produits "Destination" vs "Impulsion"
plt.subplot(1, 2, 2)
sns.scatterplot(data=aisle_analysis, x='add_to_cart_order', y='reordered', 
                size='total_sales', alpha=0.6, sizes=(20, 500))
plt.title('Position au panier vs Taux de Ré-achat')
plt.xlabel('Ordre d\'ajout moyen')
plt.ylabel('Taux de Ré-achat')

plt.tight_layout()
plt.show()

# ==========================================
# 4. EXPORT POUR ANALYSE STATISTIQUE (R)
# ==========================================
# On sauvegarde le résumé pour l'ouvrir facilement dans R (tidyverse)
aisle_analysis.to_csv('aisle_performance_summary.csv', index=False)