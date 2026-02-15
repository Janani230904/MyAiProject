if hands:
        # Get the list of landmarks and the hand type (left or right)
        lmList = hands[0]['lmList']
        
        # 1. Coordinates for Index (8) and Middle (12) finger tips
        x1, y1 = lmList[8][0], lmList[8][1]
        x2, y2 = lmList[12][0], lmList[12][1]

        # 2. Draw the rectangle and map coordinates (same as before)
        cv2.rectangle(img, (100, 100), (540, 380), (255, 0, 255), 2)
        mouse_x = np.interp(x1, (100, 540), (0, screen_w))
        mouse_y = np.interp(y1, (100, 380), (0, screen_h))

        # 3. Move the mouse cursor
        pyautogui.moveTo(mouse_x, mouse_y, _pause=False)

        # 4. Check distance for CLICKING
        # findDistance calculates the pixels between two points
        length, info, img = detector.findDistance(lmList[8][:2], lmList[12][:2], img)

        # If the fingers are very close (less than 40 pixels), click!
        if length < 40:
            cv2.circle(img, (info[4], info[5]), 15, (0, 255, 0), cv2.FILLED)
            pyautogui.click()
            print("Click detected!")