import sys
import subprocess

if len(sys.argv) < 2:
    print('Usage: python mp4-to-webm.py <input_file> [<input_file> ...]')
    sys.exit(1)

input_files = sys.argv[1:]

for input_file in input_files:
    output_file = input_file[:-4] + '_converted.webm'
    command = ['ffmpeg', '-i', input_file, '-c:v', 'vp9', '-c:a', 'libopus', output_file]
    subprocess.run(command)