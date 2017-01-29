#coding:utf-8

import numpy as np
from keras.models import Sequential
from keras.layers import Dense


# データセットのロード
dataset = np.loadtxt("pima-indians-diabetes.csv", delimiter=",")

# 入力データとそれに対応する正解データを準備する
X = dataset[:,0:8]
Y = dataset[:,8]

# 重みの初期化
W1 = np.random.rand(8, 12) * 0.1 - 0.05
b1 = np.random.rand(12)    * 0.1 - 0.05
W2 = np.random.rand(12,8)  * 0.1 - 0.05
b2 = np.random.rand(8)     * 0.1 - 0.05
W3 = np.random.rand(8,1)   * 0.1 - 0.05
b3 = np.random.rand(1)     * 0.1 - 0.05

# モデルを作成
model = Sequential()

# モデルの各層を定義


# モデルの層を重ねる


# コンパイル
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 学習
model.fit(X, Y, nb_epoch=500, batch_size=10,  verbose=2)

# 予測
predictions = model.predict(X)

print predictions
