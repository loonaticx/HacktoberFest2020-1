import os, subprocess
import sys, re


allFiles = []
for root, _, files in os.walk('.'):
    root = root.replace('.', '')
    
    for file in files:
        if not file.endswith('.mp3') or file.endswith('.mp4'):
            continue

        file = os.path.join(root, file)
        allFiles.append(file)

print(allFiles)

for file in allFiles: 
    newFile = file.replace('.mp3', '.mp4')
        
    if os.path.exists(newFile):
        print('%s already exists' % newFile)
        continue

    print('Encoding %s' % file)

    #x = ['ffmpeg', '-i', file, '-vcodec', 'h264', '-vf', 'subtitles=%s' % re.escape(file), '-preset', 'veryfast', '-acodec', 'aac', '-map_chapters', '-1', '-map', '0:v:0', '-map', '0:a:1', '-strict', '-2', newFile]
    x = ['ffmpeg', '-loop', '1', '-i', 'FRONT_COVER.png', '-i', file, '-shortest', '-c:v', 'libx264', '-tune', 'stillimage', '-c:a', 'copy', newFile]
    print(x)
    subprocess.call(x, shell=True)
    
    if (not os.path.exists(newFile)) or os.path.getsize(newFile) == 0:
        print('Failure')
        sys.exit()
    
    #os.remove(file)
