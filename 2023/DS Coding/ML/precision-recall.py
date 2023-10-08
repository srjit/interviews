
import random
import numpy as np

# actual = [random.randint(0,1) for i in range(10)]
# predicted = [random.randint(0,1) for i in range(10)]

predicted = [1,1,1,1,0,0,0,1,0,1]
actual = [1,0,1,0,0,1,1,1,1,1]

# Actual = 1, Predicted = 1
tp = np.sum([1 for a,p in zip(actual, predicted) if a == p and a==1])
# Actual = 0, Predicted = 1
fp = np.sum([1 for a,p in zip(actual, predicted) if a != p and a==0])
# Actual = 0, Predicted = 0
tn = np.sum([1 for a,p in zip(actual, predicted) if a == p and a==0])
# Actual = 1, Predicted = 0
fn = np.sum([1 for a,p in zip(actual, predicted) if a != p and a==1])

# True positives /
precision = tp/(tp+fp)

# True positives / Actual positives
recall = tp/(tp+ fn)

print("Precision: ", precision)
print("Recall: ", recall)