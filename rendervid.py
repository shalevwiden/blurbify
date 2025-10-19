# ffmpeg


import subprocess
import os

imagespath='/Users/shalevwiden/Downloads/Projects/blurbify/outputs/demovid'

donepath='/Users/shalevwiden/Downloads/Projects/blurbify/outputs/vidoutput'

def checkpaths():
    if os.path.exists(imagespath):
        print('first good')
    if os.path.exists(donepath):
        print('second good')
    else:
        print(f'not found\n\n\n\n')

framerate = 10                 # frames per second
output_file =os.path.join(donepath,'donevid.mp4')      # output file

if os.path.exists(output_file):
    os.remove(output_file)
codec = "libx264"              # codec (common for mp4)
pix_fmt = "yuv420p"            # ensures compatibility


file_list_path = os.path.join(donepath, "file_list.txt")
def makefilelist():
    images = sorted([
        f for f in os.listdir(imagespath)
        if f.lower().endswith(('.png', '.jpg', '.webp'))
    ])

  
    with open(file_list_path, "w") as f:
        for img in images:
            f.write(f"file '{os.path.join(imagespath, img)}'\n")

makefilelist()
# === Build FFmpeg command ===
def createvid():
    cmd = [
        "ffmpeg",
        "-f", "concat",        # tell FFmpeg it's a list of files
        "-safe", "0",          # allow absolute paths
        "-i", file_list_path,  # path to file_list.txt
        "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2",
        "-r", str(framerate),
        "-c:v", codec,
        "-pix_fmt", pix_fmt,
        output_file
    ]

    subprocess.run(cmd, check=True)
    print("✅ Created video successfully!")
createvid()