import time


def create_timer(begin_time): return lambda: round(time.time() - begin_time, 2)


def calc_delta_time(timer, last_time):
    current_time = timer()
    delta_time = round(current_time - last_time, 2)
    return delta_time, current_time
