import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load 'data_df' from your CSV file
data_df = pd.read_csv('/home/kuladi03/Brain Tumor Project/Temporary Project/assets/data_df.csv')

# Define feature matrix X and target vector y
X = data_df[['corner_x', 'corner_y', 'width', 'height']]  # Features from 'data_df'
y = data_df['Tumor_Present']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree classifier
tree_model = DecisionTreeClassifier(random_state=42)

# Fit the model to the training data
tree_model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = tree_model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Decision Tree Accuracy:", accuracy)