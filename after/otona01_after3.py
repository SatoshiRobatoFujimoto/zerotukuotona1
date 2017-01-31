#coding:utf-8

def Step(z):
    if z >= 0:
        return 1
    else:
        return 0

def AND(x1, x2):
    
    w1 =  7.139 #848709106445312e+00 #ここに数値を入れる
    w2 = -7.579 #839229583740234e+00 #ここに数値を入れる
    b  = -3.329 #003334045410156e+00 #ここに数値を入れる
    
    a = w1*x1 + w2*x2 + b
    y = Step(a)
    return y

def OR(x1, x2):
    
    w1 =  4.917 #499065399169922e+00 #ここに数値を入れる
    w2 =  4.917 #571067810058594e+00 #ここに数値を入れる
    b  = -7.434 #002876281738281e+00 #ここに数値を入れる
    
    a = w1*x1 + w2*x2 + b
    y = Step(a)
    return y

def NAND(x1, x2):
    
    w1 =  6.366 #593360900878906e+00 #ここに数値を入れる
    w2 =  6.367 #094039916992188e+00 #ここに数値を入れる
    b  = -2.853 #782415390014648e+00 #ここに数値を入れる
    
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
    
    # --- XOR ---
    
    print('XOR')
    
    for x1_x2 in list_of_x1_x2:
        x1 = x1_x2[0]
        x2 = x1_x2[1]
        
        # ここにXOR回路を作ってみよう
        y_nand = NAND(x1, x2)
        y_or = OR(x1, x2)
        y = AND(y_nand, y_or)
        
        print("%d %d | %d" % (x1, x2, y))
        
    
    print('AND')
    
    for x1_x2 in list_of_x1_x2:
        x1 = x1_x2[0]
        x2 = x1_x2[1]
        
        y = AND(x1, x2)
        
        print("%d %d | %d" % (x1, x2, y))

    print('OR')
    
    for x1_x2 in list_of_x1_x2:
        x1 = x1_x2[0]
        x2 = x1_x2[1]
        
        y = OR(x1, x2)
        
        print("%d %d | %d" % (x1, x2, y))
    
    print('NAND')
    
    for x1_x2 in list_of_x1_x2:
        x1 = x1_x2[0]
        x2 = x1_x2[1]
        
        y = NAND(x1, x2)
        
        print("%d %d | %d" % (x1, x2, y))
        
        