import os
import pathlib
import random
from diffusers import StableDiffusionXLPipeline
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

#declare project directory
path = pathlib.Path(__file__).parent.resolve()

#reads settings.txt and load the config
def config():
    settings = [0,0,0]
    f = open(f"{path}/config/settings.txt", "r")
    j = 0
    for x in f:
        settings[j] = int(x)
        j += 1
    f.close()
    return settings



def testNSFW():
    #load latest generated image
    prev = 1
    while (os.path.exists(f"{path}/output/{prev}.jpg")):
        prev+=1
    latest = prev - 1
    img = Image.open(f"{path}/output/{latest}.jpg")

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

    timenum = random.randint(0,1)
    if (timenum == 0):
        when = " at night"

    expressionnum = random.randint(0,99)
    if (expressionnum in range (0,29,1)):
        expression = " smiling"
    elif (expressionnum in range (30,59,1)):
        expression = " sad"    
    elif (expressionnum in range (60,70,1)):
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



def getimage(pipe, prompt):
    
    #load LORA weight. Ensure base model of weight is either SD v1-5 or SDXL v1.0
    pipe.load_lora_weights(f"{path}/models/weight.safetensors")
    prompt = "woman at night"
    #generate image
    negprompt = "deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, NSFW"
    output = pipe(prompt=prompt,
                  num_inference_steps=100, 
                  height=1024, width=1024,
                  negative_prompt = negprompt).images[0]
       
    #saving image into output folder
    name = 1
    while (os.path.exists(f"{path}/output/{name}.jpg")):
        name+=1

    output.save(f"{path}/output/{name}.jpg")
  


def main():

    settings = config()

    #choose models based off settings

    if settings[0] == 1:                 #using SD v1-5
        modelpl = StableDiffusionPipeline
        if settings[1] == 0:             #using pre-trained model
            if os.path.exists(f"{path}/models/realistic"):
                model = f"{path}/models/realistic"
            else:
                model = "SG161222/Realistic_Vision_V6.0_B1_noVAE" 
        else:                            #download SD 1.5 from huggingface
            model = "runwayml--stable-diffusion-v1-5"

    else:                                #using SDXL 1.0
        modelpl= StableDiffusionXLPipeline
        if settings[1] == 0:             #using pre-trained model
            if os.path.exists(f"{path}/models/realistic"):
                model = f"{path}/models/realisticXL"
            else:
                model = "coreml-community/coreml-YamersRealistic-v4_SDXL_8-bit"
        else:                            #download SDXL 1.0 from huggingface
            model = "stabilityai/stable-diffusion-xl-base-1.0"
        


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
    if settings[2] == 0:
        prompt = getprompt()
    else:
        prompt = input("Prompt: ")

    getimage(pipe, prompt)


    #Regenerate image until a safe image is produced
    while testNSFW() == (0,0,0):    
        print("Retrying. Consider changing prompts.")
        getimage(pipe)




if __name__ == "__main__":
    main()