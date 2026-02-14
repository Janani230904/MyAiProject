import cv2
import mediapipe as mp

# We use the 'tasks' API which is the newer way for Python 3.12
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

print("Attempting to start camera...")
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Just show the camera feed for now to see if OpenCV is okay
    cv2.imshow('Janani Test Feed', image)
    
    if cv2.waitKey(5) & 0xFF == 27: # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()