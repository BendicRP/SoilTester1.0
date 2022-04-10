<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="./css/main.css">
  <script src = "./scripts/login.js"></script>
  <title>Login</title>
</head>

<?php
if(isset($_POST['submit'])){
$firstName = "First Name:".$_POST['firstName']."
";
$lastName = "Last Name:".$_POST['lastName']."
";
$file=fopen("dataFile.txt", "a");
fwrite($file, $firstName);
fwrite($file, $lastName);
fclose($file);
}
?>
<body>
  <main>
    <h1>Login</h1>
	<form method="post">
      <input type="text" name="firstName" placeholder="First Name" required autocomplete="off"> <br>
      <input type="text" name="lastName" placeholder="Last Name" required autocomplete="off"> <br>
      <input type="submit" name="submit" value="Submit">
    </form>
  </main>
</body>
<footer>
	<p>Group10 -CEG4920- Spring 2022</p>
</footer>
</html>
