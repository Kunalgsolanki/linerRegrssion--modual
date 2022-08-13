

import  numpy as np

# arry1 = np.array([[2,3,4],
#                   [3,4,6],
#                  ])
# kgs=arry1.sum(axis=1)  # addition row wise
#  # if x=10 addition as  row wise
#
# print(kgs)
# arry2 = np.array([[23,4,1],
#                   [3,4,0]])
# # for the dot product
# print(arry2.dot(arry1.transpose()))
# # print(len(dir(np)))
# arry3 = np.array([[2,3,2],
#                   [3,3,5]])
# print(arry3.transpose())
# # for the crosss product
# e = np.cross(arry3,arry1)
# print(e)
# ad = np.cross(arry1,arry2)
# print(ad)
#
# # shortyng
#
#
# arry3 = np.array([[2,3,2],
#                   [3,3,5]])
# sd=np.sort(arry3)
# print(sd)
#
# arry2 = np.array([[23,4,1],
#                   [3,4,0]])
# op= np.sort(arry2)
#
# print(op)
# ol = np.sort(arry2,axis=0)
# print(ol)
#
# # [[ 3  4  0]
# #  [23  4  1]]
#
# ol = np.sort(arry2,axis=1,kind='quiksort')
# print(ol)

# [[ 1  4 23]
#  [ 0  3  4]]

# reshape
#
# b= np.array([2,3,5,6,1,1,5,1,4,2,1,1,5,7,3,1,41,3,5,4,2,1,4,1])
# print(b.reshape(4,6))

#argshot  with type of index elemennt use for sort function
b = np.array([2,3,5,6,1,1,5,1,4,2,1,1,5,7,3,1,41,3,5,4,2,1,4,1])

print(np.argsort(b))
#argmin funtion
# b = np.array([2,3,5,6,1,1,5,1,4,2,1,1,5,7,3,1,41,3,5,4,2,1,4,1])
# print(np.argmin(b))
# [11 21 15 10  7 23  4  5  0  9 20  1 17 14 22 19  8 12  2 18  6  3 13 16]
# 4
#a argmax
#
# print(np.argmax(b,axis=0))

# [11 21 15 10  7 23  4  5  0  9 20  1 17 14 22 19  8 12  2 18  6  3 13 16]
# 16

b = np.array([2,3,5,6,1,1,5,1,4,2,1,1,5,7,3,1,41,3,5,4,2,1,4,1])
b= b.reshape(8,3)





















