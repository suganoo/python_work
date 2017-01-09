# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_lines = raw_input()
input_lines_arry = input_lines.split(" ")

max_x = int(input_lines_arry[1])
max_y = int(input_lines_arry[0])

map = max_y * [0]
for i in xrange(int(max_y)):
        s = list(raw_input().rstrip())
        map[i] = s

# position
# first
pos_x = 0
pos_y = 0

# next move distance
move_x = 1
move_y = 0

move_count = 0
while 0 <= pos_x and 0 <= pos_y and pos_x < max_x and pos_y < max_y:
        if map[pos_y][pos_x] == '\\':
                tmp = 0
                tmp = move_y
                move_y = move_x
                move_x = tmp

        elif map[pos_y][pos_x] == '/':
                tmp = 0
                tmp = move_y
                move_y = -1 * move_x
                move_x = -1 * tmp

        pos_y += move_y
        pos_x += move_x

        move_count += 1

print move_count
