# here first we import cv2  so that we can use computer vision.
import cv2
import winsound

# here we define cam variable and tell cv2 to captuer  video.
cam = cv2.VideoCapture(0)

# to captuer the video we have first see wheather cam is on or not.
while cam.isOpened():

    # here we define to frame so that we can see the difference.
    ret1, frame1 = cam.read()
    ret2, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    clr = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    
    # here passing (5,5) is cernel size and 0 is a sigma x. 
    blur = cv2.GaussianBlur(clr, (5, 5), 0)
    
    # here we passing 20 is min threshold 500 is max threshold , cv2.thresh_binary is threshold type...
    # threshold is use to remove the noise..
    _, noise = cv2.threshold(blur, 20, 500, cv2.THRESH_BINARY)
    
    # dilated is opposite of threshold...
    # with the help of threshold we remove the unwanted this so now we reamin with actually thing...
    # so here we make actully thing bigger with the help of dialation...
    dilated = cv2.dilate(noise, None)
    
    # contor is border of item which are moving...
    # cv2.retr_tree mode we can pass any mode...
    # cv2 chain method...
    con, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in con:
        
        # here we give the condition the thing smaller than 5000 cv2 will ignore it.
        if cv2.contourArea(c) < 5000:
            continue

        # x axis ,y axis , wight and high.
        x, y, w, h = cv2.boundingRect(c)

        # color fist one , 2 is thickness.
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        winsound.Beep(500, 200)

    # This line will shout down the camera when we presse d on keyboard.    
    if cv2.waitKey(10) == ord("d"):
        break

    cv2.imshow('Pranay Security Camera', frame1)

