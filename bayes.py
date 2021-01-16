from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix


def bayes(train_inputs, test_inputs, train_classes, test_classes):
    # trenowanie drzewa na zbiorze treningowym
    gnb = GaussianNB()
    gnb.fit(train_inputs, train_classes)

    # ewaluacja klasyfikatora
    score = gnb.score(test_inputs, test_classes)

    # macierz błędu
    y_pred = gnb.predict(test_inputs)
    cm = confusion_matrix(test_classes, y_pred)

    return score, cm
