
# Claire: Ai influencer

<div align="left">
  <img src="https://insightface.ai/assets/img/custom/logo3.jpg" width="240"/>
</div>


## Introduction
The purpose of this project is to generate AI instagram worthy pictures with consistent facial features. This project is mainly powered by Diffusers from [huggingface]().
The face of Claire is completelly AI generated. The LORA weights found in this repository are trained to generate Claires's features specifically. However, the repository is made to be flexible for anyone with their own trained model and wishes to create their own AI influencer to use.


## Updates

**`2023-08-08`**:





## Quick Start

### Installation
Clone this repository and run 'setup.bat' to install the [dependencies](#dependencies) needed.
Alternatively, you could run ```pip install -r requirements.txt``` in the directory and then run "setup.py"

### Run time
- The initial run will take significantly more time due to the initial downloading of stable diffusion.
- Time taken to generate image depends on the RAM and VRAM available on the machine running this project.
- est times for : ~1min per image

### Models
- The base models available are [stable-diffusion-xl-base-1.0]() and [stable-diffusion-v1-5](). 
- However, samller sized, diffuser friendly and pre-trained models are provided. Opt to use them by changing the settings through setup.py. Models provided are modified versions of []() (GB) for SD v1-5 and []() (GB) for (SDXL v1.0). I have converted the .safetensor files to diffuser friendly modules. They are significantly smaller than their base models with no significant difference in effectiveness.
- To use your own custom model, place the model folder into the "models" folder and rename it to ```lanjiao```
- Custom LORA weights can be used by replacing the ```face.safetensors``` file in the "models" folder with your trained weights.      



## Dependencies
- Compatibillity for Python 3.10.8 - 3.11
- Python modules: accelerate, diffusers, pytorch with Cuda Support
- Minimum 4GB of VRAM (12GB reccomended)



## Meet Joy


[<img src=https://insightface.ai/assets/img/github/facerecognitionfromvideo.PNG width="760" />](https://www.youtube.com/watch?v=y-D1tReryGA&t=81s)


Please click the image to watch the Youtube video. For Bilibili users, click [here](https://www.bilibili.com/video/av38041494?from=search&seid=11501833604850032313).








