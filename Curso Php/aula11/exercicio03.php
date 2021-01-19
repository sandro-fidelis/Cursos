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
       $i = isset ($_GET["i"])? $_GET["i"]:0;
       $f = isset ($_GET["f"])? $_GET["f"]:0;
       $inc = isset ($_GET["inc"])? $_GET["inc"]:0;

       while($i<$f){
          echo "$i<br>";
          $i = $i + $inc;
       }

       while($i>$f){
           echo "$i<br>";
            $i = $i - $inc;
       }
    ?>
    <a href="exercicio03.html">Voltar</a>
</div>
    
</body>
</html>