import os
import time
import math

import cv2
import numpy as np
import pandas as pd

# модули
from modules.has.img import HorSunImg
from calc_dist import calc_dist
from modules.read.read_imgs import read_imgs
from modules.print.dev_print import print_img_info, print_end_info
from modules.timer import create_timer, calc_delta_time

# настройки
from settings import output_path, output_path_csv, input_path, to_read_imgs_list, is_dev

# главная часть программы
dev_timer = create_timer(time.time())
last_time = dev_timer()

imgs, imgs_count = read_imgs(input_path, to_read_imgs_list)

# таблица данных об обработанных изображениях
imgs_datatable = {'time': [], 'mins': [], 'dist': []}

for index, img_data in enumerate(imgs):
    delta_time, last_time = calc_delta_time(dev_timer, last_time)
    start_img, [[degs, mins], [img_height, img_width], img_time] = img_data

    dist, angle, img = [None for i in range(3)]

    try:
        dist, angle, img = calc_dist(start_img)
    except:
        print('Something wrong in a detection!')
        continue

    imgs_datatable['time'].append(time.asctime(img_time))
    imgs_datatable['mins'].append(degs * 60.0 + mins)
    imgs_datatable['dist'].append(dist)

    if is_dev:
        angle_to_log = round(math.degrees(angle), 2)
        dist_to_log = round(dist, 2)

        cv2.imwrite(os.path.join(output_path, f'{index}.jpg'), img)
        print_img_info(
            index,
            degs, mins,
            img_time,
            dist_to_log, angle_to_log,
            delta_time
        )

print_end_info(dev_timer())

# вывод таблицы в csv
output_dataframe = pd.DataFrame(
    imgs_datatable, columns=['time', 'mins', 'dist'])
output_dataframe.to_csv(output_path_csv, index=False)
