import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

# Load data
iris = load_iris()
x = iris.data
y = iris.target

# Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=1)
print("x_train shape:", x_train.shape)
print("x_test shape:", x_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# Scale
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Train
log_reg = LogisticRegression(max_iter=200)
log_reg.fit(x_train, y_train)

# Evaluate
y_pred = log_reg.predict(x_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Predict new samples
sample = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [6.2, 3.4, 5.4, 2.3],
    [5.9, 3.0, 4.2, 1.5]
])

sample = scaler.transform(sample)
preds = log_reg.predict(sample)
pred_species = [iris.target_names[p] for p in preds]

print("Predictions:", pred_species)

# custom dataset through pandas
import pandas as pd

# making data frame
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
print(df.head(10))

# label encoding
from sklearn.preprocessing import LabelEncoder

categorical_feature = ['cat', 'dog', 'dog', 'cat', 'bird']

encoder = LabelEncoder()

encoded_feature = encoder.fit_transform(categorical_feature)

print("encoded feature:", encoded_feature)

# one-hot encoding
from sklearn.preprocessing import OneHotEncoder
import numpy as np

categorical_feature = ['cat', 'dog', 'dog', 'cat', 'bird']

categorical_feature = np.array(categorical_feature).reshape(-1,1)

encoder = OneHotEncoder(sparse_output=False)

encoded_feature = encoder.fit_transform(categorical_feature)

print("OneHotEncoded feature:\n", encoded_feature)

