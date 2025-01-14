import cv2


cap = cv2.VideoCapture('http://192.168.0.6:4747/video')

while True:
    ret, frame = cap.read() # read frame/image one by one
    resized = cv2.resize(frame, (600,400))
    cv2.imshow("Frame", resized) # display frame/image

    key = cv2.waitKey(1)  # wait until key press
    if key == ord("q"):  # exit loop on 'q' key press
        break

cap.release() # release video capture object
cv2.destroyAllWindows() # destroy all frame windows

