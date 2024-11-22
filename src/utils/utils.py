
import numpy as np
import pygame

def normalize(arr):
    v_min = np.min(arr)
    v_max = np.max(arr)
    return (arr - v_min) / (v_max - v_min) if v_max != v_min else arr 
