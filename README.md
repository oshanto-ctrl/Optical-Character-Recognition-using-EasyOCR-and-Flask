# Optical-Character-Recognition-using-EasyOCR-and-Flask

# Sentiment Analysis API

## Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Project Folder Structure](#project-folder-structure)
* [Walkthrough](#walkthrough)
* [Output](#output)
* [Evaluation](#evaluation)

## Introduction
An optical character recognition project of python, Flask framework with Easy-OCR integration.
User can upload digital images of writing and select languages then output of the project shows
the characters or texts from the digital images as a text format.

## Technologies
Project is created with:
* Python version: 3.10.6
* Flask Framework version: 2.2.2
* Easy-OCR: https://github.com/JaidedAI/EasyOCR
* HTML5
* CSS3

## Project Folder Structure
Folder name: sentiment_analysis_api
Subfolder and files: 

-static
    - css
    | style.css
    - images
    | Pictures for upload.

-templates
    | base.html
    | index.html
    | upload_image.html
    | success.html

app.py

## Walkthrough
### Instruction to run the project:
------------------------------------------------------
#### Front page of web application
![homepage](https://github.com/oshanto-ctrl/Optical-Character-Recognition-using-EasyOCR-and-Flask/assets/55896261/832721cf-96b8-42cc-b283-543db5660412)

#### Upload Image
![upload_image](https://github.com/oshanto-ctrl/Optical-Character-Recognition-using-EasyOCR-and-Flask/assets/55896261/68c0c2b6-798f-4f9b-b762-051539646d27)

#### Select desired image from folder
![choose_desired_image](https://github.com/oshanto-ctrl/Optical-Character-Recognition-using-EasyOCR-and-Flask/assets/55896261/cde180b6-9e9d-4422-b35d-88ff23e264ba)

#### Successfully Submit the desired image
![submit_image](https://github.com/oshanto-ctrl/Optical-Character-Recognition-using-EasyOCR-and-Flask/assets/55896261/7a22c149-4655-48d1-a88e-f90810ff4450)



Install virtual environment

>> py -m pip install --user virtualenv 

create a virtual environment in OCR directory

>> python -m venv venv

Start virtual environment:

>> venv\Scripts\activate


install flask

>> pip install flask

install easyocr module

>> pip install easyocr

Now, set the flask app for app.py file

>> set FLASK_APP=app.py

now, run the file.

>> flask run

This project will be available at browser with localhost

127.0.0.1:5000 url.

Then follow the procedures input and output.


## Output

Output can be found by uploading images.

#### Desired Output
![desired_output](https://github.com/oshanto-ctrl/Optical-Character-Recognition-using-EasyOCR-and-Flask/assets/55896261/edb0274f-4bff-49d8-91f9-a886f417eb3d)



## Evaluation

This program is to learn the flask framework and how to integrate other functionalites to flask app.
Future work planned:
a) No previous language selection
b) Dynamic recognition of the text/characters and output the result.

Thank you. :)

