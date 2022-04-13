<!DOCTYPE html>
<html>
<head>
    <title>Results</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="./css/main.css">
    <link rel="stylesheet" href="./css/datagetter.css">
</head> 
<body>
	<header>
		<h1> Results </h1>
		<nav>
		<button type="button"><a href="index.php" id="nav">Navigations page</a></button>
		</nav>
	</header>
<pre><?php
echo file_get_contents("dataFile.txt");
?> </pre>
	<footer>
       <p>Group10 -CEG4920- Spring 2022</p>
    </footer>  
</body>
  
</html>
