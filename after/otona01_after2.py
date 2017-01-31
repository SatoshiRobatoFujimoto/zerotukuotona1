#coding:utf-8

def Step(z):
    if z >= 0:
        return 1
    else:
        return 0

def AND(x1, x2):
    
    w1 = 0.75 #ここに数値を入れる
    w2 = 0.75 #ここに数値を入れる
    b  = -1.0 #ここに数値を入れる
    
    a = w1*x1 + w2*x2 + b
    y = Step(a)
    return y

def OR(x1, x2):
    
    w1 =  1.5 #ここに数値を入れる
    w2 =  1.5 #ここに数値を入れる
    b  = -1.0 #ここに数値を入れる
    
    a = w1*x1 + w2*x2 + b
    y = Step(a)
    return y

# ANDの符号反転したもの
def NAND(x1, x2):
    
    w1 = -0.75 #ここに数値を入れる
    w2 = -0.75 #ここに数値を入れる
    b  =  1.0  #ここに数値を入れる
    
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
    
    print('XOR')
    
    for x1, x2 in list_of_x1_x2:
        # ここにXOR回路を作ってみよう
        y_nand = NAND(x1, x2)
        y_or = OR(x1, x2)
        y = AND(y_nand, y_or)
        print("%d %d | %d" % (x1, x2, y))
    
    print('AND')
    
    for x1, x2 in list_of_x1_x2:
        y = AND(x1, x2)
        print("%d %d | %d" % (x1, x2, y))

    print('OR')
    
    for x1, x2 in list_of_x1_x2:
        y = OR(x1, x2)
        print("%d %d | %d" % (x1, x2, y))
    
    print('NAND')
    
    for x1, x2 in list_of_x1_x2:
        y = NAND(x1, x2)
        print("%d %d | %d" % (x1, x2, y))


