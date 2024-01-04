import os
import pathlib
import random
import igbot

from diffusers import StableDiffusionXLPipeline
from diffusers import StableDiffusionPipeline
import torch
import gdown
from PIL import Image

#declare project directory
path = pathlib.Path(__file__).parent.resolve()

#reads in settings and load the config
def aiconfig():
    settings = [0,0,0,0]
    f = open(f"{path}/config/aisettings.txt", "r")
    j = 0
    for x in f:
        settings[j] = int(x)
        j += 1
    f.close()
    return settings



def testNSFW(img):
    #get colours in image
    colors = img.getcolors(1000) 
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present   #returns most detected colour
    except TypeError:
        return



# automatically generates random prompts each time
def getprompt():
    where = ""
    when = ""
    expression = ""
    pictype = ""

    locationnum = random.randint(0,4)
    if (locationnum == 0):
        where = " outdoors"
    elif (locationnum == 1):
        where = " indoors"
    elif (locationnum == 2):
        where = " in nature"
    elif (locationnum == 3):
        where = " in a city"

    timenum = random.randint(0,2)
    if (timenum == 0):
        when = " at night"

    expressionnum = random.randint(0,99)
    if (expressionnum in range (0,39,1)):   # 40% chance due to better results
        expression = " smiling"
    elif (expressionnum in range (40,49,1)): # 10% chance
        expression = " sad"    
    elif (expressionnum in range (50,59,1)): #last 40% dedicated to no expression
        expression = " angry"
    
    picnum = random.randint(0,9)
    if (picnum == 0):
        pictype = "close up picture of "
        where,when = "" , ""
    elif (picnum == 1):
        pictype = "selfie of "


    prompt = f"{pictype}woman{where}{when}{expression}"
    print(prompt)
    return prompt



def getimage(pipe, prompt,steps):
    
    #generate image
    negprompt = "deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, NSFW"
    output = pipe(prompt=prompt,
                  num_inference_steps=steps, 
                  height=1024, width=1024,
                  negative_prompt = negprompt).images[0]
       
    #saving image into output folder
    name = 1
    while (os.path.exists(f"{path}/output/{name}.jpg")):
        name+=1

    output.save(f"{path}/output/{name}.jpg")
  


def main():

    settings = aiconfig()

    #choose models based off settings
    if settings[0] == 1:                 #using SD v1-5
        modelpl = StableDiffusionPipeline
        if os.path.exists(f"{path}/models/realistic"):
            model = f"{path}/models/realistic"
        else:
            model = "SG161222/Realistic_Vision_V6.0_B1_noVAE"

        if os.path.exists(f"{path}/models/weight.safetensors") == False:       #downloads claire LORA weights
            print("Downloading Claire trained weights for SD v1-5...")
            url = "https://drive.google.com/uc?id=1_X5vV409D0mr8fU2N7i5vu1rnToV8jBD"
            output = f"{path}/models/weight.safetensors"
            gdown.download(url, output, quiet=False)

    else:                                #using SDXL 1.0
        modelpl= StableDiffusionXLPipeline          
        
        if os.path.exists(f"{path}/models/realisticXL") == False:
            print("Downloading trained model for SDXL 1.0...This make take awhile...")
            url = "https://drive.google.com/drive/folders/1xTRiqZ__XhLR0zxbTaMTG21yYK3-z30u?usp=sharing"
            output = f"{path}/models/realisticXL"
            gdown.download_folder(url, output = output,quiet=True, use_cookies=False)   

        model = f"{path}/models/realisticXL"

        
        if os.path.exists(f"{path}/models/weightXL.safetensors") == False:       #downloads claire LORA weights
            print("Downloading Claire trained weights for SDXL 1.0...")
            url = "https://drive.google.com/uc?id=1EJsV_2zqseAypcH_v_Eku49x7QMtJMeE"
            output = f"{path}/models/weightXL.safetensors"
            gdown.download(url, output, quiet=False)
    

    #check for cuda support and setup pipeline accordingly
    if torch.cuda.is_available() == True:         
        pipe = modelpl.from_pretrained(model,
                                       torch_dtype=torch.float16
                                       )
        pipe = pipe.to("cuda") 
    else:
        print('Pytorch with Cuda support not found, proceeding with CPU only...')
        pipe = modelpl.from_pretrained(model, 
                                       torch_dtype=torch.float32
                                       )
    
    
    steps = round(int(settings[1]))

    if settings[2] == 0:
        prompt = getprompt()
    else:
        prompt = input("Prompt: ")
    
    if(settings[0]==1):
        pipe.load_lora_weights(f"{path}/models/weight.safetensors")
    else:
        pipe.load_lora_weights(f"{path}/models/weightXL.safetensors")

    getimage(pipe, prompt, steps)


    #load latest generated image
    prev = 1
    while (os.path.exists(f"{path}/output/{prev}.jpg")):
        prev+=1
    latest = prev - 1
    img = Image.open(f"{path}/output/{latest}.jpg")


    #Regenerate image until a safe image is produced
    while testNSFW(img) == (0,0,0):    
        print("Retrying. Consider changing prompts.")
        os.remove(f"{path}/output/{latest}.jpg")
        getimage(pipe, prompt, steps)

    #open final image
    img.show()

    if settings[3] == 0:
        igbot.main()





if __name__ == "__main__":
    main()