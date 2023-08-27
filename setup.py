from setuptools import find_packages, setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='text2image',
      version="0.0.1",
      description="Pick up an image from Celeb A dataset with user text inputs",
      license="Le Wagon Tokyo",
      author="Le Wagon Tokyo #1299 Kana",
      author_email="contact@lewagon.org",
      install_requires=requirements,
      packages=find_packages(),
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
