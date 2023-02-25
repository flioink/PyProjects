from os import walk, listdir
import pygame


def import_folder(path):
    surface_list = []

    for _, _, img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image

            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list


def import_folder_dict(path):
    surface_dict = {}

    sprites_list = listdir(path)

    for i, name in enumerate(sprites_list):
        full_path = path + "/" + name
        image_surf = pygame.image.load(full_path).convert_alpha()
        surface_dict[name.split(".")[0]] = image_surf

    return surface_dict
