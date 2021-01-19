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
    <pre>
    <?php
        $v = array("nome" =>"Ana",
                    "idade" => 23,
                    "peso"=>65.5);
        print_r($v);
        foreach($v as $k => $c){ // cada vetor "$v" como "$k" associado a "$c" 
            echo "o campo $k possui o conteúdo $c <br>";
        }
    ?>
    </pre>
</div>
    
</body>
</html>