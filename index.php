<!DOCTYPE html>

<html>
    <?php

        session_start();

        $source = "http://127.0.0.1:5000";

        if(!isset($_SESSION['bot'])){
            $_SESSION['user'] = array();
            $_SESSION['bot'] = array();
            $_SESSION['method'] = 'Regex';
            array_push($_SESSION['bot'], "Hi, I am what can i help you with?");
        }

        if(isset($_POST['method'])){
            $_SESSION['method'] = $_POST['method'];
        }

        if(isset($_POST['querySubmitted'])){
            $chat = $_POST['query'];
            if (isset($_POST['query'])){
                array_push($_SESSION['user'], $chat);
                $ans = getResult($source, http_build_query($_POST));
                array_push($_SESSION['bot'], $ans);
            }

            unset($_POST['querySubmitted']);
            header("Location: ".$_SERVER['PHP_SELF']);
        }

        function getResult($url, $data){
            $source = curl_init($url);
            curl_setopt($source, CURLOPT_RETURNTRANSFER, TRUE);
            curl_setopt($source, CURLOPT_POST, 1);
            curl_setopt($source, CURLOPT_POSTFIELDS, $data);
            var_dump($data);
            $tempResult = curl_exec($source);
            curl_close($source);
 
            $result = json_decode($tempResult);
            return $result;
        }

    ?>

    <head>
        <title>Chatbot Prototype</title>
        <link rel ="stylesheet" href="style.css">
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
            <div class = "logs">
                        <div class ="chat bot">
                            <div class = "profile"><img src="bot2.gif"></div>
                            <p class = "message"><?= $_SESSION['bot'][0]?></p>
                        </div>
            <?php
                    $i = 0;
                    while($i < sizeof($_SESSION['user'])){?>

                        <div class ="chat user">
                            <p class = "message"><?= $_SESSION['user'][$i]?></p>
                        </div>

                        <div class ="chat bot">
                            <div class = "profile"><img src="bot2.gif"></div>
                            <p class = "message"><?= $_SESSION['bot'][$i+1]->data?></p>
                        </div>

                        <?php
                    $i++;
                    }?>
            </div>

            <div class="queries">
                <textarea name="query" autofocus></textarea>
                <audio id="soundSend" src="send.ogg" preload="auto"></audio>
                <button onclick="document.getElementById('soundSend').play();">Ask</button>
            </div>

            <input type="hidden" name="querySubmitted" value= "1"/>
        </div>
    </form>
    </body>
</html>