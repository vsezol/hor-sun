import cv2
import math
import numpy.linalg as linalg
from modules.has.vct import HorSunVct

class HorSunCnt:
    @staticmethod
    def get_cnt_center(c):
        M = cv2.moments(c)     
        try:
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            return [cX, cY]
        except ZeroDivisionError:
            return [None, None]

    @staticmethod
    def get_cnt_r(c): return round(cv2.arcLength(c, True) / (2*math.pi))

    @staticmethod
    def approx_cnt(c, k):
        peri = cv2.arcLength(c, True)
        return cv2.approxPolyDP(c, k*peri, True)

    @staticmethod
    def get_upper_line(cnts):
        min_y = 999999
        max_len = 0
        upper_line = [(0, 0, 0, 0), (0, 0, 0), 0]
        n = len(cnts)

        for i in range(n - 1):
            if i == n + 1:
                x1, y1 = cnts[i]
                x2, y2 = cnts[0]
            else:
                x1, y1 = cnts[i]
                x2, y2 = cnts[i + 1]

            av_y = (y1 + y2) / 2
            line_len = linalg.norm([x2-x1, y2-y1])

            # if angel = 90.0
            try: k, b = HorSunVct.get_linear_eq(x1, y1, x2, y2)
            except linalg.LinAlgError: continue
            angle = math.atan(k)
            # if angel > 60.0
            if abs(math.degrees(angle)) > 60.0: continue
            
            if av_y < min_y:
                min_y = av_y
                # upper_line = x1, y1, x2, y2
                upper_line = [(x1, y1, x2, y2), (k, b, angle), line_len]
        return upper_line