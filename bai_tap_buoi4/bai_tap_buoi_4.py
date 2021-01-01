"""
Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
 Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp
 trong đó không có bài hát nào được lặp lại
 Example:
      Input: A = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
=> Output: 6 (vì chuỗi hình thành được là: [1, 2, 3, 7, 4, 5])
"""
# n = int(input('mời nhập chiều dài chuỗi: '))
# res = []
#
# for i in range (0,n):
#     ele = int(input('mời nhập số: '))
#     res.append(ele)
# res_1 = set(res)
# print(list(res_1))


'''
Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).
'''
# column_size_a = int(input("Enter size of column_a: "))
# row_size_a = int(input("Enter size of row_a: "))
# #matrx a
# a = []
# # value element of matrix
# b = []
# #Initialize the column.
# for j in range(0, column_size_a):
#     ele = int(input('mời nhập số: '))
#     b.append(ele)
# #Append the column to each row.
# for i in range(0, row_size_a):
#     a.append(b)
# #Printing the 2d created array
#
#
# column_size_b = int(input("Enter size of column_b: "))
# row_size_b = int(input("Enter size of row_b: "))
# #matrx a
# b = []
# # value element of matrix
# c = []
# #Initialize the column.
# for j in range(0, column_size_b):
#     ele = int(input('mời nhập số: '))
#     c.append(ele)
# #Append the column to each row.
# for i in range(0, row_size_b):
#     b.append(c)
# #Printing the 2d created array
# print('matrix a ',a)
# print('matrix b ',b)
# d = a*b




'''
Cho list các số nguyên dương A. Xây dựng chương trình đếm số lượng tập
gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.
Input: A = [0, 1, 2, 4, 7, 2, 3, 8]
Output: 4
  Vì: 4 lớn hơn 2 và 3 => có 2 cặp
        7 lớn hơn 2 và 3 => có 2 cặp
=> Tổng có 4 cặp thỏa mãn
'''
# A = [0, 1, 2, 4, 7, 2, 3, 8]
# b=A[3]
# print(b)


'''
Viết chương trình kiểm tra 2 list có phần tử chung hay không.
Input:
- List_1: [0, 1, 2, 3, 5, 6, 0, 2, 3, 10]
- List_2: [9, 8, 7, 10]
Output: True
'''
# lis_A = []
# lis_B = []
# leng_1 = int(input('số phần tử trong list A: '))
# for i in range (0,leng_1):
#     ele = int(input('mời nhập số: '))
#     lis_A.append(ele)
# leng_2 = int(input('số phần tử trong list B: '))
# for i in range (0,leng_2):
#     ele = int(input('mời nhập số: '))
#     lis_B.append(ele)
# print(lis_A)
# print(lis_B)
# A = 0 # nếu phần tử có thì gán 1
# for x in lis_A:
#     if x in lis_B:
#         A = 1
# if A == 1:
#     print('True')
# else:
#     print('False')

'''
Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
    Input: ["12341", "xyza", "am ma", "10928301", "xx", "1", "01001", "900" ]
Output: 4
'''
# lis_A = []
# coun = 0
# leng_1 = int(input('số phần tử trong list A: '))
# for i in range(0, leng_1):
#     ele = (input('mời nhập chuỗi: '))
#     lis_A.append(ele)
# print(lis_A)
# for i in  lis_A:
#     if len(i) > 2:
#         if i[0] == i[-1]:
#             coun = coun + 1
#             print(coun)
#     else:
#         print('Nhập kí tự lớn hơn 2 kí tự')

'''
Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list
Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
Input: [1, 2, 4, 5, 6, 7, 3, 2, 1, 4, 5, 1, 2, 3]
Output: 1
'''
# lis_A = []
# coun = 0
# leng_1 = int(input('số phần tử trong list A: '))
# for i in range(0, leng_1):
#     ele = (input('mời nhập chuỗi: '))
#     lis_A.append(ele)
# print(lis_A)
# for i in lis_A:
#     curr_fre = lis_A.count(i) # đếm từng giá trị
#     if curr_fre > coun:
#         coun = curr_fre
#         lis_A[0]= coun
# print(lis_A[0])

'''
Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.
Input:
 - List: [0, 1, 2, 3, 4, 9, 8, 7, 6]
 - n = 3
Output:
 - List_1: [0, 1, 2]
 - List_2: [3, 4, 9, 8, 7, 6]
'''
# lis_A = []
#
# leng_1 = int(input('số phần tử trong list A: '))
# for i in range(0, leng_1):
#     ele = int((input('mời nhập chuỗi: ')))
#     lis_A.append(ele)
# print(lis_A)
# n = int(input('index split character: '))
# var = lis_A[0:n]
# var_1 = lis_A[n::]
# print('lis_A: ',var)
# print('lis_B: ',var_1)

'''
Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
Input:
 - List: ["mot", "hai", "bon", "tam", "giac", "xyz abc"]
 - s: "$$"
Output: ["mot$$", "hai$$", "bon$$", "tam$$", "giac$$", "xyz abc$$"]
'''
# lis_A = []
#
# leng_1 = int(input('số phần tử trong list A: '))
# for i in range(0, leng_1):
#     ele = (input('mời nhập chuỗi: '))
#     lis_A.append(ele+'$$')
# print(lis_A)


'''
Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.
Input: [0, 1, 2, 3, 9, -5, -8, 3, 0, -1]
Output:
 - Max: 9
 - Min: -8
'''

# lis_A = []
# tong = 0
# leng_1 = int(input('số phần tử trong list A: '))
# for i in range(0, leng_1):
#     ele = int((input('mời nhập chuỗi: ')))
#     lis_A.append(ele)
# print(lis_A)
# print('Min: ',min(lis_A))
# print('Max: ',max(lis_A))
# for i in lis_A:
#     tong += i
# print('Sum_element_lis_A: ',tong)