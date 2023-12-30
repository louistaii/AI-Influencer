
# Ai Influencer

## Introduction
The purpose of this project is to generate AI instagram worthy pictures with consistent facial features. The project is mainly powered by Diffusers from [huggingface](https://huggingface.co/docs/diffusers/index). This repository, together with an Instagram manager bot, can be made to manage a AI influencer account on its own. See [Claire Reety](#claire) for example of implementation. The LORA weights found in this repository are trained to generate Claires's features specifically. However, the repository is made to be flexible for anyone with their own trained model to use.

<div align="left">
  <img src="https://drive.google.com/uc?id=1waE5gjU2Gcnt1QWoNamjMjwd95QiZfhN" />
</div>

## Updates

**`2023-30-12`**: Automatic prompt generator added to vary type of images generated for better realism. "setup.py" and "requirements.txt" updated. Tests for NSFW images implemented and automatic re-generating of images until SFW ones produced.




## Quick Start

### Installation
Clone this repository and run 'setup.bat' to install the [dependencies](#dependencies) needed.
Alternatively, you could run ```pip install -r requirements.txt``` in the directory and then run "setup.py"

### Run time
- The initial run will take significantly more time due to the initial downloading of stable diffusion. Subsequent run times to generate image depends on the RAM and VRAM available on the machine running this project.

## Models
- The base models available are [stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) and [stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5). 
- However, pre-trained models with smaller file sizes are provided. Opt to use them by changing the settings through "setup.py". Models provided are [Realistic Vision V6.0 B1](https://civitai.com/models/4201/realistic-vision-v60-b1) (SD v1-5 base) and [SDXL Yamer's Realistic](https://civitai.com/models/127923?modelVersionId=272724) (SDXL v1.0 base). They produce better results compared to the base models, hence they are HIGHLY RECOMMENDED
- To use your own custom model, rename your model file to ```realistic``` (for models with SD v1-5 base) or ```realisticXL``` (SDXL v1.0 based) and then place the model folder into the folder named "models" 
- Custom LORA weights can be used by replacing the ```weight.safetensors``` file in the "models" folder with your trained weights.      



## Dependencies
- Compatibillity for Python 3.10.8 - 3.11
- Python modules: accelerate(recommended), diffusers v0.25, Pillow v10.1, Pytorch 2.01 with Cuda Support
- Minimum 4GB of VRAM (12GB reccomended) and 12GB of space


## Claire
Claire's features are completely AI generated. Images of female celebrities were used as image prompts to generate pictures in stable diffusion to produce unique faces. These faces were then used as image prompts to repeat the cycle of generating faces until Claire's features were generated. Images of her face were then used to train and create the LORA weight found in the repository.
<div align="center">
  <img src="https://drive.google.com/uc?id=1Iu_beiUUH4EX_V0S0d2xCiNKRXxo7bFM" />
  <p>
    Give Claire Reety a follow on Instagram!
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








