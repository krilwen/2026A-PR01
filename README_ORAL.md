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

## 2.2 — Choix et génération des plateformes

**Dans `platforms.py` :** `choose_platform_type()` tire un nombre entre 0 et 1. Les seuils cumulés 0,65, 0,82 et 0,92 donnent 65 % de vertes, 17 % de bleues, 10 % de ressorts et 8 % de marron.

**Dans `window.py` :** une boucle ajoute des plateformes jusqu'en haut. Leur `x` reste dans la fenêtre, leur `y` monte d'un écart aléatoire, et leur type vient de `choose_platform_type()`.

**À dire à l'oral :** « J'ai mis le tirage des types dans une fonction réutilisable. La génération l'appelle pour chaque plateforme et avance vers le haut avec un espacement aléatoire. »

## 2.3 — Plateformes bleues mobiles

**Changement dans `game.py` :** `move_platforms()` ajoute `vx` à `x` seulement pour les plateformes bleues actives. Au bord gauche (`x <= 0`) ou droit (`x + width >= SCREEN_WIDTH`), elle garde la plateforme dans la fenêtre et inverse le sens de `vx`.

**À dire à l'oral :** « La vitesse `vx` fait bouger les plateformes bleues. Aux bords, je corrige leur position et je change le signe de la vitesse pour les faire repartir dans l'autre sens. »

## 3.1 — Gravité

**Changement dans `game.py` :** `apply_gravity()` ajoute `GRAVITY` à `vel_y`, puis ajoute cette nouvelle vitesse à `y` à chaque image.

**À dire à l'oral :** « La gravité augmente la vitesse vers le bas. Une vitesse négative fait monter le Doodle ; une vitesse positive le fait descendre. »

## 3.2 — Collision et rebond

**Changement dans `game.py` :** `check_platform_collisions()` vérifie que le Doodle descend, que la plateforme est active, que leurs rectangles se touchent et que ses pieds arrivent par-dessus. La position précédente des pieds est estimée avec `vel_y` ; une tolérance de 14 pixels est admise.

**Rebond :** le Doodle est replacé sur la plateforme. Le ressort donne `SPRING_JUMP_VELOCITY` ; les autres donnent `JUMP_VELOCITY`. La plateforme marron devient inactive. La fonction s'arrête après un rebond.

**À dire à l'oral :** « Un chevauchement seul ne suffit pas : je vérifie aussi que le Doodle descend et arrive sur le dessus. Ensuite je lui donne une vitesse négative pour le faire remonter. »
