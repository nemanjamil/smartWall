var wantedMeasurements = [
    "temperature", 
    "humidity", 
    "pressure", 
    "Color temperature", 
    "CO2", 
    "O2", 
    "TVOC",
    "PM10",
    "PM2.5"];
var nameMappings = [
    'Temperature', 
    "Humidity", 
    "Pressure",
    "Light temperature", 
    "CO<sub>2</sub>",
    "O<sub>2</sub>", 
    "Volatile compounds",
    "PM<sub>10</sub>",
    "PM<sub>2.5</sub>"];
var significantDigits = [2,2,3,2,2,3,2,2,2]
var updateInterval = null;
var updateDisplayInterval = null;
var changeDisplayMeasurementInterval = null;
var values = null;

var currentIdx = 0;
var refreshTime_ms = 1000;
var changeTime_ms = 10000;
// Rounds a measured value to two significant digits
// It looks ugly otherwise
function getRoundedValue(number, precision=2){
    return parseFloat(number.toPrecision(precision));
}

// Get the JSON data using jquery
function updateValues(){
    $.getJSON("/measurements.json", success=function(data){values=data;});
}

// Perform a display update (change the displayed values)
function updateDisplay(){
    if(values){
        var currentMeasurementID = wantedMeasurements[currentIdx];
        var currentMeasurementName = nameMappings[currentIdx];
        var currentSignificantDigits = significantDigits[currentIdx];
        var currentMeasurement = values[currentMeasurementID];

        var displayValue = getRoundedValue(currentMeasurement.value, currentSignificantDigits);
        var displayUnit = currentMeasurement.unit;    
        $("#measurementName").html(currentMeasurementName);
        $("#measurementValue").html(String(displayValue) + " " + displayUnit);
    }
}

// Change the measurement idx
function changeDisplayMeasurement(){
    currentIdx = (currentIdx + 1) % wantedMeasurements.length;
}
function mainDivClicked(){
   clearInterval(changeDisplayMeasurementInterval);
   changeDisplayMeasurementInterval = setInterval(changeDisplayMeasurement,changeTime_ms);
   changeDisplayMeasurement();
   updateDisplay();
}


$(
    function(){
        $("body").bind('click', mainDivClicked);
        updateInterval = setInterval(updateValues, refreshTime_ms);
        updateDisplayInterval = setInterval(updateDisplay, refreshTime_ms);
        changeDisplayMeasurementInterval = setInterval(changeDisplayMeasurement, changeTime_ms);
        updateValue();
    }
)