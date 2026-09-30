# ======================== game.py ========================

import pygame
import random
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, GRAVITY, JUMP_VELOCITY, SPRING_JUMP_VELOCITY,
    DOODLE_SPEED, DOODLE_WIDTH, DOODLE_HEIGHT, PLATFORM_WIDTH,
    MIN_PLATFORM_GAP, MAX_PLATFORM_GAP, CAMERA_SCROLL_THRESHOLD,
    PLATFORMS, doodle_dict, DOODLE_START_X, DOODLE_START_Y, LIVES
)
from platforms import create_platform, choose_platform_type
from doodle import doodle_left_img, doodle_right_img
from window import generate_initial_platforms


# ======================== PARTIE 3.1 ========================
def apply_gravity():
    """
    Applique la gravité au Doodle en augmentant progressivement sa vitesse verticale (vel_y).
    Met à jour la position verticale (y) du Doodle.
    """
    doodle_dict["vel_y"] += GRAVITY
    doodle_dict["y"] += doodle_dict["vel_y"]

# ===========================================================


# ======================== PARTIE 1.2 ========================
def move_doodle():
    """
    Gère le déplacement horizontal du Doodle selon les touches pressées (Flèches ou A/D).
    Implémente le passage fluide d'un côté de l'écran à l'autre (Screen Wrap).
    """
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        doodle_dict["x"] -= DOODLE_SPEED
        doodle_dict["direction"] = "left"
        doodle_dict["image"] = doodle_left_img
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        doodle_dict["x"] += DOODLE_SPEED
        doodle_dict["direction"] = "right"
        doodle_dict["image"] = doodle_right_img

    # Le personnage sort entièrement de l'écran avant de réapparaître.
    if doodle_dict["x"] < -DOODLE_WIDTH:
        doodle_dict["x"] = SCREEN_WIDTH
    elif doodle_dict["x"] > SCREEN_WIDTH:
        doodle_dict["x"] = -DOODLE_WIDTH

# ===========================================================


# ======================== PARTIE 2.3 ========================
def move_platforms():
    """
    Déplace horizontalement les plateformes mobiles ("blue").
    Fait rebondir les plateformes lorsqu'elles atteignent les bords de la fenêtre.
    """
    for platform in PLATFORMS:
        if platform["type"] != "blue" or not platform["active"]:
            continue

        platform["x"] += platform["vx"]
        if platform["x"] <= 0:
            platform["x"] = 0
            platform["vx"] = abs(platform["vx"])
        elif platform["x"] + platform["width"] >= SCREEN_WIDTH:
            platform["x"] = SCREEN_WIDTH - platform["width"]
            platform["vx"] = -abs(platform["vx"])

# ===========================================================


# ======================== PARTIE 3.2 ========================
def check_platform_collisions():
    """
    Détecte si le Doodle atterrit sur une plateforme.
    Le rebond ne se produit QUE lorsque le Doodle descend (vel_y > 0)
    et qu'il arrive sur le dessus d'une plateforme.
    """
    if doodle_dict["vel_y"] <= 0:
        return

    doodle_rect = (doodle_dict["x"], doodle_dict["y"], DOODLE_WIDTH, DOODLE_HEIGHT)
    feet_y = doodle_dict["y"] + DOODLE_HEIGHT
    previous_feet_y = feet_y - doodle_dict["vel_y"]

    for platform in PLATFORMS:
        if not platform["active"]:
            continue

        platform_rect = (
            platform["x"], platform["y"], platform["width"], platform["height"]
        )
        if not rects_collide(doodle_rect, platform_rect):
            continue
        if previous_feet_y > platform["y"] + 14 or feet_y < platform["y"]:
            continue

        doodle_dict["y"] = platform["y"] - DOODLE_HEIGHT
        doodle_dict["vel_y"] = (
            SPRING_JUMP_VELOCITY if platform["type"] == "spring" else JUMP_VELOCITY
        )
        if platform["type"] == "brown":
            platform["active"] = False
        return

# ===========================================================


# ======================== PARTIE 3.3 ========================
def scroll_camera():
    """
    Fait défiler le monde lorsque le Doodle dépasse CAMERA_SCROLL_THRESHOLD.
    Met à jour le score et maintient les plateformes visibles.
    """
    # TODO : Lorsque le Doodle dépasse le seuil de caméra, il doit rester
    # visuellement au seuil pendant que les plateformes sont déplacées vers
    # le bas de la même distance.
    #
    # Le score doit représenter la distance verticale ainsi parcourue et le
    # meilleur score doit être mis à jour. Les plateformes sorties sous
    # l'écran doivent être retirées, puis de nouvelles plateformes générées.

    return

# ===========================================================


# ======================== PARTIE 3.4 ========================
def generate_new_platforms():
    """
    Génère de nouvelles plateformes au-dessus du haut de l'écran pour maintenir
    un flux continu lorsque la caméra défile.
    """
    # TODO : Complétez cette fonction en vous inspirant de la logique de
    # génération initiale, sans la recopier inutilement.
    #
    # Vous devrez partir de la plateforme actuellement la plus haute et
    # continuer à ajouter des plateformes tant que nécessaire. Utilisez
    # choose_platform_type(...) avec les probabilités indiquées dans le README.

    return

# ===========================================================


def check_game_over():
    """
    Vérifie si le Doodle tombe sous le bas de l'écran.
    Si oui, réduit les vies.
    Retourne True si la partie est terminée.
    """
    if doodle_dict["y"] > SCREEN_HEIGHT:
        doodle_dict["lives"] -= 1
        return True
    return False


def restart_game():
    """
    Réinitialise la partie : position du Doodle, vitesse, score et plateformes.
    """
    doodle_dict["x"] = DOODLE_START_X
    doodle_dict["y"] = DOODLE_START_Y
    doodle_dict["vel_y"] = 0.0
    doodle_dict["direction"] = "right"
    doodle_dict["image"] = doodle_right_img
    doodle_dict["score"] = 0
    doodle_dict["lives"] = LIVES

    generate_initial_platforms()


def rects_collide(r1, r2):
    """
    Vérifie si deux rectangles (x, y, largeur, hauteur) se chevauchent.
    Cette fonction est fournie et ne doit pas être modifiée.
    """
    return not (
        r1[0] + r1[2] <= r2[0] or r1[0] >= r2[0] + r2[2] or
        r1[1] + r1[3] <= r2[1] or r1[1] >= r2[1] + r2[3]
    )
