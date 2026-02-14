import cv2
import mediapipe as mp
import os

print("--- System Diagnostics ---")
print(f"Mediapipe File Location: {mp.__file__}")

# Check if the solutions folder actually exists
base_path = os.path.dirname(mp.__file__)
solutions_path = os.path.join(base_path, 'solutions')
print(f"Checking for solutions folder at: {solutions_path}")
print(f"Does it exist? {os.path.exists(solutions_path)}")

print("\n--- Testing Imports ---")
try:
    from mediapipe.solutions import hands
    print("✅ SUCCESS: Standard import worked!")
except Exception as e:
    print(f"❌ Standard failed: {e}")

try:
    import mediapipe.python.solutions.hands as hands
    print("✅ SUCCESS: Internal import worked!")
except Exception as e:
    print(f"❌ Internal failed: {e}")