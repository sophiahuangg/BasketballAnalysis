
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

file = "/Users/sophia/Desktop/Interview/testingdata.csv"
df = pd.read_csv(file)

arr = df.to_numpy()
print(arr)

all_data = arr[:, 1 : -1] # Only looks at DREB_DIFF column
print("ALL_DATA=", all_data)


all_labels = arr[:, -1] # Looks at win loss column 
all_labels=all_labels.astype(int)
#print("all_labels=", all_labels)

training_data, testing_data, training_labels, testing_labels = train_test_split(all_data, all_labels, train_size=0.20)
#print(training_data), evaluate model accuracy on 80% of data

#print(testing_data)
modeltype = LogisticRegression()
modeltype.fit(training_data, training_labels)
print(modeltype.predict(testing_data))
print(modeltype.score(testing_data, testing_labels)) #See how well our model does
