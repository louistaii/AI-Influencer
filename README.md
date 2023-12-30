
# Claire: Ai Influencer

<div align="left">
  <img src="https://drive.google.com/uc?id=1waE5gjU2Gcnt1QWoNamjMjwd95QiZfhN" />
</div>


## Introduction
The purpose of this project is to generate AI instagram worthy pictures with consistent facial features. This project is mainly powered by Diffusers from [huggingface](https://huggingface.co/docs/diffusers/index).
The face of Claire is completelly AI generated. The LORA weights found in this repository are trained to generate Claires's features specifically. However, the repository is made to be flexible for anyone with their own trained model and wishes to create their own AI influencer to use.


## Updates

**`2023-30-12`**: 





## Quick Start

### Installation
Clone this repository and run 'setup.bat' to install the [dependencies](#dependencies) needed.
Alternatively, you could run ```pip install -r requirements.txt``` in the directory and then run "setup.py"

### Run time
- The initial run will take significantly more time due to the initial downloading of stable diffusion. Subsequent run times to generate image depends on the RAM and VRAM available on the machine running this project.

### Models
- The base models available are [stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) and [stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5). 
- However, samller sized diffuser friendly, pre-trained models are provided. Opt to use them by changing the settings through setup.py. Models provided are modified and converted versions of [Realistic Vision V6.0 B1
](https://civitai.com/models/4201/realistic-vision-v60-b1) (SD v1-5 base) and [SDXL Yamer's Realistic](https://civitai.com/models/127923?modelVersionId=272724) (SDXL v1.0 base). They are significantly smaller in size than their base models without affecting quality of image output.
- To use your own custom model, place the model folder into the "models" folder and rename it to ```realistic```
- Custom LORA weights can be used by replacing the ```weight.safetensors``` file in the "models" folder with your trained weights.      



## Dependencies
- Compatibillity for Python 3.10.8 - 3.11
- Python modules: accelerate, diffusers, pytorch with Cuda Support
- Minimum 4GB of VRAM (12GB reccomended)



## Other examples
- Generated with pre trained SD v1-5 and external [LORA weight](https://civitai.com/models/171781?modelVersionId=192959)
<div align="left">
  <img src= "https://drive.google.com/uc?id=1urQ8m4EOV-M6CvwPW3hhg50uTG3ST0ZV">
</div>








