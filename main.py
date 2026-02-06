import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# --- Configuration ---
SCROLL_SPEED = 100  # Amount to scroll per frame (Increased for snappiness)
pyautogui.PAUSE = 0 # Remove default 0.1s delay after each pyautogui call
pyautogui.FAILSAFE = False # Optional: prevent failsafe from stopping script if mouse hits corner

# --- Initialization ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

print("--- Hand Controlled Auto Scroll Ready ---")
print("1. Jari Telunjuk KE ATAS -> SCROLL UP")
print("2. Jari Jempol KE BAWAH   -> SCROLL DOWN")
print("Press 'q' to quit.")

def is_finger_up(landmarks, tip_idx, pip_idx):
    # Tip y < Joint y means pointing up
    return landmarks[tip_idx].y < landmarks[pip_idx].y

def is_thumb_down(landmarks):
    # Thumb Tip: 4, Thumb IP: 3
    # Tip y > Joint y means pointing down (Thumbs down)
    return landmarks[4].y > landmarks[3].y

try:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        image = cv2.flip(image, 1) # Selfie view
        h, w, _ = image.shape
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_image)

        status = "No Hand"
        color = (100, 100, 100)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                landmarks = hand_landmarks.landmark
                
                # Logic:
                # 1. Index Finger pointing UP
                idx_up = is_finger_up(landmarks, 8, 6)
                
                # 2. Thumb pointing DOWN
                thmb_down = is_thumb_down(landmarks)
                
                # 3. Stability check: middle, ring, pinky should be closed (optional)
                # But for simplicity, let's stick to the core request first.
                
                if idx_up and not thmb_down:
                    pyautogui.scroll(SCROLL_SPEED)
                    status = "SCROLL UP (Index Up)"
                    color = (0, 255, 0)
                elif thmb_down and not idx_up:
                    pyautogui.scroll(-SCROLL_SPEED)
                    status = "SCROLL DOWN (Thumb Down)"
                    color = (0, 0, 255)
                else:
                    status = "IDLE (Neutral)"
                    color = (255, 255, 255)

        # UI Overlay
        cv2.rectangle(image, (5, 5), (420, 60), (0, 0, 0), -1)
        cv2.putText(image, status, (15, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.imshow('Auto Scroll Gestures', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    hands.close()
