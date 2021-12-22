


prediction = [1,1,1,1,0,0,0,1,0,1]
actual = [1,0,1,0,0,1,1,1,1,1]


tp = tn = fp = fn = 0

for actual, predicted in zip(prediction, actual):

    if actual == 0:
        if predicted == 0:
            tn += 1
        else:
            fp += 1

    else:
        if predicted == 1:
            tp += 1
        else:
            fn += 1


confusion_matrix = [[tp, fn], [fp, tn]]

print(confusion_matrix_manual)


print("Sensitivity:", tp/(tp+fn))
print("Specificity:", tp/(tp+fp))
            

            

            
