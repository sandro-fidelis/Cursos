<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="_css/estilo.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<div>
    <?php
        for($i=1; $i <= 10; $i++){
            echo "$i ";
        }

        echo"<br>";
        for($i=10; $i>=1; $i--){
            echo "$i ";
        }
        echo "<br>";

        for($i=0;$i<=100;$i+=10){
            echo "$i ";
        }
    ?>
</div>
    
</body>
</html>