
# AI Influencer
The purpose of this project is to create an AI Instagram influencer by automating both the generation of AI Instagram worthy images and the management of an Instagram account. See [Claire Reety](#claire) for example of implementation. The repository consists of 2 parts: [AI image generation](#generating-ai-images) and [Instagram bot](#instagram-bot). Note that the AI image generation can work independently from the Instagram handler bot if the user chooses not to upload to Instagram. AI Influencer also comes with a low spec mode to enable lower tier PCs to run the project. However, this comes with the cost of lower quality images.

## Generating AI images
### Introduction
This part of the project is mainly powered by Diffusers from [huggingface](https://huggingface.co/docs/diffusers/index). To produce consistent facial features, trained image generating models and LORA weights were used. This project is optimised to generate Claires's features specifically. However, it is made to be flexible for anyone with their own trained model to adjust and use. 
An automated prompt generator is embedded in the project to vary the images that are generated for more realism. All generated images are saved in the "outputs" folder.

<div align="left">
  <img src="https://drive.google.com/uc?id=1waE5gjU2Gcnt1QWoNamjMjwd95QiZfhN" />
</div>

### Models
- The image models used are pre trained models based off [stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) and [stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5). They can be found here: [Realistic Vision V6.0 B1](https://civitai.com/models/4201/realistic-vision-v60-b1) (SD v1-5 base) and [SDXL Yamer's Realistic](https://civitai.com/models/127923?modelVersionId=272724) (SDXL v1.0 base). They produce better results compared to the base models, hence they are HIGHLY RECOMMENDED
- To use your own custom model, rename your model file to ```realistic``` (for models with SD v1-5 base) or ```realisticXL``` (SDXL v1.0 based) and then place the model folder into the folder named "models". Custom LORA weights can be used by replacing the ```weight.safetensors``` file in the "models" folder with your trained weights.      

### Run time
- The initial run will take significantly more time due to the initial downloading of stable diffusion and selected models. Expect future runtimes to be lower.
- AI image generation is a higly CPU and GPU dependent task. Hence run times to generate image depends on the RAM and VRAM available on the machine running this project.

## Instagram Bot
Simple Instagram bot that selects an image and caption before posting. Comes with a hashtag feature for captions and an [algorithm](#algorithm) to increase social media traction. Captions are chosen by randomly picking 1 in a list of 100 intriguing captions. The list of captions can be edited by editing the ```captions.txt``` file in the "config" folder
### Algorithm
Directly after posting an image, AI Influencer will search for the latest few posts in the #like4like catergory. AI Influencer will then like these posts and follow the accounts that posted them. This helps publicise the account to other users and hopefully increase the like and following counts on our account.  


## Updates
- **`2023-30-12`**: Automatic prompt generator added to vary type of images generated for better realism. "setup.py" and "requirements.txt" updated. Tests for NSFW images implemented and automatic re-generating of images until SFW ones produced.
- **`2024-01-01`**: Happy New Year! Improved setup and implementation of instagram bot.

## Quick Start

### Installation
Clone this repository and run 'setup.bat' to install the [dependencies](#dependencies) needed.
Alternatively, you could run ```pip install -r requirements.txt``` in the directory and then run "setup.py"


## Dependencies
- Compatibillity for Python 3.10.8 - 3.11
- Minimum 4GB of VRAM (12GB reccomended) and 12GB of space
- diffusers==0.25.0
- gdown==4.7.1
- instagrapi==2.0.1
- Pillow==10.1.0
- psutil==5.9.7
- torch==2.0.1+cu118



## Claire
Claire's features are completely AI generated. They were generated through multiple cycles of image prompting with Stable Diffusion. Images with her features were then used to train and create the LORA weight found in the repository.
<div align="center">
  <img src="https://drive.google.com/uc?id=1Iu_beiUUH4EX_V0S0d2xCiNKRXxo7bFM" />
</div>

Claire's instagram account and content creation are both automated by this project. The code is being hosted on a server ran on randomly generated timings to evade Instagram's bot detection. 

<div align="center">
  <p>
    Give Claire Reety a follow on Instagram! Click on the image below!
  </p>
  <p>
    <a href="https://www.instagram.com/claire_reety/"><img src="https://drive.google.com/uc?id=1KGspAbrW2CocgEwmG0zJDzs4md9xeE8f" , width = 500/>
  </p>
</div>


## Other examples
- Generated with pre trained SD v1-5 and external [LORA weight](https://civitai.com/models/171781?modelVersionId=192959)
<div align="left">
  <img src= "https://drive.google.com/uc?id=1urQ8m4EOV-M6CvwPW3hhg50uTG3ST0ZV">
</div>








