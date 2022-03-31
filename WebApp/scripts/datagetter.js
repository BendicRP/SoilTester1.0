        document.getElementById("data")
            .addEventListener("change", function() {
              
            var filegetter = new FileReader();
            filegetter.onload=function(){
                document.getElementById("output")
                        .textContent=filegetter.result;
            }
              
            filegetter.readAsText(this.files[0]);
        })