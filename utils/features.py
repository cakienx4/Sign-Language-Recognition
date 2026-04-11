import numpy as np

def normalize_landmarks(coords):
    coords = coords - coords[0]

    max_val = np.max(np.abs(coords))
    if max_val != 0:
        coords = coords / max_val

    return coords


def compute_distances(coords):
    def dist(i, j):
        return np.linalg.norm(coords[i] - coords[j])

    pairs = [
        (4,8), (8,12), (12,16), (16,20),
        (0,8), (0,12), (0,16), (0,20)
    ]

    return np.array([dist(i, j) for i, j in pairs])


def extract_features(coords):
    coords = normalize_landmarks(coords)
    distances = compute_distances(coords)
    return np.concatenate([coords.flatten(), distances])