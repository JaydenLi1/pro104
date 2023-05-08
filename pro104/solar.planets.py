import cv2


img = cv2.imread('G:/Coding/python/pro104/solar-system.jpg')
cv2.putText(img, "Sun", (110, 100),
            cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 255))
cv2.putText(img, "Mercury", (130, 180),
            cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Venus", (190, 255),
            cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Earth", (290, 265),
            cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Mars", (380, 255),
            cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))
cv2.putText(img, "Jupiter", (450, 115),
            cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 255, 255))
cv2.putText(img, "Saturn", (750, 115),
            cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 255, 255))
cv2.putText(img, "Uranus", (950, 115),
            cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 255, 255))
cv2.putText(img, "Neptune", (1100, 115),
            cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 255, 255))
cv2.imshow('Dusplay Image', img)

cv2.imwrite("Solar_systemwithname.jpg", img)
cv2.waitKey(0)
