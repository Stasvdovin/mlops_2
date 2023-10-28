import yaml
import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split

params = yaml.safe_load(open("params.yaml"))["split"]
p_split_ratio = params["split_ratio"]
p_seed = params["seed"]


if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 train_test_split.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]

os.makedirs(os.path.join("data", "stage4"), exist_ok=True)

# забираем датасет для обработки
df = pd.read_csv(f_input)

X = df.drop(columns = ["Price(euro)"])
y = df["Price(euro)"]
features_names = df.drop(columns = ["Price(euro)"]).columns
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=p_split_ratio, random_state=p_speed)

pd.concat([X_train, y_train], axis=1).to_csv("data/stage4/train.csv", index=None)
pd.concat([X_test, y_test], axis=1).to_csv("data/stage4/test.csv", index=None)
