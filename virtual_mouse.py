import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
screen_width, screen_height = pyautogui.size()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1) # Flip for mirror effect
    hands, img = detector.findHands(img) # This draws the dots for you automatically

    if hands:
        # Get the first hand detected
        lmList = hands[0]['lmList'] # List of 21 Landmark points
        
        # Landmark 8 is the Index Finger Tip
        # lmList[8] gives us (x, y, z)
        x1, y1 = lmList[8][0], lmList[8][1]

        # Map camera coordinates to screen size
        # We use a smaller range [100, 500] to make it easier to reach corners
        mouse_x = cv2.np.interp(x1, [100, 540], [0, screen_width])
        mouse_y = cv2.np.interp(y1, [100, 380], [0, screen_height])

        pyautogui.moveTo(mouse_x, mouse_y)

    cv2.imshow("Janani's AI Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()