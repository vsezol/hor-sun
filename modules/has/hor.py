import cv2
import numpy as np
import math
from modules.has.img import HorSunImg
from modules.has.cnt import HorSunCnt
from modules.has.vct import HorSunVct


def get_hor_params(img, size):
    w, h = size
    blur = cv2.medianBlur(img, 11)

    low_threshold = round(HorSunImg.get_av_px(img) / 2)
    max_threshold = low_threshold * 5

    edged = cv2.Canny(blur, low_threshold, max_threshold, apertureSize=5)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (41, 21))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    cnts, _ = cv2.findContours(
        closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # new alg
    min_upl_angle = 90
    max_upl_len = 0
    max_upl = None
    for c in cnts:
        if cv2.arcLength(c, True) > w:
            c = HorSunCnt.approx_cnt(c, 0.02)  # аппроксимируем контур

            # поиск прямоугольника
            rect = cv2.minAreaRect(c)  # пытаемся вписать прямоугольник
            box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
            box = np.int0(box)  # округление координат

            # поиск верхней линии прямоугольника
            curr_upl = HorSunCnt.get_upper_line(box)
            [(upx1, upy1, upx2, upy2), (k, b, upl_angle), upl_len] = curr_upl
            upl_deg_angle = math.degrees(upl_angle)
            # ограничиваем пределами ширины фото
            if upx2 > w:
                upx2 = w
            if upx1 < 0:
                upx1 = 0

            if upl_len <= 0.98*w:
                continue

            if upl_len > max_upl_len and upl_deg_angle < min_upl_angle:
                max_upl = curr_upl

    return max_upl
