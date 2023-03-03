from PIL import Image
import os

def image_to_txt(image:str):
    test_file = image
    mnm = image.removeprefix("C:/Users/code code/Main/Projects/python/badascii/frames_c/")

    #wow no way test file
    chars = {
        100:"█",
        80:"▓",
        60:"■",
        40:"▒",
        20:"░",
        0:" "
    }

    print([char for char in chars.values()])

    test_im = Image.open(test_file)
    if test_im.mode != "L":
        test_im = test_im.convert("L")
    pixels = test_im.load()
    img_size = test_im.size
    print(img_size)

    def char(x):
        numbers = list(chars.keys())

        closest_number = numbers[0]
        smallest_difference = abs(x - closest_number)

        for number in numbers:
            difference = abs(x - number)
            if difference < smallest_difference:
                closest_number = number
                smallest_difference = difference

        return chars[closest_number]

    oldcol = 0

    for row in range(img_size[1]):
        for col in range(img_size[0]):
            vg:tuple =  pixels[col,row]
            print(f"{vg}, {col,row},{char(vg)}")
            with open(f"{mnm}.txt", "a",encoding="UTF-8") as f:
                if row != oldcol:
                    oldcol = row
                    f.write("\n")
                else:
                    pass
                f.write(char(vg))

for filename in os.listdir("C:/Users/code code/Main/Projects/python/badascii/frames_c"):
    image_to_txt("C:/Users/code code/Main/Projects/python/badascii/frames_c/"+filename)