from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score


def svm_f(train_inputs, test_inputs, train_classes, test_classes):
    model = svm.SVC()
    model.fit(train_inputs, train_classes)

    predictions = model.predict(test_inputs)
    scores = accuracy_score(test_classes, predictions)
    error = confusion_matrix(test_classes, predictions)

    return scores, error
