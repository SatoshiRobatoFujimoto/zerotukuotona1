#coding:utf-8

def Step(z):
    
    return 0


def AND(x1, x2):
    
    y = 0
    
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

