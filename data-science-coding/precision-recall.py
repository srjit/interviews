
import numpy as np
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score



def get_confusion_matrix(actual, prediction):

    tp = 0
    tn = 0
    fp = 0
    fn = 0
    
    for a_, p_ in zip(actual, prediction):

        if a_ == 1:
            if p_ == 1:
                tp += 1
            else:
                fp += 1
        elif a_ == 0:

            if p_ == 0:
                tn += 1
            else:
                fn += 1

    return [[tp, fn],[fp, tn]]
            
prediction = [1,1,1,1,0,0,0,1,0,1]
actual = [1,0,1,0,0,1,1,1,1,1]

confusion_matrix_coding = get_confusion_matrix(actual, prediction)
[[tn, fp], [fn, tp]] = confusion_matrix(actual, prediction)
confusion_matrix_sklearn = [[tp, fn],[fp, tn]]
print(confusion_matrix_coding)
print(confusion_matrix_sklearn)

_precision = tp/(tp+fp)
_recall = tp/(tp+fn)
_f_score = (2*_precision*_recall)/(_precision+_recall)


print(_precision, _recall, _f_score)
print(precision_score(actual, prediction),
      recall_score(actual, prediction),
      f1_score(actual, prediction))
