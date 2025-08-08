import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot(scores, title, yrange, line1, line2, width=8):

    scores["indice"] = scores.index.get_level_values("indice")

    has_cat = "cat" in scores.index.names

    middle = (yrange[0] + yrange[1])/2

    #width = int((len(scores) * 8) / 13)

    # Créer le graphique
    fig, ax = plt.subplots(figsize=(width, 5), layout="constrained")

    # Références horizontales
    for y, color in zip([middle-line2, middle-line1, middle, middle+line1, middle+line2], ["orange", "blue", "red", "blue", "orange"]):
        ax.axhline(y, color=color, linewidth=1.5, linestyle="-", zorder=0, alpha=0.5)

    # Barres
    b = sns.barplot(data=scores, x="indice", y='score', hue='cat' if has_cat else "indice", palette='Set2', ax=ax, width=0.5)
    if has_cat:
        b.legend_.remove()

    # Axe principal (labels des tests)
    #ax.set_xticks(np.arange(len(scores)))

    ax.set_xticklabels(scores.index.get_level_values("indice"), rotation=0)
    ax.set_ylim(yrange[0], yrange[1])
    ax.set_ylabel("Notes")

    # Afficher les scores sous les barres
    for i, score in enumerate(scores.score.values):
        ax.text(i, score + 0.3, str(int(score)), ha='center', va='bottom', fontsize=9)

    # Axe secondaire pour les catégories
    if has_cat:

        sec = ax.secondary_xaxis(location=0)
        group_labels = []
        group_centers = []
        current_group = None
        start = 0

        # Calcul des centres pour les groupes
        for i, (cat, _) in enumerate(scores.index):
            if cat != current_group:
                if current_group is not None:
                    center = (start + i - 1) / 2
                    group_centers.append(center)
                    group_labels.append(current_group)
                current_group = cat
                start = i
        # Ajouter le dernier groupe
        center = (start + len(scores) - 1) / 2
        group_centers.append(center)
        group_labels.append(current_group)

        sec.set_xticks(group_centers)
        sec.set_xticklabels(["\n\n" + label for label in group_labels])
        sec.tick_params('x', length=0)

        # Axe secondaire pour lignes séparatrices
        sec2 = ax.secondary_xaxis(location=0)
        boundaries = [-0.5]
        for i in range(1, len(scores)):
            if scores.index[i][0] != scores.index[i - 1][0]:
                boundaries.append(i - 0.5)
        boundaries.append(len(scores) - 0.5)

        sec2.set_xticks(boundaries)
        sec2.set_xticklabels([])
        sec2.tick_params('x', length=30, width=1.5)
        ax.set_xlim(-0.6, len(scores) - 0.4)

    plt.title(title)
    plt.xlabel('')
    return plt