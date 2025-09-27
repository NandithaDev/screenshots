import cv2
import os

def extract_frames(video_path, output_dir="bg", interval_seconds=3):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    frame_interval = int(fps * interval_seconds)

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            filename = os.path.join(output_dir, f"frame3_{frame_count}.jpg")
            cv2.imwrite(filename, frame)  # Keep RGB
            saved_count += 1
            print(f"Saved frame {frame_count}")

        frame_count += 1

    cap.release()
    print(f"Total frames saved: {saved_count}")

# Example usage
extract_frames("vid1.mp4", interval_seconds=1)

