import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split


class disease_detector:
    train = pd.read_csv("assets/Training.csv")
    test = pd.read_csv("assets/Testing.csv")
    global ytest1

    def createcsv(self):
        self.train.drop(["Unnamed: 133"], axis=1, inplace=True)
        # self.train.columns = self.train.columns.str.replace('_', ' ')
        # print(self.train.head())

    def create_model(self,predictmatrix):
        P = self.train["prognosis"]
        X = self.train.drop(["prognosis"], axis=1)
        Y = self.test[X.columns]  # Use the columns from the training data
        xtrain, xtest, ytrain, ytest = train_test_split(X, P, test_size=0.2, random_state=42)

        # Train the model without using feature names
        rf = RandomForestClassifier(random_state=42)
        model_rf = rf.fit(xtrain, ytrain)

        # Predict using the test data
        y_predicted = model_rf.predict([predictmatrix])
        self.ytest1 = ytest
        return y_predicted

    def create_analytics(self, y_predicted):
        conf_mat = confusion_matrix(self.ytest1, y_predicted)
        df_cm = pd.DataFrame(conf_mat, index=self.train['prognosis'].unique(), columns=self.train['prognosis'].unique())
        print('F1-score% =', f1_score(self.ytest1, y_predicted, average='macro') * 100, '|', 'Accuracy% =',
              accuracy_score(self.ytest1, y_predicted) * 100)
        plt.figure(figsize=(10, 7))
        sns.heatmap(df_cm, annot=True)
        plt.xlabel('Predicted')
        plt.ylabel('Truth')
        plt.title('CONFUSION MATRIX')
        plt.show()
#
# a=disease_detector()
# a.createcsv()
# a.create_model()
# a.