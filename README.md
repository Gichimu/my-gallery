## Project Name
Personal Gallery

## Brief description of website.
The project is a python-based application built with the Django framework that showcases personal images and how to manage them through an admin panel.

## Main contributors
- [Eric Gichimu](https://github.com/Gichimu)

## About the author
The author is a moringa core student studying software development.

## Application specifications

The application requires a user to follow the live link provided in the space below. 
* When a user first lands on the application, he/she meets a beautiful user front page interface that has a navbar at the top which has a home link and a search bar. The search bar enables the user to search for different categories of images such as food, nature, tech, etc.
* The landing page also features an array of images which have been added recently and each of which upon clicking displays a modal with an enlarged version of the image and the image's details.
* The user can access an admin panel by login in with a preset username and password. These, the user needs to create by opening a cloning the project, navigating to the project folder and opening a terminal and typing 'heroku run python3.6 manage.py createsuperuser'. He will then be prompted to enter a username, email and password which he will use to login to the panel.
* Upon login into the panel, the user can add images by clicking on the 'plus' sign and adding information in the required fields and clicking save.
* For best practices, the user is required to enter an image name with dashes (-) between the spaces. 
 
## Languages
The application is written in American english.

## Setup/Installation Requirements
To run the application on a local server, the user needs to install the following dependencies alongside Python3.6 after which the project can be ran by typing the command 'python3.6 manage.py runserser'
* beautifulsoup4==4.8.1
* dj-database-url==0.5.0
* Django==1.11
* django-bootstrap4==1.1.1
* django-heroku==0.3.1
* gunicorn==20.0.4
* Pillow==6.2.1
* psycopg2==2.8.4
* python-decouple==3.3
* pytz==2019.3
* soupsieve==1.9.5
* whitenoise==5.0.1

## Technologies Used
* The python language
* Django python framework
* The postgresql database management system


## Support and contact details
 Incase of any bugs encountered contact [gichimueric12@gmail.com]

## Website live link
[Personal Gallery](https://my-pics-gallery.herokuapp.com/)

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Gichimu/my-gallery/blob/master/LICENCE.md) for details