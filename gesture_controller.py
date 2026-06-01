import cv2
import mediapipe as mp
import simpleaudio as sa
import os

# Load .wav files from current folder
music_folder = './songs'
playlist = [f"{music_folder}/{f}" for f in os.listdir(music_folder) if f.endswith('.wav')]
current_song_index = 0
play_obj = None
is_playing = False

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

def load_and_play_song(song_path):
    global play_obj
    wave_obj = sa.WaveObject.from_wave_file(song_path)
    play_obj = wave_obj.play()

def stop_song():
    global play_obj
    if play_obj and play_obj.is_playing():
        play_obj.stop()

# Play first song
load_and_play_song(playlist[current_song_index])
is_playing = True

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame")
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = handedness.classification[0].label  # 'Left' or 'Right'

            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            d_index = distance(thumb_tip, index_tip)
            d_middle = distance(thumb_tip, middle_tip)

            if label == 'Right':
                if d_index < 0.05 and not is_playing:
                    load_and_play_song(playlist[current_song_index])
                    is_playing = True
                elif d_index > 0.1 and is_playing:
                    stop_song()
                    is_playing = False

            elif label == 'Left':
                # Next song
                if d_index < 0.05:
                    stop_song()
                    current_song_index = (current_song_index + 1) % len(playlist)
                    load_and_play_song(playlist[current_song_index])
                    is_playing = True

                # Previous song
                elif d_middle < 0.05:
                    stop_song()
                    current_song_index = (current_song_index - 1) % len(playlist)
                    load_and_play_song(playlist[current_song_index])
                    is_playing = True

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Music Controller", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        stop_song()
        break

cap.release()
cv2.destroyAllWindows()
