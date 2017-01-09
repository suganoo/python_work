# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_lines = int(raw_input())
for i in range(input_lines):
  s = raw_input().rstrip().split('.')
  judge = True
  for s_num in s:
      if len(s) != 4:
          judge = False
          break
      
      if s_num == '' :
          judge = False
          break
      
      if 255 < int(s_num) :
          judge = False
          break
      
      if int(s_num) < 0:
          judge = False
          break
      
  if judge == True :
      print judge
  else:
      print False
      

