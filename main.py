import pandas as pd
from sklearn import model_selection
import matplotlib.pyplot as plt
from timeit import default_timer as timer

import desc
import data
import bayes
import dtree
import k_NN
import nn
import svm
import random_forest as rf


df = pd.read_csv('adult.csv', na_values=['?'])

df = data.prepare_data_to_visual(df)
# desc.statistic(df)
df = data.prepare_data(df)

print(df.head())

list_col = list(df.columns)
list_col.remove('class')
print(list_col)

all_inputs = df[list_col].values
all_classes = df['class'].values

(train_inputs, test_inputs, train_classes, test_classes) = model_selection.train_test_split(all_inputs,
                                                                                            all_classes,
                                                                                            train_size=0.7,
                                                                                            test_size=0.3)
print(train_inputs)
print(train_classes)
print(test_inputs)
print(test_classes)

# DRZEWA DECYZYJNE
start_tree = timer()
score_dtree, error_dtree = dtree.dtree(train_inputs, test_inputs, train_classes, test_classes)
end_tree = timer()

# NAIWNY BAYES
start_bayes = timer()
score_nbayes, error_nbayes = bayes.bayes(train_inputs, test_inputs, train_classes, test_classes)
end_bayes = timer()

# k-NN k = 3
start_knn3 = timer()
score_knn3, error_knn3 = k_NN.k_NN(3, train_inputs, test_inputs, train_classes, test_classes)
end_knn3 = timer()

# neural network
start_nn = timer()
score_nn, error_nn = nn.nn(df, train_inputs, test_inputs, train_classes, test_classes)
end_nn = timer()

# SVM
start_svm = timer()
score_svm, error_svm = svm.svm_f(train_inputs, test_inputs, train_classes, test_classes)
end_svm = timer()

# k-NN k = 5
start_knn5 = timer()
score_knn5, error_knn5 = k_NN.k_NN(5, train_inputs, test_inputs, train_classes, test_classes)
end_knn5 = timer()

# k-NN k = 7
start_knn7 = timer()
score_knn7, error_knn7 = k_NN.k_NN(7, train_inputs, test_inputs, train_classes, test_classes)
end_knn7 = timer()

# Random Forest
start_rf = timer()
score_rf, error_rf = rf.random_forest(train_inputs, test_inputs, train_classes, test_classes)
end_rf = timer()

# algs = ['dtree', 'nbayes', 'knn3', 'nn']
algs = ['dtree', 'nbayes', 'knn3', 'knn5', 'knn7', 'nn', 'svm', 'rf']
# scores = [score_dtree*100, score_nbayes*100, score_knn3*100, score_nn]
scores = [score_dtree*100, score_nbayes*100, score_knn3*100, score_knn5*100, score_knn7*100, score_nn,
          score_svm*100, score_rf*100]
# errors = [error_dtree, error_nbayes, error_knn3, error_nn]
errors = [error_dtree, error_nbayes, error_knn3, error_knn5, error_knn7, error_nn, error_svm, error_rf]
# times = [end_tree-start_tree, end_bayes-start_bayes, end_knn3-score_knn3, end_nn-start_nn]
times = [end_tree-start_tree, end_bayes-start_bayes, end_knn3-score_knn3, end_knn5-score_knn5, end_knn7-score_knn7,
         end_nn-start_nn, end_svm - start_svm, end_rf - start_rf]

plt.bar(algs, scores)
plt.title('Dokładność procentowa algorytmów')
plt.show()

plt.plot(algs, times)
plt.title('Czasy uzyskania rozwiązania przez badane algorytmy')
plt.show()

for error in errors:
    print(error)

print(scores)

