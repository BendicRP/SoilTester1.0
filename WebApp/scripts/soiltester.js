fetch("./dataFile.txt")
                .then(response => response.text())
                .then(text => displayText(text));

/*
    If dataFile is available,
        read dataFile.txt and parse each line into a new array element
        perform ForEach on array
*/
displayText = plantDataText => {

    var arrOfData = plantDataText.split("\n");
    
    // Grab document element by ID from index.html
    const dataDiv = document.querySelector('#plantData'); 
    
    /*  ForEach text of line in dataFile,
            create a <h2> tag,
            attach text to <pre> tag,
            attach element to DOM
    */ 
    arrOfData.forEach(data => {
        const headerElem = document.createElement('h3');
        const textElement = document.createElement('pre');
        textElement.innerText = data;
        headerElem.append(textElement);
        dataDiv.append(headerElem);
        
    });
};

