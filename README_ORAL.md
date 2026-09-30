# Fiche pour l'oral

Ce fichier explique seulement les parties qu'on a terminées. On l'ajoutera à chaque nouvelle étape.

## 1.1 — Position de départ du Doodle

**Changement dans `doodle.py` :** j'ai remplacé `x = 1000` et `y = 1000` par `DOODLE_START_X` et `DOODLE_START_Y`.

**Pourquoi :** `1000` place le personnage hors de la fenêtre. Les constantes de `config.py` le placent au centre, juste au-dessus de la plateforme verte. Elles sont aussi utilisées quand on recommence une partie.

**À dire à l'oral :** « Le Doodle est stocké dans un dictionnaire. Ses clés `x` et `y` donnent sa position. J'utilise les constantes de départ pour qu'il apparaisse au bon endroit, sans écrire des coordonnées fixes. »

**Question possible — C'est quoi `doodle_dict.update()` ?** Ça ajoute ou modifie plusieurs valeurs dans le dictionnaire du Doodle.

## 1.2 — Déplacement horizontal

**Changement dans `game.py` :** `move_doodle()` lit les touches avec `pygame.key.get_pressed()`. Gauche ou A enlève `DOODLE_SPEED` à `x` et choisit l'image de gauche. Droite ou D ajoute cette vitesse et choisit l'image de droite.

**Passage d'un bord à l'autre :** quand le Doodle est entièrement sorti à gauche (`x < -DOODLE_WIDTH`), il revient à `SCREEN_WIDTH`. À droite (`x > SCREEN_WIDTH`), il revient à `-DOODLE_WIDTH`.

**À dire à l'oral :** « À chaque image, je lis le clavier, je change la position et l'image selon la direction. Si le Doodle sort complètement de l'écran, je le replace de l'autre côté. »

## 2.1 — Créer une plateforme

**Changement dans `platforms.py` :** `create_platform(x, y, platform_type)` retourne un dictionnaire avec la position reçue, le type et son image. La plateforme est active et garde la largeur normale.

**Selon le type :** seule la bleue reçoit `MOVING_PLATFORM_SPEED` ; seule la plateforme à ressort a 10 pixels de hauteur en plus. Les autres ont une vitesse nulle et une hauteur normale.

**À dire à l'oral :** « Je réutilise une seule fonction pour créer les quatre types. Le paramètre `platform_type` choisit l'image et les propriétés propres à chaque plateforme. »
