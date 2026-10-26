import cv2
import mediapipe as mp
import random
import time

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

state = "WAITING"   
player_move = None
computer_move = None
result_text = ""
timer_start = 0

def get_gesture(hand_landmarks):
    tip_ids = [8, 12, 16, 20] 
    open_fingers = []

    for id in tip_ids:
        if hand_landmarks.landmark[id].y < hand_landmarks.landmark[id - 2].y:
            open_fingers.append(1)
        else:
            open_fingers.append(0)

    if open_fingers == [0, 0, 0, 0]:
        return "Bua"
    elif open_fingers == [1, 1, 0, 0]:
        return "Keo"
    elif open_fingers == [1, 1, 1, 1]:
        return "Bao"
    
    return None 

def get_winner(player, computer):
    if player == computer:
        return "HOA NHAU!"
    if (player == "Bua" and computer == "Keo") or \
       (player == "Keo" and computer == "Bao") or \
       (player == "Bao" and computer == "Bua"):
        return "BAN THANG!"
    return "MAY THANG!"

while True:
    success, img = cap.read()
    if not success:
        break
    
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    current_gesture = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            current_gesture = get_gesture(hand_landmarks)

    if state == "WAITING":
        cv2.putText(img, "GIO TAY DE BAT DAU (Bua/Keo/Bao)", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        
        if current_gesture:
            player_move = current_gesture
            state = "PLAYING"
            timer_start = time.time()
            
    elif state == "PLAYING":
        elapsed_time = time.time() - timer_start
        cv2.putText(img, f"Dang chot ket qua... {3 - int(elapsed_time)}s", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2)
        cv2.putText(img, f"Ban: {current_gesture}", (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        
        if current_gesture:
            player_move = current_gesture

        if elapsed_time > 3:
            if player_move: 
                computer_move = random.choice(["Bua", "Keo", "Bao"])
                result_text = get_winner(player_move, computer_move)
                state = "RESULT"
                timer_start = time.time()
            else:
                state = "WAITING" 
                
    elif state == "RESULT":
        cv2.putText(img, f"Ban: {player_move} VS May: {computer_move}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        color = (0, 255, 0) if result_text == "BAN THANG!" else (0, 0, 255) if result_text == "MAY THANG!" else (255, 255, 0)
        cv2.putText(img, result_text, (30, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 4)
        
        if time.time() - timer_start > 3:
            state = "WAITING"
            player_move = None
            computer_move = None

    cv2.imshow("Rock Paper Scissors", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()