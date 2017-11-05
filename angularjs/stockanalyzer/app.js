var app= angular.module("myApp", ["chart.js"]);


  app.config(['ChartJsProvider', function (ChartJsProvider) {

    ChartJsProvider.setOptions({
      chartColors: ['#2C19F1', '#19F12C','#FE010D'],
      responsive: true,
	    options: {
    
    chartArea: {
					backgroundColor: 'red'
				}
  }

    });

    ChartJsProvider.setOptions('line', {
      showLines: false
	  	  
    });
  }]);

  app.controller("LineCtrl", ['$scope', '$timeout', function ($scope) {
    // Default data
  $scope.labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
  $scope.series = ['Stock A', 'Stock B','Stock C'];
  $scope.data = [
    [65, 59, 80, 81, 56, 55, 40],
    [28, 48, 40, 19, 86, 27, 90],
	[15, 5, 12, 63, 63, 27, 12],
  ];
  $scope.colors = [{
    fill: true,
    backgroundColor: "#FF6384"
}];
   
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };
  
  $scope.clickme = function () {
    var b = CSVToArray($scope.csv);
    $scope.labels=formatArrayColumn(b,0);

    $scope.series=formatArrayRow(b,0);
    $scope.data=formatArray(b);
}
  
 }]);

// Functions

function formatArray(table){
  var i;
  var z="[[";
  for (i=1;i<table[i].length-1;i++){
    z+=formatArrayColumn(table,i);
    z+="],["
   
  }
  z = z.slice(0, -1);
  z = z.slice(0, -1);
  z+="]";
  z=JSON.parse(z);
  return z;
}

  function formatArrayColumn(table,n){
     var i;
     var y="[";
    for (i=1;i<table.length;i++){
      y +='"'+table[i][n]+'",';

    }  
	//console.log(y);
    y = y.slice(0, -1);
    y+=']';
    // y=y.replace(', "undefined"','');
    y=JSON.parse(y);
    return y;
  
  }

// Generate ChartJS 
 function formatArrayRow(table,n){
     var i;
     var x="[";
    for (i=1;i<table[i].length-1;i++){
    
      x +='"'+table[n][i]+'",';

    }  
    x = x.slice(0, -1);
    x+=']';
    return JSON.parse(x);
  
  }

  
//CSVToArray function
  function CSVToArray(strData, strDelimiter) {

    strDelimiter = (strDelimiter || ",");
    var objPattern = new RegExp((
    "(\\" + strDelimiter + "|\\r?\\n|\\r|^)" +
    "(?:\"([^\"]*(?:\"\"[^\"]*)*)\"|" +
    "([^\"\\" + strDelimiter + "\\r\\n]*))"), "gi");
    var arrData = [[]];
    var arrMatches = null;

    while (arrMatches = objPattern.exec(strData)) {
        var strMatchedDelimiter = arrMatches[1];
        if (strMatchedDelimiter.length && (strMatchedDelimiter != strDelimiter)) {
            arrData.push([]);
        }

        if (arrMatches[2]) {
 
            var strMatchedValue = arrMatches[2].replace(
            new RegExp("\"\"", "g"), "\"");
        } else {

            var strMatchedValue = arrMatches[3];
        }

        arrData[arrData.length - 1].push(strMatchedValue);
    }
    return (arrData);
}



