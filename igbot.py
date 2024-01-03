import pathlib
import random
import os
from instagrapi import Client
from instagrapi.types import Location




path = pathlib.Path(__file__).parent.resolve()
cl = Client()

def f4f():
    posts = cl.hashtag_medias_recent("like4like", 5)
    for i in range(5):
        print(f"Liked Post {i+1}")
        cl.media_like(posts[i].id)
        cl.user_follow(posts[i].user.pk)
        print("Followed " + posts[i].user.username)




def getcaption(hashtags):
    num = random.randint(0,99)
    f = open(f"{path}/config/captions.txt", encoding="utf8")
    content = f.readlines()
    caption = content[num] + hashtags
    f.close()
    return caption


def postimg(imgpath, caption):
    print("Posting with caption: " + caption) 
    cl.photo_upload(
        imgpath,
        caption,
        location=Location(name='Singapore', lat=1.351880, lng =103.823339)
        )

def storyimg(imgpath, caption):
    print("Uploading Story")
    cl.photo_upload_to_story(imgpath, caption)
    

def auto(hashtags, algo, confirm):
    prev = 1
    while (os.path.exists(f"{path}/output/{prev}.jpg")):
        prev+=1
    latest = prev - 1 
    imgpath = f"{path}/output/{latest}.jpg"
    caption = getcaption(hashtags)
    
    #gain confirmation
    if int(confirm) == 0:
        print(f"Upload {latest}.jpg with caption: {caption} ? ")
        confirmation = input("[y/n]:")
        if (confirmation == "y" or confirmation == "Y"):
            postimg(imgpath, caption)
            if int(algo) == 0:
                f4f()
        else:
            quit()
    else:
        postimg(imgpath, caption)
        if int(algo) == 0:
            f4f()




def main():
    f = open(f"{path}/config/igsettings.txt", "r")
    username, password, hashtags, algo, confirm = f.read().splitlines()
    f.close()
    
    print(f"Logging in to @{username}")
    cl.login(username, password)
    auto(hashtags, algo, confirm)


if __name__ == "__main__":
    main()






