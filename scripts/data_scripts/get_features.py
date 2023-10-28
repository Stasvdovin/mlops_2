import sys
import os
import io
import pandas as pd


if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 get_features.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
os.makedirs(os.path.join("data", "stage2"), exist_ok=True)

# забираем датасет для обработки
df = pd.read_csv(f_input)

# добавляем новый признак
df['Age'] = 2022 - df.Year
df['km_year'] = df.Distance/df.Age
question_km_year = df[df.km_year > 50e3]
df = df.drop(question_km_year.index)
question_km_year = df[df.km_year < 100]
df = df.drop(question_km_year.index)
df = df.reset_index(drop=True)


df.to_csv("data/stage2/train.csv", index=False)
