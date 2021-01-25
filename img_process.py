import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import os 

# print(os.listdir('./image/'))
all_image_list = os.listdir('./image/') 
all_image_list = ['./image/'+i for i in all_image_list]
print(all_image_list)

img_list = []
for i in all_image_list: 
    img_list.append(cv2.imread(i))

edge_list = []
for i in img_list: 
    edge_list.append(cv2.Canny(i, 100, 150))

for i in range(len(edge_list)): 
    plt.figure()
    
    plt.imshow(edge_list[i], cmap='gray')
    plt.savefig(all_image_list[i]+'.png')

# plt.show()

# img = cv2.imread('./image/5.jpg')
# print(img.shape)


# # 顯示圖片
# cv2.imshow('My Image', img)

# edges = cv2.Canny(img,100,200)
# plt.imshow(edges, cmap='gray')
# plt.show()


# # 按下任意鍵則關閉所有視窗
# cv2.waitKey(0)
# cv2.destroyAllWindows()