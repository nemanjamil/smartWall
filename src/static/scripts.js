var displayItems = [
    new MeasurementItem("temperature", "Temperature", 2),
    new MeasurementItem("humidity", "Humidity", 2),
    new MeasurementItem("pressure", "Pressure", 3),
    new MeasurementItem("Color temperature", "Light temperature", 2),
    new MeasurementItem("CO2", "CO<sub>2</sub>", 2),
    new ImageItem("static/imgs/sensor.svg", 400, 500),
    new MeasurementItem("O2", "O<sub>2</sub>", 3),
    new MeasurementItem("TVOC", "Volatile compounds", 2),
    new MeasurementItem("PM10", "PM<sub>10</sub>", 2),
    new MeasurementItem("PM2.5", "PM<sub>2.5</sub>", 2),
    new ImageItem("static/imgs/noviModel.png", 300, 200)
];

var updateInterval = null;
var updateDisplayInterval = null;
var changeDisplayMeasurementInterval = null;
var values = null;

var currentIdx = 0;
var refreshTime_ms = 1000;
var changeTime_ms = 10000;


// Get the JSON data using jquery
function updateValues(){
    $.getJSON("/measurements.json", success=function(data){values=data;});
}

// Perform a display update (change the displayed values)
function updateDisplay(){
    if(values){
        displayItems[currentIdx].display();
    }
}

// Change the measurement idx
function changeDisplayMeasurement(){
    currentIdx = (currentIdx + 1) % displayItems.length;
    console.log("Changed")
}

function mainDivClicked(){
    console.log("clicked")
    clearInterval(changeDisplayMeasurementInterval);
    changeDisplayMeasurementInterval = setInterval(changeDisplayMeasurement,changeTime_ms);
    changeDisplayMeasurement();
    updateDisplay();
}
console.log(mainDivClicked)
function measurementBodyLoaded(){
    updateInterval = setInterval(updateValues, refreshTime_ms);
    updateDisplayInterval = setInterval(updateDisplay, refreshTime_ms);
    changeDisplayMeasurementInterval = setInterval(changeDisplayMeasurement, changeTime_ms);
    DisplayableItem.setMeasurementGetter(function(){return values;})
    $("body").bind('click', mainDivClicked)
    updateValues();
}

function clearLogs(){
    if(confirm("Are you sure that you want to clear all logfiles. This cannot be undone!")){
        $.get("/clearAll") 
            .done(function(data) {
                alert(data);
                location.reload(true);
            });
    }else{
        location.reload(true);
    }
}