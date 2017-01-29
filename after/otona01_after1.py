#coding:utf-8

def Step(z):
    if z >= 0:
        return 1
    else:
        return 0


def AND(x1, x2):
    
    w1 =  0.75 #ここに数値を入れる
    w2 =  0.75 #ここに数値を入れる
    b  =  -1.0 #ここに数値を入れる
    
    a = w1*x1 + w2*x2 + b
    y = Step(a)

    return y

# main関数
if __name__ == '__main__':
    
    # 入力４パターン
    list_of_x1_x2 =[
        [0, 0],
        [1, 0],
        [0, 1],
        [1, 1],
    ]
    
    print('ANDの結果')
    
    for x1, x2 in list_of_x1_x2:
        y = AND(x1, x2)
        print("%d %d | %d" % (x1, x2, y))
