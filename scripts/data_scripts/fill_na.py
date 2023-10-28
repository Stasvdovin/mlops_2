import sys
import os
import pandas as pd

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 fill_na.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
os.makedirs(os.path.join("data", "stage1"), exist_ok=True)

# забираем датасет для обработки
df = pd.read_csv(f_input)

# Удалим дубликаты
df = df.drop_duplicates()
df = df.reset_index(drop=True)

# Почистим данные
question_dist = df[(df.Year <2021) & (df.Distance < 1100)]
df = df.drop(question_dist.index)
question_dist = df[(df.Distance > 1e6)]
df = df.drop(question_dist.index)
question_engine = df[df["Engine_capacity(cm3)"] < 200]
df = df.drop(question_engine.index)
question_engine = df[df["Engine_capacity(cm3)"] > 5000]
df = df.drop(question_engine.index)
question_price = df[(df["Price(euro)"] < 101)]
df = df.drop(question_price.index)
question_price = df[df["Price(euro)"] > 1e5]
df = df.drop(question_price.index)
question_year = df[df.Year < 1971]
df = df.drop(question_year.index)
df = df.reset_index(drop=True)

# Список имён колонок с числовыми и категориальными значениями
num_columns = list(df.select_dtypes(include='number').columns)
cat_columns = list(df.select_dtypes(exclude='number').columns)

df[num_columns] = df[num_columns].fillna(0)
df[cat_columns] = df[cat_columns].fillna("")

df.to_csv("data/stage1/train.csv", index=False)
