import sys
import subprocess

if len(sys.argv) < 2:
    print('Usage: python script.py <input_file> [<input_file> ...]')
    sys.exit(1)

input_files = sys.argv[1:]

for input_file in input_files:
    output_file = input_file[:-5] + '_converted.mp4'
    command = ['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-c:a', 'aac', output_file]
    subprocess.run(command)