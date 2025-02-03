import cv2

IMG_PATH = "data/Lenna_test_image.jpeg"

img = cv2.imread(IMG_PATH, cv2.IMREAD_COLOR)
cv2.imshow("Lenna", img)
cv2.waitKey(0)  # ожидание нажатия клавиши, иначе окно закроется сразу же
cv2.destroyAllWindows()  # закрытие всех окон
