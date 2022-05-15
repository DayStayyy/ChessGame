# Flask chessgame

> Clamadieu-Tharaud Adrien
> Gélineau Benjamin
> Joyet Hugo

## Explaination

- The objective of the project was to create our own chess website made with flask and docker

## prerequisites

```
docker
flask
An ide
```

## Setup

- First you will need to git clone the project:

```
git@gitlab.com:benji.gelineau/chessgame.git
```

- Then you just need to do:

```
pip install -r requirements.txt
docker-compose up -d
python -m flask run
```

## Features

### Register/login

- First of all we have a login/register page that will allowed users to create accounts on
  ![](https://i.imgur.com/zdlNJOJ.png)

### Game Menu

- when you will be logged in, you will arrive on the game menu, you will be able to determine if you want to play versus an ia or against an another local player. You have also the possibility to manage your options and logout.
  ![](https://i.imgur.com/csS8UOq.png)

### Home

- And finally you have the game
  ![](https://i.imgur.com/zyBxvaR.png)
