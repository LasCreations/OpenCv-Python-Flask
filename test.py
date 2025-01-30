import cv2
from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return ("Hello world, from Flask!")


"""
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() # read frame/image one by one
    resized = cv2.resize(frame, (600,400))
    cv2.imshow("Frame", resized) # display frame/image

    key = cv2.waitKey(1)  # wait until key press
    if key == ord("q"):  # exit loop on 'q' key press
        break

cap.release() # release video capture object
cv2.destroyAllWindows() # destroy all frame windows
"""

