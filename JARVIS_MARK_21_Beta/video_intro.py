import cv2
import threading
import time
import numpy as np
from core.config import BASE_DIR
import os

play_video = False
video_thread = None
fade_out = None

def play_intro_video(path="assets/intro.mp4"):
    video_path = os.path.join(BASE_DIR, path)
    print("Loading intro video...")
    global play_video, video_thread, fade_out
    if play_video:
        return

    play_video = True
    fade_out = False

    def _play():
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("❌ Could not open intro video.")
            return

        #cv2.namedWindow("Intro", cv2.WND_PROP_FULLSCREEN)
        #cv2.setWindowProperty("Intro", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # No fullscreen
        cv2.namedWindow("Intro", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Intro", 1280, 720)  # Manually resize

        fps = cap.get(cv2.CAP_PROP_FPS)
        delay = 0.5 / fps

        while play_video:
            ret, frame = cap.read()
            if not ret:
                break
            
            # 🔥 If fade-out requested, perform fade-out frames
            if fade_out:
                for alpha in np.linspace(1, 0, int(fps * 1.2)):  # ~1.2 sec fade
                    black = np.zeros_like(frame)
                    faded = cv2.addWeighted(frame, alpha, black, 1 - alpha, 0)
                    cv2.imshow("Intro", faded)
                    if cv2.waitKey(int(delay)) == 27:
                        break
                break  # Exit after fade
            
            cv2.imshow("Intro", frame)
            if cv2.waitKey(int(1000 / fps)) == 27:
                break
            #if cv2.waitKey(1) == 27:
             #   break
            #time.sleep(delay)

        cap.release()
        cv2.destroyAllWindows()

    video_thread = threading.Thread(target=_play)
    video_thread.daemon = True # Make sure it exits with main program
    video_thread.start()

def stop_intro_video():
    global play_video, video_thread, fade_out
    if play_video:
        play_video = False
        fade_out = True
        if video_thread and video_thread.is_alive():
            video_thread.join()
    print(f"intro stopped at {time.ctime()}")