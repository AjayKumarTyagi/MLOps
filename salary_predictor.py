import warnings
warnings.filterwarnings("ignore")
from sklearn.externals import joblib
model=joblib.load("salary_model.pk1")
print("\t\t\tWelcome to Future Tools")
print("\t\t\t-----------------------\n")
while True:
    print("0. Exit program")
    print("1. Predict salary based on experience")
    choice=input("Enter your choice: ")
    if choice=="1":
        exp=float(input("Enter job experience: "))
        print("Expected salary: ",float(model.predict([[exp]])))
    elif choice=="0":
        exit()
    else:
        print("invalid choice")