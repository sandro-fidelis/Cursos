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
        function soma($a,$b){
            $s = $a + $b;
            echo "A soma vale $s<br>";
        }
        soma(3,4);
        $x = 9;
        $y = 15;
        soma($x,$y);
    ?>
</div>
    
</body>
</html>