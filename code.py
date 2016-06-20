import os
from shutil import move

music_dir = "./music"
img_dir = "./image"
doc_dir = "./documents"

music_ext = ["mp3"]
img_ext = ["jpg", "png"]
doc_ext = ["doc", "docx", "ppt", "pptx", "xls", "xlsx"]

def get_extension(x):
    file_extension = os.path.splitext(x)[1]
    print(x)
    file_extension = file_extension.replace(".", "")
    return file_extension

if not(os.path.exists(music_dir)):
    os.mkdir(music_dir)
if not(os.path.exists(img_dir)):
    os.mkdir(img_dir)
if not(os.path.exists(doc_dir)):
    os.mkdir(doc_dir)

files = os.listdir(str('.'))
print(files)
i = 0
while(i < len(files)):
    print(i)
    if(os.path.isfile(files[i])):
        ext = get_extension(files[i])
        if (ext in music_ext):
            move(files[i], music_dir + "/" + files[i])
        elif (ext in img_ext):
            move(files[i], img_dir + "/" + files[i])
        elif (ext in doc_ext):
            move(files[i], doc_dir + "/" + files[i])
    i = i+1
