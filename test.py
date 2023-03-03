import os,time,pygame
pygame.mixer.init()

def custom_sort_key(filename:str):
    filename = filename.removeprefix('C:/Users/code code/Main/Projects/python/badascii/frames_c')
    
    parts = filename.split("_")
    print(str(int(parts[2].split(".")[0].lstrip("0"))) + " 🗸")
    time.sleep(0.0000001)
    return int(parts[2].split(".")[0].lstrip("0"))

lst = []
for filename in os.listdir("C:/Users/code code/Main/Projects/python/badascii/frames_c"):
    lst.append(custom_sort_key(filename=filename))

lst.sort()

pygame.mixer_music.load("C:/Users/code code/Main/Projects/python/badascii/bad_apple_is/bad_apple.wav")
pygame.mixer_music.play()

for filename in lst:
    with open("C:/Users/code code/Main/Projects/python/badascii/bad_apple_"+str(filename)+".png.txt",encoding="UTF-8") as f:
        print(f.read())
        time.sleep(0.02995613258219)

os.system("cls")