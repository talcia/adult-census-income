from sklearn import tree
from sklearn.metrics import confusion_matrix


def dtree(train_inputs, test_inputs, train_classes, test_classes):
    # trenowanie drzewa na zbiorze treningowym
    dtc = tree.DecisionTreeClassifier()
    clf = dtc.fit(train_inputs, train_classes)

    # ewaluacja klasyfikatora
    score = dtc.score(test_inputs, test_classes)

    # macierz błędu
    y_pred = dtc.predict(test_inputs)
    cm = confusion_matrix(test_classes, y_pred)

    return score, cm
