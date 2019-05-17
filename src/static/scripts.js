var displayItems = [
    new ImageItem("imgs/NMeng.jpg", 800, 480),
    new MeasurementItem("temperature", "temperature", 2),
    new MeasurementItem("humidity", "humidity", 2),
    new MeasurementItem("pressure", "pressure", 3),
    new MeasurementItem("Color temperature", "light temperature", 2),
    new MeasurementItem("CO2", "CO<sub>2</sub>", 2),
    new MeasurementItem("O2", "oxygen", 3),
    new MeasurementItem("TVOC", "volatile compounds", 2),
    new MeasurementItem("PM10", "PM<sub>10</sub>", 2),
    new MeasurementItem("PM2.5", "PM<sub>2.5</sub>", 2),
    new ImageItem("imgs/NMsrp.jpg", 800, 480),
    new MeasurementItem("temperature", "температура", 2),
    new MeasurementItem("humidity", "влажност ваздуха", 2),
    new MeasurementItem("pressure", "притисак", 3),
    new MeasurementItem("Color temperature", "температура светла", 2),
    new MeasurementItem("CO2", "CO<sub>2</sub>", 2),
    new MeasurementItem("O2", "кисеоник", 3),
    new MeasurementItem("TVOC", "лако испарљива органска једињења", 2),
    new MeasurementItem("PM10", "PM<sub>10</sub>", 2),
    new MeasurementItem("PM2.5", "PM<sub>2.5</sub>", 2),
];


var randomItems = [];

var updateInterval = null;
var updateDisplayInterval = null;
var changeDisplayMeasurementInterval = null;
var values = null;
var imgPresentInterval = [3, 6];
var clickswap = true;

var refreshTime_ms = 1000;
var changeTime_ms = 10000;
var isTestEnvironment = true;

// Get the JSON data using jquery
function updateValues(){
    $.getJSON("/measurements.json", success=function(data){values=data;});
}

function gotRandomImgs(data){
    imgFilenames = data.imgs;
    for(i = 0; i<imgFilenames.length; i++){
        randomItems += [new ImageItem(imgFilenames, 800, 480)];
    }
}

function getRandomImgs(){
    $.getJSON("/randimgs_list.json", success=gotRandomImgs);
}
// Perform a display update (change the displayed values)
function updateDisplay(){
    if(values){
        displayItems[currentIdx].display();
    }
}

function getRandomIncrement(){
    Math.floor(Math.random() * (imgPresentInterval[1] - imgPresentInterval[0])) + imgPresentInterval[0];
}

var nextRandomImgIdx = getRandomIncrement();
var currentIdx = 0;
var currentRandIdx = 0;

// Change the measurement idx
function changeDisplayMeasurement(){
    currentIdx = (currentIdx + 1) % displayItems.length;
    if(currentIdx == nextRandomImgIdx & randomItems){
        currentDisplayItem = randomItems[currentRandIdx];
        currentRandIdx = (currentRandIdx + 1) & randomItems.length;
        nextRandomImgIdx += getRandomIncrement();
        currentIdx--;
    }else{
        currentDisplayItem = displayItems[currentRandIdx];
    }
    if(currentIdx == 0){
        currentRandIdx = getRandomIncrement();

    }
    console.log("Changed")
}

function mainDivSwyped(e){
    direction = e.detail.data[0].currentDirection;
    if(!direction || (direction > 100 && direction < 260)){
        console.log("swiped")
        clearInterval(changeDisplayMeasurementInterval);
        changeDisplayMeasurementInterval = setInterval(changeDisplayMeasurement,changeTime_ms);
        changeDisplayMeasurement();
        updateDisplay();
    }
}

function mainDivClicked(){
    console.log("clicked")
    clearInterval(changeDisplayMeasurementInterval);
    changeDisplayMeasurementInterval = setInterval(changeDisplayMeasurement,changeTime_ms);
    changeDisplayMeasurement();
    updateDisplay();
}
function measurementBodyLoaded(){
    updateInterval = setInterval(updateValues, refreshTime_ms);
    updateDisplayInterval = setInterval(updateDisplay, refreshTime_ms);
    changeDisplayMeasurementInterval = setInterval(changeDisplayMeasurement, changeTime_ms);
    DisplayableItem.setMeasurementGetter(function(){return values;})

    if(clickswap){
        $("body").on('click', mainDivClicked)
    }else{
        touchRegion = ZingTouch.Region($("#outerDiv")[0]);
        touchRegion.bind($("#outerDiv")[0], 'swipe', mainDivSwyped);
    }
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