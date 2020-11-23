import math

import cv2
from numpy.linalg import linalg

from settings import is_dev

from modules.has.sun import get_sun_params
from modules.has.hor import get_hor_params


def calc_dist(start_img):
    gray_img = cv2.cvtColor(start_img, cv2.COLOR_BGR2GRAY)

    sun_contour, [sun_cx, sun_cy], sun_r = get_sun_params(gray_img)
    lower_sun_y = sun_cy + sun_r

    gray_timg = gray_img[lower_sun_y:]
    timg_height, timg_width = gray_timg.shape[0], gray_timg.shape[1]

    [
        (hor_x1, hor_y1, hor_x2, hor_y2),
        (hor_k, hor_b, hor_angle),
        hor_len
    ] = get_hor_params(gray_timg, (timg_width, timg_height))

    hor_y1 += lower_sun_y
    hor_y2 += lower_sun_y
    hor_b += lower_sun_y

    cross_x = int(sun_cx)
    cross_y = int(hor_k * cross_x + hor_b)
    cross_line = (sun_cx, sun_cy, cross_x, cross_y)
    cross_line_len = linalg.norm(
        [cross_line[2] - cross_line[0], cross_line[3] - cross_line[1]])

    # !!!
    dist_btw_hor_sun = cross_line_len * math.cos(hor_angle) - sun_r

    if is_dev:
        # центр солнца
        cv2.circle(
            start_img,
            (sun_cx, sun_cy), 5,
            (0, 48, 242), 10
        )
        # окружность солнца
        cv2.circle(
            start_img,
            (sun_cx, sun_cy),
            sun_r,
            (0, 48, 242),
            10
        )
        # нижняя граница солнца
        cv2.line(
            start_img,
            (sun_cx - sun_r, lower_sun_y),
            (sun_cx + sun_r, lower_sun_y),
            (242, 14, 105),
            10
        )
        # линия горизонта
        cv2.line(
            start_img,
            (hor_x1, hor_y1),
            (hor_x2, hor_y2),
            (255, 0, 0),
            10
        )
        # перпендикуляр от солнца
        cv2.line(
            start_img,
            (cross_line[0],
            cross_line[1]),
            (cross_line[2], cross_line[3]),
            (0, 255, 0),
            10
        )
        return dist_btw_hor_sun, hor_angle, start_img

    else:
        return dist_btw_hor_sun, hor_angle, None
