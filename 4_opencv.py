import cv2
import numpy as np
import sys
img = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', cv2.IMREAD_COLOR)


if img is None or img1 is None:
    print('image read failed')
    sys.exit()

print('img type = ', type(img))
print('img type = ', type(img1))

print('img dimension = ', img.shape)
print('img dimension = ', img1.shape)

print('data type = ', img.dtype)
print('data type = ', img1.dtype)


cv2.imshow('image', img)
cv2.imshow('image1', img1)

cv2.waitKey()
cv2.destroyAllWindows()
img = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', cv2.IMREAD_GRAYSCALE)
# img1 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', cv2.IMREAD_COLOR)


if img is None or img1 is None:
    print('image read failed')
    sys.exit()


print('img dimension = ', img.shape)
# print('img dimension = ', img1.shape)


h, w = img.shape[:2]
print('img size = {} * {}'.format(w, h))

cv2.imshow('image', img)
# cv2.imshow('image1', img1)

cv2.waitKey()
cv2.destroyAllWindows()
img = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', cv2.IMREAD_COLOR)
# img1 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', cv2.IMREAD_COLOR)


if img is None or img1 is None:
    print('image read failed')
    sys.exit()


print('img dimension = ', img.shape)
# print('img dimension = ', img1.shape)


h, w = img.shape[:2]
print('img size = {} * {}'.format(w, h))

cv2.imshow('image', img)
# cv2.imshow('image1', img1)

cv2.waitKey()
cv2.destroyAllWindows()
## 픽셀값 참고
img1 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 1)
img2 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 0)

if img is None:
    print('image read failed')
    sys.exit()
    
h, w = img.shape[:2]

img1_center = img1[h//2, w//2]
print(img1_center)
# [ 0 14 40] BGR 값 나옴
img2_center = img2[h//2, w//2]
print(img2_center)
# 20    
    
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.waitKey()

cv2.destroyAllWindows()
## 픽셀값 참고
img1 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 1)
img2 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 0)

if img is None:
    print('image read failed')
    sys.exit()
    
x = 120
y = 320

img1_center = img1[y, x]
print(img1_center)
# [194 198 209] BGR 값 나옴
img2_center = img2[y, x]
print(img2_center)
# 201    
    
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.waitKey()

cv2.destroyAllWindows()
## 픽셀값 참고
img1 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 1)
img2 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 0)

if img is None:
    print('image read failed')
    sys.exit()
    
# img1[10:110, 100:200] = 255 # 하얀색 상자
# img1[10:110, 100:200] = 1 # 검정색 상자
# img1[10:110, 100:200] = (0, 0, 255) # 빨간색 상자 (BGR 순서)
# img1[10:110, 100:200] = (0, 255, 0) # 초록색 상자 (BGR 순서)
# img1[10:110, 100:200] = (255, 0, 0) # 파란색 상자 (BGR 순서)
img1[10:110, 100:200] = (0,255,0)
img2[10:110, 100:200] = 128

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.waitKey()

cv2.destroyAllWindows()
img1 = np.zeros((240, 320, 3), dtype=np.uint8)
img2 = np.ones((240, 320, 3), dtype=np.uint8)
img3 = np.full((240, 320, 3), 255, dtype=np.uint8)
img4 = np.random.randint(0,255, size = (240,320), dtype=np.uint8)

img1[10:60, 10:60] = (0, 0, 255)
# img2[10:60, 10:60] = 255

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)


cv2.waitKey()
cv2.destroyAllWindows()
## 영상 복사

img = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/cat.bmp')

if img is None:
    print('image read failed')
    sys.exit()
    
img1 = img

cv2.imshow('image', img)
cv2.imshow('image1', img1)


while True:
    if cv2.waitKey(20) == 27:
        break
        
cv2.destroyAllWindows()
## 영상 복사

img = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/cat.bmp')

if img is None:
    print('image read failed')
    sys.exit()
    
img1 = img
img2 = img.copy()

img[100:200, 200:300] = (0,0,255)

cv2.imshow('image', img)
cv2.imshow('image1', img1)
cv2.imshow('image2', img2)


while True:
    if cv2.waitKey(20) == 27:
        break
        
cv2.destroyAllWindows()
## 영상 복사

image = np.ones((400, 400, 3), dtype = np.uint8) * 255

img1 = image.copy()

# circle(img, center, radius, color[, thickness[, lineType[, shift]]])
cv2.circle(image, (100, 200), 100, (0, 0, 255), 3, cv2.LINE_AA)

cv2.imshow('image', image)

cv2.waitKey()
cv2.destroyAllWindows()
img1 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_1_Opencv_Intro/fig/puppy.bmp')

print(img1.shape)
img1 = img1[100:250, 400:500]

cv2.imshow('img', img1)

cv2.waitKey()
cv2.destroyAllWindows()
img1 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_1_Opencv_Intro/fig/puppy.bmp')

img2 = img1[200:400, 300:500]
img3 = img1[200:400, 300:500].copy()

cv2.circle(img2, (110, 90), 50, (0, 0, 250), -1) # -1 이면 원 안의 색이 가득 색칠해짐

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)


cv2.waitKey()
cv2.destroyAllWindows()
## copyTO

src = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('image read failed')
    sys.exit()
    
# dst = cv2.copyTo(src, mask, dst = None)
dst = cv2.copyTo(src, mask, dst)    
    
cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()
##
src = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/airplane.bmp', cv2.IMREAD_COLOR)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(src_gray, 160, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)
cv2.imshow('mask', mask)


cv2.waitKey()
cv2.destroyAllWindows()
img1 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/cow.png')
img2 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/green.png')
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img1_gray, 190, 255, cv2.THRESH_BINARY_INV)
new = cv2.copyTo(img1, mask, img2)

cv2.imshow('mask', mask)
cv2.imshow('new', new)
# cv2.imshow('img2', img2)

cv2.waitKey()
cv2.destroyAllWindows()
img1 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/cow.png')
img2 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/green.png')
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


h, w = img1.shape[:2]
img2 = cv2.resize(img2, (w, h), interpolation=cv2.INTER_AREA)


ret, mask = cv2.threshold(img1_gray, 240, 255, cv2.THRESH_BINARY_INV)

cv2.copyTo(img1, mask, img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('mask', mask)


cv2.waitKey()
cv2.destroyAllWindows()


