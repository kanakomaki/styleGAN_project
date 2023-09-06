# Readme lat update 2023.Sep.6
# Description of App "AIdentikit"

![Demo presentation](./images/presentation1.png "Demo presentation")

![app image](./images/app_image1.png "app front page")

![app image](./images/app_image2.png "app demo page")

# setup command 
## install in development mode
pip install -e .
## install in production mode
pip install .

# run command
python main.py

# To modify input text
## you need to modify "input text" in "process.py"

# To see the selected pictures 
## goto data/save/ directory

### lastupdated 2023 Aug 30
- 2023 Aug 30: added a vocaburary dict option in Tfidifvectorization
-            : changed ngram_range(1,2) --> (1,3)
