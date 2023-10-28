#!/usr/bin/python3

import pandas as pd

# скачиваем данные и сохраняем в папке raw

train = pd.read_csv('https://raw.githubusercontent.com/Stasvdovin/mlops_2/main/cars_moldova.csv')

train.to_csv("../../data/raw/train.csv", index=False)
