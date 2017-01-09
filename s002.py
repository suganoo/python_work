# -*- coding: utf-8 -*-

from Queue import Queue
# 定数
start_pos_x = -1
start_pos_y = -1
cul = 0
row = 0

map = []
past_map = []
mv_len = 0

# 移動用リスト
# 上 下 左 右
next_mv_x = [1, 0, -1, 0]
next_mv_y = [0, 1, 0, -1]

def input():
        global start_pos_x
        global start_pos_y

        global past_map

        # 入力1行目
        input_lines = raw_input()
        input_lines_arry = input_lines.split(" ")

        # 入力1行目の縦列 横列のサイズ取得
        global cul
        global row
        cul = int(input_lines_arry[0])
        row = int(input_lines_arry[1])

        # すでに通ったmap を-1埋め
        past_map = [[-1 for i in range(cul)] for j in range(row)]

        # start goal位置を取得
        for i in range(row):
                row_arr = raw_input().split(" ")

                map.append(row_arr)

                # start 位置取得
                for i_s in range(len(row_arr)):
                        if (row_arr[i_s] == 's'):
                                start_pos_x = int(i_s)
                                start_pos_y = int(i)
                                break

def searchkeiro(x ,y):
        # 幅優先探索のキュー
        q=Queue()

        # スタートの状態をキューに格納
        q.put([start_pos_x,start_pos_y])

        # まずスタート地点の距離は0
        past_map[start_pos_y][start_pos_x] = 0

        # キューが空になるまでループ
        while not q.empty():

                # 取り出す
                pos = q.get()
                pos_x = pos[0]
                pos_y = pos[1]

                # 移動可能のセルに移動する
                for i in range(len(next_mv_x)):
                        next_pos_x = pos_x + next_mv_x[i]
                        next_pos_y = pos_y + next_mv_y[i]

                        if 0 <= next_pos_x and \
                                0 <= next_pos_y and \
                                next_pos_x < cul and \
                                next_pos_y < row and \
                                past_map[next_pos_y][next_pos_x] == -1 and \
                                map[next_pos_y][next_pos_x] != '1':

                                if map[next_pos_y][next_pos_x] == 'g':
                                        return (past_map[pos_y][pos_x] + 1)

                                q.put([next_pos_x,next_pos_y])
                                past_map[next_pos_y][next_pos_x] = past_map[pos_y][pos_x] + 1

        return -1


if __name__ == "__main__":
        input()
        dist = searchkeiro(start_pos_x, start_pos_y)
        if ( 0 < dist):
                print dist
        else:
                print "Fail"


