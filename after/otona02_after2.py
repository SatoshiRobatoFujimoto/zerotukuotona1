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
    
    # output(XOR)
    list_of_1output = [
        [0],
        [1],
        [1],
        [0],
    ]
    
    # W1 = [
    #     [-0.75, 1.5],
    #     [-0.75, 1.5],
    # ]
    # b1 = [1, -1]
    
    # W2 = [[0.75], [0.75]]
    # b2 = [-1]

    W1 = np.random.rand(2,2) - 0.5
    b1 = np.random.rand(2) - 0.5
    W2 = np.random.rand(2,1) - 0.5
    b2 = np.random.rand(1) - 0.5
    
    # list_of_4input  = np.array(list_of_4input)
    # list_of_1output = np.array(list_of_1output)

    # W1 = np.array(W1) * 100
    # b1 = np.array(b1) * 100
    # W2 = np.array(W2) * 100
    # b2 = np.array(b2) * 100

    # 重みを List -> numpyのarray にする
    W1 = np.array(W1)
    b1 = np.array(b1)
    W2 = np.array(W2)
    b2 = np.array(b2)
    
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
    model.fit(list_of_4input, list_of_1output, nb_epoch=10000, batch_size=10)

    # 評価
    # scores = model.evaluate(list_of_4input, list_of_1output, verbose=0)
    # print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
    
    # 予測
    predictions = model.predict(list_of_4input)
    
    print('predictions')
    print predictions
    
    # 学習したネットワークの重みを保存
    weights1 = dense1.get_weights()
    weights2 = dense2.get_weights()
    
    W1 = np.array(weights1[0])
    b1 = np.array(weights1[1])
    W2 = np.array(weights2[0])
    b2 = np.array(weights2[1])
    
    print('W1')
    print W1
    print('b1')
    print b1
    print('W2')
    print W2
    print('b2')
    print b2
    
    np.savetxt('W1.csv', W1, delimiter=',')
    np.savetxt('b1.csv', b1, delimiter=',')
    np.savetxt('W2.csv', W2, delimiter=',')
    np.savetxt('b2.csv', b2, delimiter=',')
