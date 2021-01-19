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
        $frase = "Eu vou estudar PHP";
        $count = str_word_count($frase,0);//contar
        echo $count;
        echo"<br>";
        $count = str_word_count($frase,1);//criar vetor
        print_r($count);
        echo"<br>";
        $count = str_word_count($frase,2);//criar vetor e mostar a posição da string na frase
        print_r($count);

    ?>
</div>
    
</body>
</html>