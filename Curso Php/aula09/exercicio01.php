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
    if ($i >=18){
        $v = "já pode votar";
        $d = "já pode dirigir";
    }else {
        $v = "não pode votar";
        $d = "não pode dirigir";
    }
    echo "<br> Com essa idade voçê $v e também $d";
    ?>
</div>
</body>
</html>