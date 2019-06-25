# %% 3.6 손글씨 숫자 인식
import sys
import os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist


(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False, one_hot_label=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

# %% argmax(x, axis=1) 이해하기
import numpy as np
x = np.array([[0.1, 0.8, 0.1], [0.1, 0.8, 0.4], [0.1, 0.3, 0.6], [0.2, 0.3, 0.4]])
y = np.argmax(x, axis=1)
print(y)
