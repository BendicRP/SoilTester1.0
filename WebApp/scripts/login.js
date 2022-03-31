function check () {
	
		var username = document.getElementById('User').value;
	  	var password = document.getElementById('Pass').value;
		
		if( username == "user" && password == "admin")
		{
			alert("Correct Password");
			location.href= "nav.html";
		}
		else
		{
			alert("Wrong Password");
		}
}