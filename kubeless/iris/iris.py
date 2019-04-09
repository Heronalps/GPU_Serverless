import numpy, time
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score, KFold, train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn import datasets

def handler(event, context):
    start = time.time()
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target

    # Because KFold cross-validation is used, the split is not necessary in this case.
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
    
    estimator = KerasClassifier(build_fn=baseline_model, epochs=20, batch_size=5, verbose=0)
    kfold = KFold(n_splits=10, shuffle=True, random_state=123)
    results = cross_val_score(estimator, x, y, cv=kfold)
    return "Accuray: {0} ({1}) Total time: {2}".format(results.mean()*100, results.std()*100, time.time() - start)

def baseline_model():
    model = Sequential()
    model.add(Dense(8, input_dim=4, activation='relu'))
    model.add(Dense(3, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

if __name__ == "__main__":
    handler({}, {})
