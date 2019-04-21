<!DOCTYPE html>

<html>
    <?php

        session_start();

        $source = "http://127.0.0.1:5000";

        if(!isset($_SESSION['user'])){
            $_SESSION['user'] = array();
            $_SESSION['bot'] = array();
            $_SESSION['method'] = 'Regex';
            array_push($_SESSION['bot'], "Hi, Aku Charles");
            array_push($_SESSION['bot'], "Ada yang bisa kubantu?");
        }


        if(isset($_POST['querySubmitted'])){
            $_SESSION['method'] = $_POST['method'];
            $chat = $_POST['query'];
            if (isset($_POST['query']) && $_POST['query']!== ''){
                array_push($_SESSION['user'], $chat);

                $ch = curl_init();
                curl_setopt($ch, CURLOPT_URL, $source);
                curl_setopt($ch, CURLOPT_TCP_FASTOPEN, TRUE);
                curl_setopt($ch, CURLOPT_FTTPAPPEND, TRUE);
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
                curl_setopt($ch, CURLOPT_POST, TRUE);
                curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($_POST));
                var_dump(http_build_query($_POST));
                $result = json_decode(curl_exec($ch));
                curl_close($ch);
                array_push($_SESSION['bot'], $result);
            }

            unset($_POST['querySubmitted']);
            header("Location: ".$_SERVER['PHP_SELF']);
        }
    ?>

    <head>
        <title>Chatbot Prototype</title>
        <link rel ="stylesheet" href="style.css">
        <meta content="width=device-width, initial-scale=1" name="viewport" />
    </head>

    <body>
    <form class="input" name="input" method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
        <div class = "wall"><img src ="star.svg"></div>

        <div class = "credits">
            <p class = "creditsValue">This interactive chat bot is made for algorithm strategy assignment. The bot implements multiple different algorithm for string matching between queries and questions. Bari, Gama, Akhmal &copy; 2019</p>
        </div>
    
        <div class = "pickMethod">
            <select class= "option" name="method">
                <option value ="Regex">Regex</option>
                <option value ="KMP">Knuth-Morris-Pratt</option>
                <option value ="BM">Boyer-Moore</option>
            </select>
        </div>

        <div class = "chatbox">
            <div class = "logs" id="logs">
                        <div class ="chat bot">
                            <div class = "profile"><img src="bot3.gif"></div>
                            <p class = "message"><?= $_SESSION['bot'][0]?></p>
                        </div>
                        <div class ="chat bot">
                            <div class = "profile"><img src="bot3.gif"></div>
                            <p class = "message"><?= $_SESSION['bot'][1]?></p>
                        </div>
            <?php
                    $size = sizeof($_SESSION['user']);
                    for($i=0; $i < $size; $i++){?>

                        <div class ="chat user">
                            <p class = "message"><?= $_SESSION['user'][$i]?></p>
                        </div>

                        <div class ="chat bot">
                            <div class = "profile"><img src="bot3.gif"></div>
                            <p class = "message"><?= $_SESSION['bot'][$i+2]->data?></p>
                        </div>

                        <?php
                    }?>
            </div>

            <script>
                var objDiv = document.getElementById("logs");
                objDiv.scrollTop = objDiv.scrollHeight;
            </script>
            
            <div class="queries">
                <textarea name="query" autofocus></textarea>
                <audio id="soundSend" src="send.ogg" preload="auto"></audio>
                <button onclick="document.getElementById('soundSend').play();">Ask</button>
                <?php usleep(250000);?>
            </div>
                    
            <input type="hidden" name="querySubmitted" value= "1"/>
        </div>

    </form>
    </body>
</html>