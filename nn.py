import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers.normalization import BatchNormalization
from keras.utils import np_utils
from sklearn.metrics import confusion_matrix


def nn(df, train_inputs, test_inputs, train_classes, test_classes):
    scaler = MinMaxScaler()
    scaler.fit(df)

    x_train = train_inputs
    x_test = test_inputs
    y_train = train_classes
    y_test = test_classes

    y_train = np_utils.to_categorical(y_train, num_classes=3)
    y_test = np_utils.to_categorical(y_test, num_classes=3)

    model = Sequential()
    model.add(Dense(1000, input_dim=len(df.columns)-1, activation='relu'))
    model.add(Dense(500, activation='relu'))
    model.add(Dense(300, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(3, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=20, epochs=10, verbose=1)

    prediction = model.predict(x_test)
    length = len(prediction)
    y_label = np.argmax(y_test, axis=1)
    predict_label = np.argmax(prediction, axis=1)

    accuracy = np.sum(y_label == predict_label) / length * 100

    cm = confusion_matrix(y_label, predict_label)

    return accuracy, cm
