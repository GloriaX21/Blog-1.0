# NatureBlog 1.0 - Django Blog Application

This is a Blog Web Application, written in <strong>Django 3</strong>. 

<strong>This application allows the creation and publication of posts</strong>. The posts are listed in the main layout, and it's possible to see the Title, the Published Date, and a small part of their Text Content. By clicking on the Post's Link you are interested in, you can see all of its content.

![Image-Intro-Webapp](images/image_intro.png)

 ## Table Of Contents

 * General Info
 * Technologies
 * Setup
 * Status
 
 ## General Info
 


![Image-Intro-Webapp](images/image_blog_layout1.png)

 ## Technologies Used

  ### Languages Used

  * [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))
  * [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3)
  * [SQLite](https://en.wikipedia.org/wiki/SQLite)

  ### Frameworks, Libraries & Programs Used

  1. [Django3](https://en.wikipedia.org/wiki/Django_(web_framework))
  2. [SASS](https://en.wikipedia.org/wiki/Sass_(stylesheet_language))
  3. [Google Fonts](https://en.wikipedia.org/wiki/Google_Fonts)
  4. [Git](https://en.wikipedia.org/wiki/Git)
  5. [GitHub](https://en.wikipedia.org/wiki/GitHub)


 ## Setup

  To run this project on your machine you should use a <strong>Virtual Enviroment</strong> with <strong>Django3</strong> installed. It's necessary to have also <strong>Python3</strong> installed.

  It's recommended to follow the instructions below:
  
  ### Check Python Version/Install Python3

  1. Check if you have Python3 installed. Open the Terminal and type:
  ```bash
  python3
  ```

  You should get an output that shows you the Python version installed on yous OS. In case you don't get nothing check this guide to install the last version of Python3 [Python.org/downloads](https://www.python.org/downloads/)

  ### Install the Virtual Enviroment

  1. After that you installed Python3. Create and empty folder in your machine:
  ```bash
  mkdir django_projects
  ```

  2. Go inside the folder and install the <strong>Virtual Enviroment</strong>:
  ```bash
  python3 -m venv my_env
  ```  
    - <strong>my_env<strong> is the name of your Virtual Enviroment

  3. Activate the Vitual Enviroment:
  ```bash
  source my_env/bin/activate
  ``` 
  Whenever you would like to <strog>deactivate</strog> the Virtual Enviroment, type:
  ```bash
  source my_env/bin/deactivate
  ``` 

  ### Install Django3 Framework in the Virtual Enviroment with pip

  (With Python3 <strong>pip</strong> package manager comes installed. It's recommended to use <strong>pip3</strong>)

  1. Install Django3:
  ```bash
  pip3 install "Django==3.0.*"
  ```  

  2. Check that Django3 it's been successfully installed:
    ```bash
  python3
  >>> import django
  >>> django.get_version()
  '3.0.14'
  ``` 

  






