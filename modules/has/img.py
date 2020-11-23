import os
import numpy as np
import time
import cv2
from matplotlib import pyplot as plt

"""Класс операций с изображениями"""

class HorSunImg:
    @staticmethod
    def draw_img(img, w, h):
        fig, ax = plt.subplots()
        ax.imshow(img)
        fig.set_figwidth(w)
        fig.set_figheight(h)
        abc = plt.show()

    @staticmethod
    def get_av_px(arr): return int(np.sum(arr) / arr.size)