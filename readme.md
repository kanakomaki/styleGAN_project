### Readme last update 2023.Sep.6
# Documentation of App "AIdentikit" 
## The app can generate face images from text inputs describing the face features.
This "Aidentitykit", firstly, selects the best-fit face image with input text keywords from the big database of the "CelebA dataset" (https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html). The CelebA dataset contains ~200K face images of celebrities in the world. 
Then, Aidentitykit arranges the picked-up face image with a feature that is input as a further text keyword and generates a new face image. You can continue to arrange the image as much as you want.

@inproceedings{liu2015faceattributes,
  title = {Deep Learning Face Attributes in the Wild},
  author = {Liu, Ziwei and Luo, Ping and Wang, Xiaogang and Tang, Xiaoou},
  booktitle = {Proceedings of International Conference on Computer Vision (ICCV)},
  month = {December},
  year = {2015} 

Demo Presentation Slide
![Demo presentation](./images/presentation1.png "Demo presentation")

Webpage(Home)
![app image](./images/app_image1.png "app front page")
Webpage(Demo)
![app image](./images/app_image2.png "app demo page")


# How to run this app locally?
streamlit run app7.py


# Preparation 
Some necessary packages will be imported when running style_clip.py while app7.py is being run. For example, Replicate, request, PIL, os, numpy, etc. Also, see requirements.txt. You need to install a package "text2image," see below.

## install in development mode
pip install -e .
## install in production mode
pip install .

## run command
python main.py

## To modify input text
you need to modify "input text" in "process.py"

## To see the selected pictures 
goto data/save/ directory

# Modification history
- 2023 Sep 06: updated py files and Readme.md
- 2023 Aug 30: added a vocabulary dict option in Tfidifvectorization
-            : changed ngram_range(1,2) --> (1,3)
