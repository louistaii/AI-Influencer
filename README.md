
# AI Influencer
The purpose of this project is to create an AI Instagram influencer by automating both the generation of AI Instagram worthy images and the management of an Instagram account. See [Claire Reety](#claire) for example of implementation. The repository consists of 2 parts: [AI image generation](#generating-ai-images) and [Instagram bot](#instagram-bot). AI Influencer also comes with a low spec mode to enable lower tier PCs to run the project. However, this comes with the cost of lower quality images.  
Note: AI image generation can work independently from the Instagram handler bot if the user chooses not to upload to Instagram. 

## Generating AI images
### Introduction
This part of the project is mainly powered by Diffusers from [huggingface](https://huggingface.co/docs/diffusers/index). To generate consistent facial features, this project utilizes trained image generating models and LORA weights. It's primarily optimized for generating Claire's distinctive features. However, it's adaptable for those with their own trained models to use. All generated images are saved in the "outputs" folder.  
Note: Intial run will take significantly longer due to the initial download of stable diffusion. Expect subsequent run times to be faster. 
 
<div align="left">
  <img src="https://drive.google.com/uc?id=1waE5gjU2Gcnt1QWoNamjMjwd95QiZfhN" />
</div>

### Features
- Option to use different models / trained LORA weight
- Auto prompt generator to increase automation and vary the images generated for more realism
- Enhanced NSFW checker to detect and replace NSFW generated images generated
- Highly customizable configuration. Includes low spec mode for lower CPU/GPU usage and high spec mode for better quality results.

### Models
- The image models used are pre trained models based off [stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) and [stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5). They can be found here: [Realistic Vision V6.0 B1](https://civitai.com/models/4201/realistic-vision-v60-b1) (SD v1-5 base) , [SDXL Yamer's Realistic](https://civitai.com/models/127923?modelVersionId=272724) (SDXL v1.0 base). These models are trained to generate images with greater realism which enhances the objective of this project.
- To use your own custom model, rename your model file to ```realistic``` (for models with SD v1-5 base) or ```realisticXL``` (SDXL v1.0 based) and then place the model folder into the folder named "models".
Custom LORA weights can be used by replacing the ```weight.safetensors``` (for models with SD v1-5 base) or ```weightXL.safetensors``` (SDXL v1.0 based) file in the "models" folder with your trained weights.      



## Instagram Bot
Simple Instagram bot that automates the selection of images and captions for a Instagram post and posts it.  
Comes with a hashtag feature to add custom hashtags in captions and an [algorithm](#algorithm) to increase social media traction.   
Captions are chosen by random from a list of 100 intriguing captions. The list of captions can be edited by editing the ```captions.txt``` file in the "config" folder.   
Note: the bot only works for existing Instagram accounts and will not create one for you.
### Algorithm
Immediately after posting an image, AI Influencer will browse recent posts under the #like4like category, engaging by liking them and following their respective accounts. This helps publicise the account to other users and aims to boost the like and following counts on the account.


## Updates
- **`2023-30-12`**: Automatic prompt generator added to vary type of images generated for better realism. "setup.py" and "requirements.txt" updated. Tests for NSFW images implemented and automatic re-generating of images until SFW ones produced.
- **`2024-01-01`**: Happy New Year! Improved setup and implementation of instagram bot.
- **`2024-03-01`**: Fixed setup bugs and simplified code. Improved SD v1-5 trained LORA weights. Auto downloading of LORA weight files.

## Quick Start

### Installation
Clone this repository and run 'setup.bat' to install the [dependencies](#dependencies) needed.  
Alternatively, you could run ```pip install -r requirements.txt``` in the directory and then run "setup.py".  
Simply launch 'run.bat' after configuration to start the project and the intial download of Stable Diffusion.




## Dependencies
- Compatibillity for Python 3.10.8 - 3.11
- Minimum 4GB of VRAM (12GB reccomended) and 12GB of space
- diffusers v0.25.0
- gdown v4.7.1
- instagrapi v2.0.1
- Pillow v10.1.0
- psutil v5.9.7
- torch v2.0.1+cu118



## Claire
<div align="center">
  <p>
    Give Claire Reety a follow on Instagram! Click on the image below!
  </p>
  <p>
    <a href="https://www.instagram.com/claire_reety/"><img src="https://drive.google.com/uc?id=1KGspAbrW2CocgEwmG0zJDzs4md9xeE8f" , width = 500/>
  </p>
</div>
      
Claire's features are entirely AI-generated, derived from multiple rounds of image prompting using Stable Diffusion. Images with her features were then used to train and create the LORA weight found in the repository.

<div align="center">
  <img src="https://drive.google.com/uc?id=1Iu_beiUUH4EX_V0S0d2xCiNKRXxo7bFM" />
</div>

Claire's Instagram account operates on this project by configuring it for complete automation and server compatibility (lower CPU/GPU usage). The repository is being hosted on a [Pytonanywhere](https://www.pythonanywhere.com/) server as they have no hard limits on CPU usage. The project automatically runs once a day on randomly generated timings to evade Instagram's bot detection. 



## Other examples
- Generated with pre trained SD v1-5 and external [LORA weight](https://civitai.com/models/171781?modelVersionId=192959)
<div align="left">
  <img src= "https://drive.google.com/uc?id=1urQ8m4EOV-M6CvwPW3hhg50uTG3ST0ZV">
</div>








