<html lang="en">
  <head>    
    <title> Navigations Page </title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<script src="./scripts/main.js"></script>
    <link rel="stylesheet" href="./css/nav.css">
	<link rel="stylesheet" href="./css/main.css">
  </head>  
  <body>
    <header>
       <h1> Options </h1>
	   <nav>
	   <button type="button"><a href="datagetter.html">Results</a></button>
	   <button type="button"><a href="index.html" id="nav">Navigations page</a></button>
	   <button type="button"><a href="soiltester.html" id="soiltester">Soil Tester</a></button>
	   <button type="button"><?PHP echo shell_exec("./python/file.py");?> Run Python Script</button>
	   </nav>
    </header>     
    <footer>
       <p>Group10 -CEG4920- Spring 2022</p>
    </footer>  
  </body>
</html>