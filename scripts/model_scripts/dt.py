import sys
import os
import yaml
import pickle
import pandas as pd
from catboost import CatBoostRegressor


if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython dt.py data-file model \n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("models", sys.argv[2])
os.makedirs(os.path.join("models"), exist_ok=True)


params = yaml.safe_load(open("params.yaml"))["train"]
p_random_seed = params["random_seed"]
p_iterations = params["iterations"]

# загружаем тренировочный датасет и разделяем признаки и метки
df = pd.read_csv(f_input)

X = df.iloc[:,[1,2,3]]
y = df.iloc[:,0]


model = CatBoostRegressor(iterations=p_iterations, random_seed=p_random_seed, loss_function='RMSE')
model.fit(X, y)

# Сохраняем обученную модель
with open(f_output, "wb") as fd:
    pickle.dump(model, fd)
