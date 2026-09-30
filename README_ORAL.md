# Fiche pour l'oral

Ce fichier explique seulement les parties qu'on a terminées. On l'ajoutera à chaque nouvelle étape.

## 1.1 — Position de départ du Doodle

**Changement dans `doodle.py` :** j'ai remplacé `x = 1000` et `y = 1000` par `DOODLE_START_X` et `DOODLE_START_Y`.

**Pourquoi :** `1000` place le personnage hors de la fenêtre. Les constantes de `config.py` le placent au centre, juste au-dessus de la plateforme verte. Elles sont aussi utilisées quand on recommence une partie.

**À dire à l'oral :** « Le Doodle est stocké dans un dictionnaire. Ses clés `x` et `y` donnent sa position. J'utilise les constantes de départ pour qu'il apparaisse au bon endroit, sans écrire des coordonnées fixes. »

**Question possible — C'est quoi `doodle_dict.update()` ?** Ça ajoute ou modifie plusieurs valeurs dans le dictionnaire du Doodle.
