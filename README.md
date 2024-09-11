# ECE4078_Practicals_2024
Repository for practicals of unit ECE4078 (Intelligent Robotics) offered in 2024.

# How to run this on your computer 

The recommended way to run notebooks this year is installing Docker on your local computer, please refer to [Local Set Up](#local-set-up). After successful installation, please consult [Running the notebook](#running-the-notebook) on how to run the notebooks.

Running on the cloud will also be possible **for certain weeks only as Deepnote recently changed their cell engine**. However, due to reliability issue, run it at your own risk, if the cloud method refuses to boot up during the lecture, there is nothing I can do! Please refer to [Weekly Notebook Cloud Compatibility](#cloud-compatibility) to check which cloud platform is available for said week.

# Homework

### Submission

There is only one `_exercise` notebook per week folder, submit only **ONE** `.ipynb` to Moodle. 

**NOTE**: if there are **TWO (2)** `.ipynb` in your Moodle submission box, you will receive 0 mark. Only submit **ONE (1)** `.ipynb` file to Moodle and any extra file that is relevant (there will be weeks where we require you to submit your notebook along with other files, such as `.pt` for the weight of neural network). 

### Grading Test Cases

At the end of each notebook with `_exercise` suffix (which is your homework), a few test cases are already included along with point allocations that we are going to use to grade you (at the end of the notebook). Note that we **may** test against additional test cases when I actually grade your notebook, so passing all the test cases will not guarantee obtaining the points but does increase your chance by a lot.

We use result-based **auto-grading** so there will be no partial mark for your solution!

# Local Set Up

For Windows and Mac User, the easiest way is to install [Docker Desktop](https://www.docker.com/products/docker-desktop/) on your computer. For Linux user, just install `docker` and `docker-compose` according to your distro.  The following sections will try to summarize the installation process on Windows and Mac.

## Installing Docker Desktop on Windows

### Installing WSL2
As a prerequisite, you have to WSL2 installed, if you are not sure you already installed it, please follow [this guide](https://docs.microsoft.com/en-us/windows/wsl/install-manual) Up to Step 5.  If you encounter any problem, please consult their [troubleshooting website](https://docs.microsoft.com/en-us/windows/wsl/troubleshooting#installation-issues), especially the part about enabling virtualization in your BIOS.

[This](https://youtu.be/cgXZ8Ecrdg0) is a video of my attempt.

### Installing Docker Desktop
If you already have WSL2 installed, consult this [webpage](https://docs.docker.com/desktop/install/windows-install/) for installation. It should be very straightforward, download the `.exe` file and install. 

[This](https://youtu.be/HbMPZl0Hd90) is a video of my attempt

## Installing Docker Desktop on MacOS
Download and install [Docker Desktop from here https://docs.docker.com/desktop/install/mac-install/](https://docs.docker.com/desktop/install/mac-install/).

NB: Chose the correct chip architecture for your notebook - with newer Macs having the Apple Silicon (~575MB download)

Follow the instructions there to install Docker or use the command line:

`sudo hdiutil attach Docker.dmg`

`sudo /Volumes/Docker/Docker.app/Contents/MacOS/install`

`sudo hdiutil detach /Volumes/Docker`


## Running the notebook 

- Open terminal, navigate the the repo folder
- Type `docker compose up --build --force-recreate`
- Copy link to web browser
- Start Using

Note, if you have problem with "name already exists", you can run:
- In Linux: `docker stop ece4078-prac && docker rm ece4078-prac`
- In Windows Powershell: `docker stop ece4078-prac; docker rm ece4078-prac`

This is a video of my attempt

If you have nvidia driver and NVIDIA container toolkit, and you want to run the docker with GPU, you can run

```
docker compose -f docker-compose-gpu.yml up --build --force-recreate
```

## Other Methods

Note that this repo is just a collection of jupyter notebooks, so if you already have a Python environment setup on your computer, feel free to use it. The repo includes `dependencies.txt` that lists all the dependencies (I didn't use `requirements.txt` because Deepnote will actually try to install stuff inside `requirements.txt` when it boots up which is redundant).

Sometimes the `ipywidgets` will not work properly out of the box, you have to look online yourself on how to enable that in your `jupyter notebook` or `jupyter lab` (It is pretty straightforward).

If you choose this, you have to figure it out yourself if you experience any problems. If the notebook simply refuse to run, and I cannot replicate the error you are experiencing, I will advise you to install Docker Desktop.

# Cloud Compatibility

Simply clicking on the badge of each week will land you in a page in which you can run notebooks. Please consult [How to use Deepnote](#how-to-use-deepnote) if this is your first time.

| 		| Cloud platform |
| ------------- | -------------- |
| Week00 | N/A   |
| Week01 | [<img src="https://deepnote.com/buttons/launch-in-deepnote-white-small.svg">](https://deepnote.com/workspace/ece4078-7216-bdf57084-6c08-4dea-a555-1d8b5ffa5d2c/project/Week01-2024-5ecbbe05-f20c-4c7e-a328-9f7c640b89a2)   |
| Week02 | [<img src="https://deepnote.com/buttons/launch-in-deepnote-white-small.svg">](https://deepnote.com/workspace/ece4078-7216-bdf57084-6c08-4dea-a555-1d8b5ffa5d2c/project/Week02-2024-87a2dcf2-1f5b-46d7-8692-2a33a908f7e6)   |
| Week03 | [<img src="https://mybinder.org/badge_logo.svg">](https://mybinder.org/v2/gh/tinsirius/Week03_2024/main) |
| Week04 | [<img src="https://deepnote.com/buttons/launch-in-deepnote-white-small.svg">](https://deepnote.com/workspace/ece4078-7216-bdf57084-6c08-4dea-a555-1d8b5ffa5d2c/project/Week04-2024-237c968e-007e-4462-be8e-8cb74c440c90)   |
| Week05 | [<img src="https://mybinder.org/badge_logo.svg">](https://mybinder.org/v2/gh/tinsirius/Week05_2024/main) |
| Week06 | [<img src="https://deepnote.com/buttons/launch-in-deepnote-white-small.svg">](https://deepnote.com/workspace/ece4078-7216-bdf57084-6c08-4dea-a555-1d8b5ffa5d2c/project/Week06-2024-158f8276-935d-4709-a2cc-e25fae6895a2) [<img src="https://mybinder.org/badge_logo.svg">](https://mybinder.org/v2/gh/tinsirius/Week06_2024/main)  |
| Week07 | [<img src="https://deepnote.com/buttons/launch-in-deepnote-white-small.svg">](https://deepnote.com/workspace/ece4078-7216-bdf57084-6c08-4dea-a555-1d8b5ffa5d2c/project/Week07-2024-7f3be395-a396-481b-a346-c76835aabccd) [<img src="https://mybinder.org/badge_logo.svg">](https://mybinder.org/v2/gh/tinsirius/Week07_2024/main)  |
| Week08 | [<img src="https://deepnote.com/buttons/launch-in-deepnote-white-small.svg">](https://deepnote.com/workspace/ece4078-7216-bdf57084-6c08-4dea-a555-1d8b5ffa5d2c/project/Week08-2024-f631e77f-03aa-4a24-b0b3-83469af1d718) [<img src="https://mybinder.org/badge_logo.svg">](https://mybinder.org/v2/gh/tinsirius/Week08_2024/main)  |


# How to use Deepnote

To launch this repo in Deepnote and run:
- Click the "Launch with Deepnote" badge.
- Press Duplicate button (If you don't have an account, create one).
- Once it is in your workspace, you can start playing with the notebook.

To do you home work:
- Work on the notebook with `_exercise.ipynb` suffix
- Download it locally to your machine
- Submit the file to Moodle before deadline.

A visual guide is included in this [video](https://youtu.be/zA7RqTRkFPA).

