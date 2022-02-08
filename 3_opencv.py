import numpy as np
import cv2
import sys
img = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 0)
# img_re = cv2.resize(img, (200, 150), interpolation=cv2.INTER_AREA)

if img is None:
    print('image read failed')
    
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)

while True:
    key = cv2/waitKey()
    if key == 27 or key == ord('q'):
        break
        
cv2.destroyAllWindows()
import matplotlib.pyplot as plt

imgBGR = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 1)
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.imshow(imgRGB, cmap = 'gray')
plt.axis('off')
plt.show()
import glob
img_list = glob.glob('../Ch_1_2_Opencv_basic/Ch_1_Opencv_Intro/fig/images/*.jpg')

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('img', cv2.WND_PROP_AUTOSIZE,
                     cv2.WINDOW_AUTOSIZE)
idx = 0
while True:
    img = cv2.imread(img_list[idx])

    cv2.imshow('img', img)
    
    if cv2.waitKey(3000) ==27:
        break
        
    idx += 1
    
    if idx >= len(img_list):
        idx = 0
    
cv2.destroyAllWindows()
    
img = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 1)

print(img.shape)

h, w = img.shape[:2]

print('image size = {} * {}'.format(w, h))
imgC = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 1)
imgG = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 0)


imgC[100:200, 200:300] = (0, 0, 255)
imgG[100:200, 200:300] = 127


cv2.imshow('img1', imgC)
cv2.imshow('img2', imgG)

cv2.waitKey()

cv2.destroyAllWindows()
img1 = np.zeros((400, 300, 3), dtype = np.uint8)
img2 = np.ones((400, 300, 3), dtype = np.uint8)*255
img3 = np.full((400, 300, 3), (0,0,255), dtype = np.uint8)
img4 = np.random.randint(0, 255, (400, 300), np.uint8)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)


cv2.waitKey()

cv2.destroyAllWindows()
img = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 1)

img1 = img
img2 = img.copy()

img[50:100, 100:300] = (0,255, 0)

cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)


cv2.waitKey()
cv2.destroyAllWindows()
img = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', 1)

img2 = img[200:400, 300:500]
cv2.circle(img2, (100, 100), 50, (0, 0, 255), -1)

cv2.imshow('img', img)
cv2.imshow('img2', img2)


cv2.waitKey()
cv2.destroyAllWindows()
src = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/airplane.bmp')
mask = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/mask_plane.bmp')
dst = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/field.bmp')

dst = cv2.copyTo(src, mask, dst)

# dst[mask > 0] = (0, 0, 255)

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)


cv2.waitKey()
cv2.destroyAllWindows()
## 송아지 합성

img1 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/cow.png')
img2 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/green.png')

h, w = img1.shape[:2]

img2_re = cv2.resize(img2, (w,h))
ret, mask = cv2.threshold(img1, 244, 255, cv2.THRESH_BINARY_INV)

cv2.copyTo(img1, mask, img2_re)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img2_re', img2_re)
cv2.imshow('mask', mask)

cv2.waitKey()
cv2.destroyAllWindows()
## 송아지 합성

img1 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/cow.png')
img2 = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/green.png')

h, w = img1.shape[:2]

# img2_re = cv2.resize(img2, (w,h))

img2_seg = img2[350:350+h, 200:200+w]

ret, mask = cv2.threshold(img1, 244, 255, cv2.THRESH_BINARY_INV)

cv2.copyTo(img1, mask, img2_seg)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img2_seg', img2_seg)
cv2.imshow('mask', mask)

cv2.waitKey()
cv2.destroyAllWindows()
src = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', cv2.IMREAD_COLOR)
img_alpha = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/imgbin_sunglasses_1.png', cv2.IMREAD_UNCHANGED)

if src is None or img_alpha is None:
    print('image read failed')
    sys.exit()
    
sunglass= img_alpha[:, :, 0:3]
mask = img_alpha[:,:,-1]

cv2.imshow('sunglass', sunglass)
cv2.imshow('mask', mask)

cv2.waitKey()
cv2.destroyAllWindows()
puppy = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', cv2.IMREAD_COLOR)
img_alpha = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/imgbin_sunglasses_1.png', cv2.IMREAD_UNCHANGED)

if puppy is None or img_alpha is None:
    print('image read failed')
    sys.exit()
    
h, w = puppy.shape[:2]

img_alpha_re = cv2.resize(img_alpha, (w,h))
ret, mask = cv2.threshold(img_alpha, 240, 350, cv2.THRESH_BINARY_INV)

cv2.copyTo(img_alpha, mask, puppy)

sunglass = img_alpha[:, :, 0:3]
mask = img_alpha[:,:,-1]

