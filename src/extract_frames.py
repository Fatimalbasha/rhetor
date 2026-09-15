import cv2 
import os 
import ffmpeg # Fast Forward Moving Picture Experts Group

# path to the input video 
video_path = "data/test.mp4"

# directory to save the extracted frames 
output_dir = "outputs/test/frames"

# creating the output folder
os.makedirs(output_dir, exist_ok=True) # If the folder already exists, don't throw an error

# opening the video file 
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: couldn't open the video (check the path)")

# how many frames per second it runs at (fps = frame per second)
fps = cap.get(cv2.CAP_PROP_FPS) 
print(f"Video opend. FPS = {fps}")

# how many frames to skip, to save about 1 per second
frame_interval = int(fps)

frame_count = 0 # counts every frame we read
saved_count = 0 # counts only the frames we actually save

while True: 
    # read the next frame
    # success is False when the video ends
    #success --return--> True/False, did it get a frame?
    # frame --return--> the actual image
    success, frame = cap.read()
    if not success:
        break

    # save a frame only when frame_count is a multiple of frame_interval
    if frame_count % frame_interval == 0:
        filename = os.path.join(output_dir, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(filename, frame)
        saved_count += 1

    frame_count += 1

print(f"Done. Saved {saved_count} frames out of {frame_count} total")


# release the video file 
cap.release()


# ---- Adio extraction ---
audio_path = "outputs/test/audio.wav"

(
    ffmpeg
    .input(video_path) # points FFmpeg at the video __.mp4
    .output(audio_path, ac = 1, ar = 16000) # audio channels = 1 (converting the audio to mono) / audio rate = 16,000 Hz
    .overwrite_output() # re-running the script is painless
    .run(quiet=True) # hides FFmpeg's very noisy internal logging so the terminal stays readable
)

print(f"Audio saved to {audio_path}")

