import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import streamlit as st
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


# Load the training and testing data
train_data = pd.read_csv('/workspaces/senseai/Training.csv')
test_data = pd.read_csv('/workspaces/senseai/Testing.csv')

# Select features and target variable for training data
X_train = train_data.drop(columns=['prognosis'])
y_train = train_data['prognosis']

# Select features and target variable for testing data
X_test = test_data.drop(columns=['prognosis'])
y_test = test_data['prognosis']

# Choose a machine learning algorithm (Random Forest Classifier)
rf_model = RandomForestClassifier(random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Evaluate the model
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Streamlit UI
st.title("SymptomSense: AI Health Diagnosis")

# Ask for symptoms from the user
symptoms = list(X_train.columns)
user_symptoms = st.multiselect("Select your symptoms:", symptoms)

# Convert user input into a DataFrame
user_data = pd.DataFrame({symptom: [1] if symptom in user_symptoms else [0] for symptom in symptoms})

# Predict disease based on user input
predicted_disease = rf_model.predict(user_data)

# Display the predicted disease to the user
st.subheader("Predicted Disease:")
st.write(predicted_disease[0])
# Data Visualization
st.subheader("Data Visualization")

# Countplot of predicted diseases in training data
plt.figure(figsize=(12, 6))
sns.countplot(data=train_data, x='prognosis')
plt.xticks(rotation=90)
plt.title("Distribution of Diseases in Training Data")
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)
# Bar plot of predicted diseases for user input
predictions = rf_model.predict_proba(user_data)[0]
predictions_df = pd.DataFrame({'prognosis': rf_model.classes_, 'Probability': predictions})
predictions_df = predictions_df.sort_values(by='Probability', ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(data=predictions_df, x='prognosis', y='Probability')
plt.xticks(rotation=90)
plt.title("Predicted Probabilities of Diseases for User Input")
st.pyplot()
#
# Confusion matrix
st.subheader("Confusion Matrix")

# Predictions on test data
y_pred = rf_model.predict(X_train)

# Compute confusion matrix
cm = confusion_matrix(y_train, y_pred)

#Plot confusion matrix
plt.figure(figsize=(12, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=rf_model.classes_, yticklabels=rf_model.classes_)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
st.pyplot()