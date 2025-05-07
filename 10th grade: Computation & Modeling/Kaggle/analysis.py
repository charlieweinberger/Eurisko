import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# Read in the data
df = pd.read_csv('/home/runner/kaggle/data&libraries/dataset.csv')

# Filter to only the column's we're interested in
keep_cols = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin', 'Embarked']
df = df[keep_cols]

# process the columns
if True:

    df['Sex'] = df['Sex'].apply(lambda sex: 0 if sex == 'male' else 1) # sex

    age_nan = df['Age'].apply(lambda entry: np.isnan(entry)) # age
    age_not_nan = df['Age'].apply(lambda entry: not np.isnan(entry))
    df.loc[age_nan, ['Age']] = df['Age'][age_not_nan].mean()
  
    df['SibSp>0'] = df['SibSp'].apply(lambda x: 1 if x > 0 else 0) # sib
    df['Parch>0'] = df['Parch'].apply(lambda x: 1 if x > 0 else 0) # parch

    # cabinType
    df['CabinType'] = df['Cabin'].fillna('None').apply(lambda cabin: cabin[0] if cabin != 'None' else cabin)
 
    for cabin_type in df['CabinType'].unique():
        dummy_var_name = 'CabinType={}'.format(cabin_type)
        df[dummy_var_name] = df['CabinType'].apply(lambda entry: int(entry == cabin_type)) 

    # Embarked
    df['Embarked'] = df['Embarked'].fillna('None')

    for embarked in df['Embarked'].unique():
        dummy_var_name = 'Embarked={}'.format(embarked)
        df[dummy_var_name] = df['Embarked'].apply(lambda entry: int(entry == embarked))

    del df['Embarked']

# setting the dataframe with the right features

features_to_use = ['Sex', 'Pclass', 'Fare', 'Age', 'SibSp', 'SibSp>0', 'Parch>0', 'Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S', 'CabinType=A', 'CabinType=B', 'CabinType=C', 'CabinType=D', 'CabinType=E', 'CabinType=F', 'CabinType=G', 'CabinType=None', 'CabinType=T']
columns_needed = ['Survived'] + features_to_use
df = df[columns_needed]

# creating interaction terms

redundant_terms = [['SibSp', 'SibSp>0'], ['Embarked=C', 'Embarked=None', 'Embarked=Q', 'Embarked=S'], ['CabinType=A', 'CabinType=B', 'CabinType=C', 'CabinType=D', 'CabinType=E', 'CabinType=F', 'CabinType=G', 'CabinType=None', 'CabinType=T']]

for term_1 in features_to_use:
    for term_2 in features_to_use:

        if features_to_use.index(term_1) < features_to_use.index(term_2):

            interaction = term_1 + ' * ' + term_2
            redundant_list = [(term_1 in elem_list and term_2 in elem_list) for elem_list in redundant_terms]

            if not any(redundant_list):
                df[interaction] = df[term_1] * df[term_2]

# split into traiding/testing dataframe

df_train = df[:500]
df_test = df[500:]

arr_train = np.array(df_train)
arr_test = np.array(df_test)

y_train = arr_train[:,0]
y_test = arr_test[:,0]

x_train = arr_train[:,1:]
x_test = arr_test[:,1:]

max_iter = 100
regressor = LogisticRegression(max_iter=max_iter)
regressor.fit(x_train, y_train)

y_train_predictions = [int(output) for output in regressor.predict(x_train)]
y_test_predictions = [int(output) for output in regressor.predict(x_test)]

def get_accuracy(predictions, actual):
    correct = ['' for i in range(len(predictions)) if predictions[i] == actual[i]]
    return len(correct) / len(predictions)

print("\n", y_train_predictions)
print("\n", [int(elem) for elem in y_train])

print("\n", y_test_predictions)
print("\n", [int(elem) for elem in y_test])

print("\ntraining accuracy", round(get_accuracy(y_train_predictions, y_train), 4))
print("testing accuracy", round(get_accuracy(y_test_predictions, y_test), 4))

# columns_featured = df_train.columns[1:]
# coefficients_featured = regressor.coef_[0]
# constant_dict = {'Constant':regressor.intercept_[0]}
# coefficients = {columns_featured[n]:coefficients_featured[n] for n in range(len(columns_featured))}
# coefficients = constant_dict.update(coefficients)

# print("\ncoefficients:", {key:round(value, 4) for key, value in coefficients.items()})