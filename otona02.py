#coding:utf-8

import numpy as np

from keras.models import Sequential
from keras.layers import Dense


if __name__ == "__main__":
    
    # input
    list_of_4input = [
        [0,0],
        [1,0],
        [0,1],
        [1,1],
    ]
    
    # output
    list_of_1output = [
        [0],
        [1],
        [1],
        [0]
    ]
    
    W1 = [
        [-0.75, 1.5],
        [-0.75, 1.5],
    ]
    b1 = [1, -1]
    
    W2 = [[0.75], [0.75]]
    b2 = [-1]
    
    list_of_4input  = np.array(list_of_4input)
    list_of_1output = np.array(list_of_1output)
    W1 = np.array(W1) * 100
    b1 = np.array(b1) * 100
    W2 = np.array(W2) * 100
    b2 = np.array(b2) * 100
    
    # ニューラルネットワークの各層を定義
    dense1 = Dense(2, weights=[W1, b1], activation='sigmoid', input_dim=2) #relu
    dense2 = Dense(1, weights=[W2, b2], activation='sigmoid')
    
    # ニューラルネットワーク構築
    model = Sequential()
    model.add(dense1)
    model.add(dense2)

    # コンパイル
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # 学習
    # model.fit(list_of_4input, list_of_1output, nb_epoch=10, batch_size=10)

    # 評価
    # scores = model.evaluate(list_of_4input, list_of_1output, verbose=0)
    # print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
    
    # 予測
    predictions = model.predict(list_of_4input)
    
    print predictions
