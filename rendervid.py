# ffmpeg


import subprocess
import os

imagespath='/Users/shalevwiden/Downloads/Projects/blurbifyoutput/demovid'

donepath='/Users/shalevwiden/Downloads/Projects/blurbifyoutput/vidoutput'

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
        # tell FFmpeg it's a file list
        "-pattern_type", "glob",
              
        "-safe", "0",                
        "-i", file_list_path,
            "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2",

            "-r", str(framerate),       # output framerate

        "-c:v", codec,
        "-pix_fmt", pix_fmt,
        output_file
    ]

    # === Run command ===
    subprocess.run(cmd, check=True)
    print('created vid')

createvid()