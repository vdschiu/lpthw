# -*- coding: utf-8 -*-
x = "There are %d types of people." % 10 # 定義一個變數 x
binary = "binary" # 定義一個變數 binary
do_not = "don't" # 定義一個變數 do_not
y = "Those who know %s and those who %s." % (binary, do_not) # 定義一個變數 y
print x
print y
# 輸出 x 跟 y
print "I said: %r." % x
print "I also said: '%s'." % y
# 分別輸出把 x 跟 y 加進去的字串
hilarious = False # 定義一個變數 hilarious
joke_evaluation = "Isn't that joke so funny? %r" # 定義一個變數 joke_evaluation

print joke_evaluation % hilarious # 把 hilarious 塞進 joke_evaluation 這個「字串」，然後輸出

w = "This is the left side of..." # 定義一個變數 w (字串)
e = "a string with a right side." # 定義一個變數 e (字串)

print w + e # 把上述兩個定串連接在一起，然後輸出
# "+" 號可以把兩個字串結合在一起，但據說這樣效率很差，所以應該採用 .join() 這個method
print ''.join((w,e)) # 要注意 .join() 只能塞一個參數而已，所以要把超過一個參數用括號包起來
