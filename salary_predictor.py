import warnings
warnings.filterwarnings("ignore")
from sklearn.externals import joblib
model=joblib.load("salary_model.pk1")

exp=float(input("Enter job experience: "))

print("Expected salary: ",float(model.predict([[exp]])))