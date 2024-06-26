# Progature: Programming Adventure Game
Welcome to the epic world of Progature! 🚀 It's not just a Python programming game; it's your ticket to an **RPG (Role-Playing Game)** adventure in the real life.

## Run the game
first install requirements
```bash
pip install -r requirements.txt
```
then run ``install.py``
```bash
python progature/install.py
```
after installation run ``run.py``
```bash
python progature/run.py
```

## Main Page
![Progature Image](/docs/docs/images/main_page.png)

## Chapter Page 
![Progature Image](/docs/docs/images/chapter_page.png)

# Description
**Progature** is a programmig advanture game, games are stored in ``.json`` format and there are several parts in games. <br>
``Game``, ``Chapter``, ``Level``, ``Quest`` are 4 parts of our app.

### Game
**Game** component contains all the data of a game, each object of this component is a ``.json`` file.

### Chapter
**Chapter** is a part of **Game** component, each **Game** has several **Chapter**'s.

### Level
**Level** is a part of **Chapter** component, each **Chapter** has several **Level**'s.

### Quest
**Quest** is a part of **Level** component, each **Level** hs sevaral **Quest**'s.
