#coding:utf-8
import numpy as np

from keras.models import Sequential
from keras.layers import Dense

# データセットのロード
dataset = np.loadtxt("pima-indians-diabetes.csv", delimiter=",")

# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]

# 係数の初期化
W1 = np.random.rand(8, 12) * 0.1 - 0.05
b1 = np.random.rand(12)    * 0.1 - 0.05
W2 = np.random.rand(12,8)  * 0.1 - 0.05
b2 = np.random.rand(8)     * 0.1 - 0.05
W3 = np.random.rand(8,1)   * 0.1 - 0.05
b3 = np.random.rand(1)     * 0.1 - 0.05

# ニューラルネットワークの各層を定義
dense1 = Dense(12, weights=[W1, b1], activation='relu', input_dim=8)
dense2 = Dense( 8, weights=[W2, b2], activation='relu')
dense3 = Dense( 1, weights=[W3, b3], activation='sigmoid')

# ニューラルネットワーク構築
model = Sequential()
model.add(dense1)
model.add(dense2)
model.add(dense3)

# コンパイル
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 学習
model.fit(X, Y, nb_epoch=500, batch_size=10,  verbose=2)

# 予測
predictions = model.predict(X)

print predictions



