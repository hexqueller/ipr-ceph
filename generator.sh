#!/bin/bash

# Размер файла в байтах (1 ГБ = 1,073,741,824 байта)
FILE_SIZE=1073741824

# Генерация случайного имени файла
RANDOM_FILE_NAME=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1).dat

# Создание файла с заданным размером
dd if=/dev/zero of=$RANDOM_FILE_NAME bs=1 count=$FILE_SIZE