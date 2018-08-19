from sklearn import datasets
import tensorflow as tf
from scipy.spatial import distance
#from sklearn.neighbors import KNeighborsClassifier
from enum import Enum
from scipy.spatial import distance
import subprocess
import MachineLearningcsv as csvreadwrite

'''
the best way in which the check if the new element is of positive or negative. 

Remember that there can be issues of having false positive and false negatives, however that is usually down to data
'''
#euclidean distance A^2 + B^2 = C^2

#y = the target we are looking for e.g. spam/not-spam
#x = the label and features that we are using to determine the targets value


def euc(a,b):
    return distance.euclidean(a,b) #this figures out the distance of C^2

class ScrappyKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
    
    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions
    
    def closest (self, row):
        best_distance = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_distance:
                best_distance = dist
                best_index = i
        return self.y_train[best_index]

class flowertype(Enum):
    Setosa = 0
    Virginica = 1
    Versicolor = 2

iris = datasets.load_iris()

X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = .5)

#clf = KNeighborsClassifier()
clf = ScrappyKNN()

clf.fit(X_train, y_train)

output = clf.predict(X_test)

for val in output:
    emunType = flowertype(val)
    print(emunType)

from sklearn.metrics import accuracy_score

score = accuracy_score(y_test, output)

print("The accuracy score is: %s" % score)

#tensorflow allows graph creation
a = tf.constant(3.0, dtype=tf.float32)
b = tf.constant(4.0)
total = a+b

print(a)
print(b)
print(total)
print()
print("-------------------")

data = csvreadwrite.importdata()
result = getattr(data, "getcsvdata")


writer = tf.summary.FileWriter('.')
writer.add_graph(tf.get_default_graph())

