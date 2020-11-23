import cv2
import numpy as np
from modules.has.cnt import HorSunCnt

def get_sun_params(img):
    # медианный фильтр
    img = cv2.medianBlur(img, 111)
    
    # порог бинаризации
    hold = np.max(img) - 10

    # бинаризация
    thresh_img = cv2.threshold(img, hold, 255, cv2.THRESH_BINARY)[1]
    
    # контура
    cnts, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # ====================
    # поиск контура солнца
    # ====================

    # параметры последнего контура
    last_cnt = cnts[0]
    last_cx, last_cy = HorSunCnt.get_cnt_center(cnts[0])

    # перебор контуров
    for c in cnts:
        if len(c) > 4:
            cx, cy = HorSunCnt.get_cnt_center(c)
            # поиск самого высокого центра
            if cy <= last_cy:
                last_cnt, last_cy, last_cx = c, cy, cx
            else:
                continue

    # радиус найденного контура
    r = HorSunCnt.get_cnt_r(last_cnt)

    return last_cnt, [last_cx, last_cy], r