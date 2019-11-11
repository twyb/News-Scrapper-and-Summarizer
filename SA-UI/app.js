function Search(){
    var searchInput = document.getElementById("myInput").value;
    database = ["Hong Kong"];
    for (i=0;i<database.length ;i++) {
        if (searchInput.toUpperCase() == database[i].toUpperCase()){
            console.log("Do something");
        } else {
            console.log("Nth");
        }
    }
}

//logic to draw table if search result is there
function drawingTablesIfSearch(){

}

//method 1 of drawing table
function drawTable() {
    console.log("hi");
    var totalRows = 5;
    var cellsInRow =3;
    var min = 1;
    var max = 10;
    // getting search result
    // var searchInput = document.getElementById("myInput").value;
    // get the reference for the body
    var div1 = document.getElementById('topic-table');

    // creates a <table> element
    var tbl = document.createElement("table");

    // creating rows
    for (var r = 0; r < totalRows; r++) {
        var row = document.createElement("tr");
     
     // create cells in row
         for (var c = 0; c < cellsInRow; c++) {
            var cell = document.createElement("td");
            getRandom = Math.floor(Math.random() * (max - min + 1)) + min;
            var cellText = document.createTextNode(Math.floor(Math.random() * (max - min + 1)) + min);
            cell.appendChild(cellText);
            row.appendChild(cell);
        }           
        
        tbl.appendChild(row); // add the row to the end of the table body
    }

 div1.appendChild(tbl); // appends <table> into <div1>
}

function dataTable(){
    //function not done
    var searchInput = document.getElementById("myInput").value 
    //doing check for matching query to database -not done

        var list = [ 
            { "col_1": "val_11", "col_3": "val_13" }, 
            { "col_2": "val_22", "col_3": "val_23" }, 
            { "col_1": "val_31", "col_3": "val_33" } 
        ]; 
                 
        function constructTable(selector) { 
              
            // Getting the all column names 
            var cols = Headers(list, selector);   
   
            // Traversing the JSON data 
            for (var i = 0; i < list.length; i++) { 
                var row = $('<tr/>');    
                for (var colIndex = 0; colIndex < cols.length; colIndex++) 
                { 
                    var val = list[i][cols[colIndex]]; 
                      
                    // If there is any key, which is matching 
                    // with the column name 
                    if (val == null) val = "";   
                        row.append($('<td/>').html(val)); 
                } 
                  
                // Adding each row to the table 
                $(selector).append(row); 
            } 
        } 
          
        function Headers(list, selector) { 
            var columns = []; 
            var header = $('<tr/>'); 
              
            for (var i = 0; i < list.length; i++) { 
                var row = list[i]; 
                  
                for (var k in row) { 
                    if ($.inArray(k, columns) == -1) { 
                        columns.push(k); 
                          
                        // Creating the header 
                        header.append($('<th/>').html(k)); 
                    } 
                } 
            } 
              
            // Appending the header to the table 
            $(selector).append(header); 
                return columns; 
        } 
}

function constructTable(selector) { 
    console.log("build");
    var list = [ 
        { "Topic": "val_11","Number of Discussion":"val_20" ,"Popularity Score": "val_13" }, 
        { "Number of Discussion": "val_22", "Popularity Score": "val_23" }, 
        { "Topic": "val_31", "Popularity Score": "val_33" } 
    ]; 
    // Getting the all column names 
    var cols = Headers(list, selector);   

    // Traversing the JSON data 
    for (var i = 0; i < list.length; i++) { 
        var row = $('<tr/>');    
        for (var colIndex = 0; colIndex < cols.length; colIndex++) 
        { 
            var val = list[i][cols[colIndex]]; 
              
            // If there is any key, which is matching 
            // with the column name 
            if (val == null) val = "";   
                row.append($('<td/>').html(val)); 
        } 
          
        // Adding each row to the table 
        $(selector).append(row); 
    } 
} 
  
function Headers(list, selector) { 
    var columns = []; 
    var header = $('<tr/>'); 
      
    for (var i = 0; i < list.length; i++) { 
        var row = list[i]; 
          
        for (var k in row) { 
            if ($.inArray(k, columns) == -1) { 
                columns.push(k); 
                  
                // Creating the header 
                header.append($('<th/>').html(k)); 
            } 
        } 
    } 
      
    // Appending the header to the table 
    $(selector).append(header); 
        return columns; 
}