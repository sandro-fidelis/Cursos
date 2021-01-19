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
        $n =isset ($_GET["num"])?$_GET["num"]:1;
    
        for($c = 1; $c<=10; $c++){
            $r = $n * $c;
            echo "$n X $c = $r<br>";
        }
    ?>
    <br>><a href="index02.php">Voltar</a>
</div>
    
</body>
</html>