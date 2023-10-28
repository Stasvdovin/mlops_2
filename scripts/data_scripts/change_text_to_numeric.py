import sys
import os
import pandas as pd


if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 change_text_to_numeric.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
os.makedirs(os.path.join("data", "stage3"), exist_ok=True)

# забираем датасет для обработки
df = pd.read_csv(f_input)

# Удалим категориальные данные
df.drop(['Make',	'Model',	'Style',	'Fuel_type',	'Transmission'],
axis=1, inplace=True)


df.to_csv("data/stage3/train.csv", index=False)
