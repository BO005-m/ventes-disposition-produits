# Étude de l'impact de l'emplacement des produits sur les ventes (Instacart Market Basket Analysis)

## Présentation du Projet

Ce projet propose une analyse de type **Market Basket Analysis** basée sur les données d'Instacart. L'objectif principal est d'étudier l'impact de l'emplacement virtuel ou physique des produits (les allées/rayons) sur le comportement d'achat des consommateurs et sur les ventes globales.

## Source des Données

La base de données utilisée provient de Kaggle : [Instacart Market Basket Analysis](https://www.kaggle.com/c/instacart-market-basket-analysis).
Elle simule les commandes de clients d'une épicerie en ligne et permet de reconstituer le parcours de constitution d'un panier.

## Étapes du Projet

### 1. Nettoyage et Préparation des Données (`Pandas`)

- **Gestion du stockage :** Extraction automatisée du jeu de données depuis l'archive ZIP principale et ses sous-archives.
- **Vérification de l'intégrité :** Contrôle des valeurs manquantes et validation des types de données (vérification que l'ensemble des identifiants `ID` soient bien typés en entiers).
- **Jointures de tables :** Fusion (_merge_) de la table des ventes `order_products__prior` avec les référentiels `products` et `aisles` afin de lier chaque ligne d'achat au nom de son rayon de destination.

### 2. Analyse de la Performance & KPIs

- **Volume de ventes :** Calcul du nombre total de ventes par allée (_aisle_) pour identifier les rayons moteurs du magasin.
- **Analyse du parcours client (Ordre d'ajout) :** Utilisation de la colonne `add_to_cart_order`.
  - _Hypothèse retenue :_ Les produits ajoutés en premier (valeur faible) agissent comme des **"produits aimants"** (achats planifiés/destination). À l'inverse, les produits ajoutés tardivement (valeur élevée) sont considérés comme des **achats d'impulsion**.
- **Fidélité et récurrence :** Calcul de la moyenne de la colonne `reordered` par catégorie pour obtenir le **taux de ré-achat** (_reorder rate_).

### 3. Visualisation Avancée (`Matplotlib` / `Seaborn`)

- **Simulations spatiales :** Création de graphiques analytiques pour lier la position au panier avec le taux de ré-achat.
- **Analyse de co-occurrence (Heatmaps) :** Construction d'une matrice de corrélation modélisant les allées les plus fréquemment visitées ensemble au cours d'une même commande, visualisée sous forme de carte de chaleur (_heatmap_).

### 4. Transition vers l'Analyse Statistique (R)

- Exportation des agrégations de performances au format CSV pour permettre une analyse statistique avancée complémentaire sous **R (via l'écosystème Tidyverse)**.

---

## Comment exécuter le projet ?

Assurez-vous que votre fichier ZIP d'origine est placé dans le dossier `data/`. Exécutez ensuite les scripts dans l'ordre suivant depuis votre terminal :

1. **Extraction et initialisation :**
   python code.py

2. **Analyse principale et Visualisation (Python):**
   python Analyse_Py.py
3. **Analyse Statistique Complémentaire (R - Optionnel) :**
   Rscript Analyse_R.R
