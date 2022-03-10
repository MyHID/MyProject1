import pickle
statement=input("enter the news to predict")
print("You entered"+str(statement))

def fake(var):
    load_model=pickle.load(open("E:\Python\model.sav","rb"))
    prediction=load_model.predict([var])
    #prob=load_model.predict_proba([var])
    return(print("Ststement is",prediction[0])),


fake(var)


