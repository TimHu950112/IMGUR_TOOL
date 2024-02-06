#上傳圖片
import pyimgur,os
from dotenv import load_dotenv
import os
load_dotenv()


CLIENT_ID = os.getenv("client_id")
PATH = "pexels-pixabay-372851.jpg" #A Filepath to an image on your computer"

Folder_Path="./processing"
All_Files=os.listdir(Folder_Path)

image_dict={}  # Create an empty dictionary to store image information
output_dict={}  # Create an empty dictionary to store output information

for file in All_Files:
    PATH = f"{Folder_Path}/{file}"
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif"):
        image_dict[PATH] = {}  # Create an empty dictionary for each image path

for image_path in image_dict.keys():
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(image_path, title="Uploaded with PyImgur")
    image_dict[image_path] = uploaded_image.link
    print('上傳進度-',image_path)

for i in image_dict.keys():
    filename = os.path.basename(i)
    output_dict[filename] = image_dict[i]

print(output_dict)
print('上傳完成，共上傳',len(output_dict),'張圖片')
