<!DOCTYPE html>

<html>
    <head>
        <title>Chatbot Prototype</title>
        <link rel ="stylesheet" href="style.css">
    </head>

    <body>
        <div class = "wall"><img src ="star.svg"></div>
        <div class = "method">
            <select class= "option" name="Pick Method">
                <option value ="Regex">Regex</option>
                <option value ="KMP">Knuth-Morris-Pratt</option>
                <option value ="BM">Boyer-Moore</option>
            </select>
        </div>

        <div class = "credits">
            <p class = "creditsValue">This interactive chat bot is made for algorithm strategy assignment. The bot implements multiple different algorithm for string matching between queries and questions. Bari, Gama, Akhmal &copy; 2019</p>
        </div>

        <div class = "chatbox">
            <div class = "logs">
                <div class ="chat bot">
                    <div class = "profile"><img src="bot.svg"></div>
                    <p class = "message">Hi what can i help you with?</p>
                </div>

                <div class ="chat user">
                    <div class = "profile"><img src="avatar.svg"></div>
                    <p class = "message">Hey</p>
                </div>

                <div class ="chat bot">
                    <div class = "profile"><img src="bot.svg"></div>
                    <p class = "message">Hey what's up?</p>
                </div>

                <div class ="chat user">
                    <div class = "profile"><img src="avatar.svg"></div>
                    <p class = "message">who are you?</p>
                </div>

                <div class ="chat bot">
                    <div class = "profile"><img src="bot.svg"></div>
                    <p class = "message">I'm an autonomous program on a network (especially the Internet) that can interact with computer systems or users, especially one designed to respond or behave like a player in an adventure game.</p>
                </div>

                <div class ="chat user">
                    <div class = "profile"><img src="avatar.svg"></div>
                    <p class = "message">who created you?</p>
                </div>

                <div class ="chat bot">
                    <div class = "profile"><img src="bot.svg"></div>
                    <p class = "message">Bari, Gama, and Akhmal bring me into existence</p>
                </div>

            </div>

            <div class="query">
                <textarea autofocus></textarea>
                <audio id="soundSend" src="send.ogg" preload="auto"></audio>
                <button onclick="document.getElementById('soundSend').play();">Ask</button>
            </div>

        </div>
    </body>
</html>