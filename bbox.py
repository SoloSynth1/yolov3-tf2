import random

SEED = 114514


def get_colors(class_names, seed=SEED):
    if seed:
        random.seed(seed)
    colors = {}
    for key in class_names:
        colors[key] = tuple([random.randint(100, 255) for _ in range(3)])
    return colors


