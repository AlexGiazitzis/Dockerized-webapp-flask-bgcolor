## Dockerized-webapp-flask-bgcolor
This is a simple flask webapp that displays a colored background and a dynamic greeting message. 

### Dynamic Color
The color can be specified in two different ways:

  1. As a command line argument with --hex-color as the argument.
  2. As an Environment variable APP_HEX_COLOR.
    
In any other case, a random color is generated.

Note 1: Color can be specified as a 3-byte hexadecimal number prefixed with the character '#'
Note 2: Command line argument precedes over environment variable.

### Dynamic Title
The dynamic greeting message can be specified in two different ways:

  1. As a command line argument with --title as the argument. Accepts any text message!
  2. As an Environment variable APP_TITLE. Accepts any text message.
    
In any other case, the static text "Cloud Computing - University of West Attica" is applied.

Note 3: Command line argument precedes over environment variable.
## Follow these steps in order to create your Dockerized-webapp-flask-bgcolor

1. First of all you have to clone this repository on your server.
```bash
    -$ mkdir -p ~/MyProjects
    -$ cd ~/MyProjects
    -$ git clone https://github.com/AlexGiazitzis/Dockerized-webapp-flask-bgcolor.git
                      OR via SSH
    -$ git clone git@github.com:AlexGiazitzis/Dockerized-webapp-flask-bgcolor.git
```
2. Now you have to build the Docker Image locally.
```bash
    -$ cd ~/MyProjects/Dockerized-webapp-flask-bgcolor
    -$ docker build . -t alexgzgs/webapp-flask-bgcolor:1.0
```
3. Now you have to spin up as many containers you want in different ports.

Random color and Static title without any command line argument nor environmental variable.
```bash
    -$ docker run -p 8002:8000 alexgzgs/webapp-flask-bgcolor:1.0
```
Blue color with environmental variable and the Static title:
```bash
    -$ docker run -p 8000:8000 -e APP_HEX_COLOR="#0000FF" alexgzgs/webapp-flask-bgcolor:1.0
```
Blue-purple color with command line argument and the static title:
```bash
    -$ docker run -p 8001:8000 alexgzgs/webapp-flask-bgcolor:1.0 --hex-color="#2617ff"
```
Red color and Dynamic title with environmental variables:
```bash
    -$ docker run -p 8003:8000 -e APP_HEX_COLOR="#FF0000" -e APP_COLOR="Test Title" alexgzgs/webapp-flask-bgcolor:1.0
```
Olive color and Dynamic title with command line arguments:
```bash
    -$ docker run -p 8004:8000 alexgzgs/webapp-flask-bgcolor:1.0 --hex-color="#808000" --title="Test Title"
```
