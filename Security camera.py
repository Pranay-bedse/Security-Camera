
import cv2
import winsound

cam = cv2.VideoCapture(0)

while cam.isOpened():

    ret1, frame1 = cam.read()
    ret2, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    clr = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(clr, (5, 5), 0)
    _, noise = cv2.threshold(blur, 20, 500, cv2.THRESH_BINARY)
    dilated = cv2.dilate(noise, None)
    con, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in con:

        if cv2.contourArea(c) < 5000:
            continue

        x, y, w, h = cv2.boundingRect(c)

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        winsound.Beep(500, 200)

    if cv2.waitKey(10) == ord("d"):
        break

    cv2.imshow('Pranay Security Camera', frame1)

