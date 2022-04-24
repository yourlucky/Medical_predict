from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import train_test_split
import copy
N_NEIGHBORS=20

class knnRegression:
    def __init__(self, data, x_col, y_col, margin, size):
        self.data = copy.deepcopy(data)
        self.x = self.data[x_col]
        self.y = self.data[y_col]
        self.margin = margin
        self.size = size
        self.regressor = KNeighborsRegressor(n_neighbors=N_NEIGHBORS)

    def runTest(self):
        x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, test_size=self.size)
        y_test.reset_index(drop=True, inplace=True)

        self.regressor.fit(x_train, y_train)
        y_pred = self.regressor.predict(x_test)
        correct = 0
        for i in range(0, len(y_test)):
            if abs(y_pred[i] - y_test[i]) <= self.margin:
                correct += 1
        print('Prediction accuracy for Testing data: ', correct/len(y_test)*100, ' %\n')