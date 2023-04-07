# MyGame project 
First of all you should create an empty project. 

## Game
Write in terminal this code:

`
pip install pygame
`

You should copy _directories_:

___1. code___

___2. graphics___

___3. levels___

___4. audio___

To start game you should open the __main.py__ file in the ___code___ directory and run the project.

## Bot

Write in terminal this code:

`
pip install aiogram
`

You should copy directory __bot__

As well in _Telegram_ find bot with name __"BotFather"__. Then create new bot and give them name. "BotFather" send to you information in which you can find TOKEN.

<img src="https://user-images.githubusercontent.com/60139477/230595987-d3eb4d1a-46c5-4cce-ae48-9142bcd1dcc5.jpg" width="400">

Сreate a __.env__ file and add a variable named ___TOKEN___ to it and paste the value that "BotFather" sent you into this variable. Then write in terminal:

`
pip install  python-dotenv
`

To start bot you should write this code in terminal:

`
cd bot
`

And then this code (also in terminal):

`
python my_bot.py
`

## Tests

Write in the terminal this code:

`
pip install pytest
`

You should copy ___test/test_support___ directory and write in terminal this code:

`
pytest
`
