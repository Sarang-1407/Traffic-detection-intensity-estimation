import cv2
import numpy as np

points = []
quadrilaterals = []

def draw_polygon(event, x, y, flags, param):
    global points, quadrilaterals

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)

        if len(points) == 4:
            quadrilaterals.append(points.copy()) 
            cv2.polylines(img, [np.array(points)], isClosed=True, color=(255, 0, 0), thickness=2)
            points = [] 

        cv2.imshow('Image', img)
        

img = cv2.imread('D:\\vehicle detection dataset\\Vehicle_Detection_Image_Dataset\\sample_image1.png')

img = cv2.resize(img, (1280, 720))


cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_polygon)

while True:
    cv2.imshow('Image', img)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    if len(quadrilaterals) == 2:
        print("Two quadrilaterals have been drawn.")
        break

cv2.destroyAllWindows()

for i, quad in enumerate(quadrilaterals):
    print(f"Coordinates of quadrilateral {i+1}: {quad}")
