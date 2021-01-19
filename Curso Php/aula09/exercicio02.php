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
    $a = isset ($_GET["ano"]) ?$_GET["ano"]:1900;
    $i = date("Y") - $a;
    echo "Voçê nasceu em $a e terá $i anos";
    if ($i < 16){
        $tipoVoto = "não vota";
    }
    elseif (($i >= 16 && $i <18) || ($i>65)){
            $tipoVoto = "voto opcional";
    }
    else{
            $tipoVoto = "voto obrigatório";
    }
    echo "<br> Para essa idade, $tipoVoto";
     ?>
</div>
</body>
</html>