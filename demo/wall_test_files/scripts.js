var wantedMeasurements = ["temperature", "humidity", "pressure", "Color temperature", "CO2", "TVOC"];
var nameMappings = ['Temperature', "Humidity", "Pressure", "Light temperature", "CO<sub>2</sub>", "Volatile compounds"];
var updateInterval = null;
var updateDisplayInterval = null;
var changeDisplayMeasurementInterval = null;
var values = null;

var currentIdx = 0;
var refreshTime_ms = 1000;
var changeTime_ms = 10000;
// Rounds a measured value to two significant digits
// It looks ugly otherwise
function getRoundedValue(number){
    return parseFloat(number.toPrecision(2));
}

// Get the JSON data using jquery
function updateValues(){
    $.getJSON("wall_test_files/measurements.json", success=function(data){values=data;});
}

// Perform a display update (change the displayed values)
function updateDisplay(){
    if(values){
        var currentMeasurementID = wantedMeasurements[currentIdx];
        var currentMeasurementName = nameMappings[currentIdx];
        var currentMeasurement = values[currentMeasurementID];
        var displayValue = getRoundedValue(currentMeasurement.value);
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
