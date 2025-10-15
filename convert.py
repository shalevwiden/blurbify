import os
import subprocess
post2path='/Users/shalevwiden/Downloads/Projects/blurbifyoutput/post22'


def convert_mov_to_mp4(folder_path):
    """
    Converts all .mov files in the given folder to .mp4 using ffmpeg.
    The output files are saved in the same folder.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".mov"):
            mov_path = os.path.join(folder_path, filename)
            mp4_path = os.path.join(folder_path, os.path.splitext(filename)[0] + ".mp4")

            print(f"Converting {filename} → {os.path.basename(mp4_path)} ...")

            # Run ffmpeg
            command = [
                "ffmpeg",
                "-i", mov_path,
                "-c:v", "libx264",  # video codec
                "-c:a", "aac",      # audio codec
                "-b:a", "192k",
                "-y",               # overwrite without asking
                mp4_path
            ]

            # subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("✅ Done.")

    print("All conversions complete.")


import os
import subprocess

import os
import subprocess

def make_instagram_friendly(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".mp4"):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, os.path.splitext(filename)[0] + "_insta.mp4")

            print(f"🎞️ Fixing {filename} for Instagram…")

            vf_filter = (
                "scale=1080:-2,"
                "crop='min(iw,ih*1.76)':'min(ih,iw/1.76)',"
                "pad=ceil(iw/2)*2:ceil(ih/2)*2:(ow-iw)/2:(oh-ih)/2,"
                "setsar=1,fps=30"
            )

            command = [
                "ffmpeg", "-y",
                "-i", input_path,
                "-vf", vf_filter,
                "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                "-pix_fmt", "yuv420p",
                "-profile:v", "high", "-level", "4.1",
                "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
                "-movflags", "+faststart",
                "-map_metadata", "-1",  # remove metadata
                "-fflags", "+genpts",
                output_path
            ]

            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                os.remove(input_path)
                print(f"✅ Done: {output_path}")
            else:
                print(f"❌ Conversion failed for {filename}. Keeping original.")
                print(result.stderr.decode().splitlines()[-10:])

    print("🚀 All videos processed.")

make_instagram_friendly(post2path)