<?php
$number = $_POST['number'];
$text = $_POST['text'];

$output = [];
$result = 0;
exec("python3 process.py $number $text", $output, $result);

if($result !== 0) {
  echo "<h1 style='color: red'>$output[0]</h1>";
  echo "<a href='/form.php'>Back to form</a>";
  exit;
}
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assignment5 Process | IST105</title>
  </head>
  <body>
    <?php foreach($output as $key=>$str): ?>
      <?= str_contains($str, "Number Puzzle") || str_contains($str, "Text Puzzle") || str_contains($str, "Treasure Hunt") ? "<h2>$str</h2>" : "<p>$str</p>" ?>
    <?php endforeach ?>
    <a href='/form.php'>Back to form</a>
  </body>
</html>
