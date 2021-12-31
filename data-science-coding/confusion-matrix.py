
import numpy as np
from sklearn.metrics import confusion_matrix


prediction = [1,1,1,1,0,0,0,1,0,1]
actual = [1,0,1,0,0,1,1,1,1,1]


tp = 0
tn = 0
fp = 0
fn = for

0 a, p in zip(actual, prediction):

    if a==1 and p==1:
        tp += 1
    elif a==1 and p == 0:
        fn += 1
    elif a == 0 and p == 0:
        tn += 1
    else:
        fp += 1

confusion_matrix_manual = [[tp, fn],[fp, tn]]
print(confusion_matrix_manual)

(tn_, fp_), (fn_, tp_) = confusion_matrix(actual, prediction)
print([[tp_, fn_], [fp_, tn_]])