cv2.imshow('puppy', puppy)
cv2.imshow('img_alpha', img_alpha)
# cv2.imshow('img_alpha_re', 'img_alpha_re')
cv2.imshow('mask', mask)


cv2.waitKey()
cv2.destroyAllWindows()
src = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/puppy.bmp', cv2.IMREAD_COLOR)
img_alpha = cv2.imread('../Ch_1_2_Opencv_basic/Ch_2_Opencv_basic/fig/imgbin_sunglasses_1.png', cv2.IMREAD_UNCHANGED)

img_alpha = cv2.resize(img_alpha, (300, 150))

if src is None or img_alpha is None:
    print('image read failed')
    sys.exit()
    
sunglass= img_alpha[:, :, 0:3]
mask = img_alpha[:,:,-1]

h, w = mask.shape[:2]
crop = src[120:120+h, 220:220+w]

crop[mask > 0] = (255, 0, 255)

# cv2.copyTo(sunglass, mask, crop)

cv2.imshow('sunglass', sunglass)
cv2.imshow('mask', mask)
cv2.imshow('src', src)
cv2.imshow('crop', crop)


cv2.waitKey()
cv2.destroyAllWindows()
img = np.full((600, 1200, 3), 255, np.uint8)


cv2.line(img, (100, 50), (300, 50), (0, 0, 255), 10)
cv2.line(img, (300, 50), (150, 200), (0, 0, 255), 10)
cv2.arrowedLine(img, (400, 50), (400,250), (0,0,255), 10)

cv2.rectangle(img, (100, 300), (400, 400), (255,0,0), -1)
cv2.rectangle(img, (100, 300, 300, 100), (0,0,255), 10)

cv2.circle(img, (600, 300), 100, (255, 0, 255), 10, cv2.LINE_AA)


cv2.ellipse(img, (600, 300), (50, 100), 10, 0, 360, (0, 255, 0), 10)

text = 'Opencv version = ' + cv2.__version__
cv2.putText(img, text, (800, 100), cv2.FONT_HERSHEY_SIMPLEX, 
           0.8, (0,0,255), 1, cv2.LINE_AA)

cv2.imshow('canvas', img)

cv2.waitKey()
cv2.destroyAllWindows()
img = np.full((600, 1200, 3), 255, np.uint8)

cv2.circle(img, (150, 200), 100, (0, 0, 0), 10, cv2.LINE_AA)
cv2.line(img, (350, 80), (350, 300), (0, 0, 0), 10)
cv2.line(img, (150, 350), (150,500), (0, 0, 0), 10)
cv2.line(img, (150, 500), (360, 500), (0, 0, 0), 10)

cv2.line(img, (600, 100), (500, 250), (0,0,0), 10)
cv2.line(img, (600, 100), (700, 250), (0,0,0), 10)
cv2.line(img, (800, 100), (800, 300), (0,0,0), 10)
cv2.line(img, (800, 200), (900, 200), (0,0,0), 10)
cv2.rectangle(img, (500, 350, 300, 200), (0,0,0), 10)



cv2.imshow('canvas', img)

cv2.waitKey()
cv2.destroyAllWindows()
cap = cv2.VideoCapture(0)
# cap.isOpened()

if not cap.isOpened():
    print('Videocap open failed')
    sys.exit()
    
while True:
    ret, frame = cap.read()

    if not ret:
        print('video read failed')
        break
            
    cv2.imshow('img', frame)
    
    if cv2.waitKey(20) == 27:
        break
            
cap.release()
cv2.destroyAllWindows()
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Videocap open failed')
    sys.exit()
    
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)*0.7
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output_class.avi', fourcc, fps, (w,h))

while True:
    
    ret, frame = cap.read()

    if not ret:
        print('video read failed')
        break
            
    cv2.imshow('img', frame)
    
    out.write(frame)
    
    if cv2.waitKey(20) == 27:
        break


cap.release()
cv2.destroyAllWindows()
cap = cv2.VideoCapture('./fig/raining.mp4')

if not cap.isOpened():
    print('Videocap open failed')
    sys.exit() 
    
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS) * 0.5)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# print(w, h, fps, sep = ' / ')
 
out = cv2.VideoWriter('output_class.avi', fourcc, fps, (w, h))


while True:
    ret, frame = cap.read() # 영상을 받는다
    
    if not ret:
        print('Video read failed')
        break
            
    edge = cv2.Canny(frame, 50, 150) 
    
    cv2.imshow('img', frame) # 영상을 보여준다
    cv2.imshow('edge', edge)
    
    out.write(frame)
    
    
    if cv2.waitKey(20) == 27:
        break
        
            
cap.release()
out.release()
cv2.destroyAllWindows()

