import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import numpy as np

# Setup Camera and Detector
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.8)
screen_w, screen_h = pyautogui.size()

while True:
    success, img = cap.read()
    if not success: break
    img = cv2.flip(img, 1)

    # --- THIS PART WAS MISSING OR MISPLACED ---
    # This line creates the 'hands' variable
    hands, img = detector.findHands(img, flipType=False)
    # ------------------------------------------

    if hands:
        lmList = hands[0]['lmList']
        x1, y1 = lmList[8][0], lmList[8][1] # Index Finger
        x2, y2 = lmList[12][0], lmList[12][1] # Middle Finger

        # Mapping to screen
        cv2.rectangle(img, (100, 100), (540, 380), (255, 0, 255), 2)
        mouse_x = np.interp(x1, (100, 540), (0, screen_w))
        mouse_y = np.interp(y1, (100, 380), (0, screen_h))

        # Movement
        pyautogui.moveTo(mouse_x, mouse_y, _pause=False)

        # Clicking (Pinch distance)
        length, info, img = detector.findDistance(lmList[8][:2], lmList[12][:2], img)
        if length < 40:
            pyautogui.click()
            cv2.circle(img, (info[4], info[5]), 15, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()