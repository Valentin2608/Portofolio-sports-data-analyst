# ⚽ Modèle Expected Goals (xG) — StatsBomb Open Data

## 📌 Présentation du projet

Ce projet consiste à construire un **modèle d’Expected Goals (xG)** à partir des **données ouvertes StatsBomb**.
L’objectif est d’estimer la probabilité qu’un tir se transforme en but en fonction de sa localisation et de certaines caractéristiques contextuelles.

Ce projet a été réalisé dans une logique de **portfolio en data sport**, avec un accent particulier sur :
- la compréhension du jeu
- la qualité de la feature engineering
- l’interprétabilité du modèle
- la clarté du code et de la démarche

---

## 🎯 Objectifs

- Extraire les tirs à partir des fichiers d’événements StatsBomb (JSON)
- Construire des variables pertinentes inspirées du football réel
- Entraîner un modèle xG simple et interprétable
- Évaluer les performances du modèle
- Attribuer une valeur xG à chaque tir

---

## 📂 Structure du projet

```
xG-analysis/
│
├── code/
│   ├── Data_extract.py         # Extraction des tirs depuis les JSON StatsBomb
│   ├── Data modelling.py       # Calcul de la distance et de l’angle
│   ├── train_xg_model.py       # Modèle xG de base
│   └── Data visualiation.py    # Visualisation des résultats du modèle
│
├── data/
│   ├── data1.json              # Events StatsBomb
│   └── data2.json              # Events StatsBomb
│   └── data17.json             # Events StatsBomb
│
├── result/
│   ├── shots_features.csv      # Tirs extraits bruts (sans feature engineering)
│   ├── shots_raw.csv           # Tirs enrichis avec les variables de distance et d’angle
│   ├── shots_with_xg.csv       # Tirs avec la probabilité xG prédite par le modèle
│   └── figures/
│       ├── goals_vs_xg.png         # Comparaison entre buts réels et buts attendus (xG)
│       ├── xg_distribution.png    # Distribution des valeurs xG pour l’ensemble des tirs
│       └── xg_vs_distance.png     # Relation entre la distance au but et la probabilité xG
│
├── requirements.txt
└── README.md

## 📊 Données

- **Source** : StatsBomb Open Data
- **Périmètre** : tirs hors penalty

Les penalties ont volontairement été exclus afin d’éviter de biaiser le modèle.

---

## 🧮 Feature engineering

### 1. Localisation du tir
- **Distance au but** (en mètres)
- **Angle de tir** (en radians), calculé à partir de la position des poteaux

### 2. Contexte du tir
- **Partie du corps**
  - variable binaire `is_header` (tir de la tête ou non)

### 3. Interaction non linéaire
- **Distance × Angle**

Cette variable permet de capturer le fait que l’impact de l’angle dépend fortement de la distance au but.

---

## 📐 Modèle

### Algorithme
- **Régression logistique**

Ce choix est volontaire :
- modèle standard en analyse football
- facilement interprétable
- robuste sur des volumes de données limités

### Variable cible
```text
is_goal = 1 si le tir est un but, 0 sinon
```

### Variables utilisées (modèle v2)
- distance
- angle
- is_header
- distance_angle

---

## 📈 Performance du modèle

| Indicateur | Valeur |
|----------|--------|
| ROC AUC  | ~0.65 – 0.70 |
| Log Loss | ~0.34 |

Ces résultats sont cohérents avec un **modèle xG simple**, entraîné sur des données ouvertes et sans tracking.

---

## 🧠 Interprétation

- Plus un tir est **loin**, moins il a de chances de finir au fond
- Un **angle ouvert** augmente la probabilité de marquer
- Les **têtes** ont une probabilité plus faible que les tirs du pied
- L’interaction distance × angle capture des effets spatiaux non linéaires

---

## 🏷 Résultat xG

Chaque tir se voit attribuer une probabilité :

```text
xG ∈ [0,1]
```

Le fichier final est disponible ici :
```
result/shots_with_xg.csv
```

---

## ⚠️ Limites

- Taille d’échantillon limitée
- Pas de données de tracking (pression, gardien, défenseurs)
- Modèle volontairement simple

Ce projet n’a pas vocation à rivaliser avec les modèles commerciaux, mais de faire un premier pas de l'analyse de données dans le footbal.

---

## 🚀 Pistes d’amélioration

- Ajout du type de tir
- Modèles non linéaires (Random Forest, XGBoost)
- Comparaison avec des xG de référence
- Position du gardien et des défenseurs (pression au moment du tir)

---

## 👤 Auteur

**Valentin Guisnet**
Formation ingénieur — expérience en finance (trading FX)
Reconversion vers les métiers de la **data dans le sport**

---




