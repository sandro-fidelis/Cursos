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
    <form action="02tabuada.php" method="get">
        <select name="num" id="num">
            <?php
                for($c = 1;$c<=10;$c++){
                    echo "<option>$c</option>";
                }
            ?>
        </select>
        <input type="submit" value="Tabuada">
    </form>
</div>
    
</body>
</html>