from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix


def k_NN(k, train_inputs, test_inputs, train_classes, test_classes):
    # trenowanie drzewa na zbiorze treningowym
    knn = KNeighborsClassifier(k)
    knn.fit(train_inputs, train_classes)

    # ewaluacja klasyfikatora
    score = knn.score(test_inputs, test_classes)

    # macierz błędu
    y_pred = knn.predict(test_inputs)
    cm = confusion_matrix(test_classes, y_pred)

    return score, cm