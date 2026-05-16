# ==============================================================================
# 1. CHARGEMENT DES BIBLIOTHÈQUES NÉCESSAIRES
# ==============================================================================
library(tidyverse)
library(corrplot)

# ==============================================================================
# 2. IMPORTATION DES DONNÉES PRÉPARÉES AVEC PYTHON
# ==============================================================================
data <- read_csv("aisle_performance_summary.csv")

# ==============================================================================
# 3. ANALYSE DESCRIPTIVE
# ==============================================================================
print("--- Résumé descriptif des variables ---")
print(summary(data))

# ==============================================================================
# 4. MODÉLISATION STATISTIQUE (RÉGRESSION LINÉAIRE)
# ==============================================================================
# Question : Est-ce que la position d'ajout au panier et le taux de ré-achat prédisent les ventes ?
model <- lm(total_sales ~ add_to_cart_order + reordered, data = data)

print("--- Résultats de la Régression ---")
print(summary(model))

# ==============================================================================
# 5. VISUALISATION STATISTIQUE ET SAUVEGARDE AVEC GGPLOT2
# ==============================================================================
ggplot(data, aes(x = add_to_cart_order, y = total_sales)) +
    geom_point(aes(size = reordered, color = reordered), alpha = 0.7) +
    geom_smooth(method = "lm", color = "red", se = TRUE) +
    scale_color_gradient(low = "blue", high = "green") +
    labs(
        title = "Impact de la disposition (Ordre d'ajout) sur le Volume de Ventes",
        x = "Ordre moyen d'ajout au panier (Proximité de l'entrée)",
        y = "Volume Total des Ventes",
        size = "Taux de Ré-achat",
        color = "Taux de Ré-achat"
    ) +
    theme_minimal()

# Sauvegarde automatique du graphique ggplot sous forme d'image PNG
ggsave("analyse_disposition_r.png", width = 10, height = 6, dpi = 300)
print("Graphique ggplot enregistré avec succès : 'analyse_disposition_r.png'")

# ==============================================================================
# 6. ANALYSE DE CORRÉLATION ET SAUVEGARDE DU CORRPLOT
# ==============================================================================
# Sélection des variables numériques pour la corrélation
cor_matrix <- cor(data %>% select(total_sales, reordered, add_to_cart_order))

# Configuration de la sauvegarde pour le graphique natif corrplot
png("corrplot_r.png", width = 800, height = 800, res = 120)
corrplot(cor_matrix, method = "color", addCoef.col = "black", tl.col = "black")
dev.off() # Fermeture du périphérique graphique pour enregistrer le fichier

print("Graphique de corrélation enregistré avec succès : 'corrplot_r.png'")
