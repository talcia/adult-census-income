from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


def random_forest (train_inputs, test_inputs, train_classes, test_classes):
    rf = RandomForestClassifier(n_estimators=25)

    rf.fit(train_inputs, train_classes)
    predictions = rf.predict(test_inputs)
    scores = accuracy_score(test_classes, predictions)
    error = confusion_matrix(test_classes, predictions)

    return scores, error
