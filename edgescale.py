import cv2
fileName = "opencv/Unknown.jpeg"
try:
    image = cv2.imread(fileName)
    result = cv2.Canny(image,100,200)
    
    # write image back to disk
    cv2.imwrite("New Image.jpeg",result)

    cv2.imshow("New Image",result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except IOError:
    print("Error while reading files!")

