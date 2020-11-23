import os
import time
import cv2

from settings import degs_mins_separator, is_parsing_time


def read_imgs(main_path, paths):
    imgs = []
    length = 0
    for path in paths:
        file_name, ext = os.path.splitext(path)
        path = os.path.join(main_path, path)

        if ext.lower() != '.jpg':
            continue

        # парсинг имени файла
        name_parts = file_name.split('_')  # [degs°mins, datetime]
        degs, mins = map(float, name_parts[0].split(
            degs_mins_separator))  # [degs, mins]

        img_time = time.gmtime(time.time())
        # если в данных есть дата, то берем ее из названия файла
        if is_parsing_time:
            img_time = time.strptime(name_parts[1], '%Y%m%d%H%M%S')  # datetime

        # считывание изображение и его параметров
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        height, width = img.shape[0], img.shape[1]

        imgs.append([img, [[degs, mins], [height, width], img_time]])
        length += 1

    return imgs, length
