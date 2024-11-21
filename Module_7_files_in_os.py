import os
import time

directory = os.getcwd()

for root, dirs, files in os.walk(directory):
    for file in files:
        file_name = file
        filepath = os.path.join(root, file)
        filetime = time.ctime(os.path.getmtime(file))
        formatted_time = time.strftime("%d.%m.%Y %H:%M")
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(root)


print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
      f'Родительская директория: {parent_dir}')




