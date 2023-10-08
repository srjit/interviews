

import numpy as np

score1 = [15,12,8,8,7,7,7,6,5,3] 
score2 = [10,25,17,11,13,17,20,13,9,15]


x_mean = np.mean(score1)
y_mean = np.mean(score2)

xs = np.array([(x1 - x_mean) for x1 in score1])
ys = np.array([(y1 - y_mean) for y1 in score2])

xs2 = np.array([(x1 - x_mean)**2 for x1 in score1])
ys2 = np.array([(y1 - y_mean)**2 for y1 in score2])

nr = xs.dot(ys)
dr = np.sqrt(np.sum(xs2)*np.sum(ys2))

print(nr/dr)


