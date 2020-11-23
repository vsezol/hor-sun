import os

is_dev = True

input_path = os.path.join(os.getcwd(), 'img', 'input')

output_path = os.path.join(os.getcwd(), 'img', 'out')
output_path_csv = os.path.join(output_path, 'out.csv')

to_read_imgs_list = [
    *os.listdir(input_path)
]

# символ, стоящий между градусами и минутами в названии файла
degs_mins_separator = 'x'
# если дата не поступает она рассчитывается автоматически
is_parsing_time = False