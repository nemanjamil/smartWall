class DisplayableItem{
    constructor(){

    }
    display(){

    }
    static setMeasurementGetter(getter){
        DisplayableItem.measurementGetter = getter;
    }
    static getRoundedValue(number, precision){
        return parseFloat(number.toPrecision(precision));
    }
    
}
class MeasurementItem extends DisplayableItem{
    constructor(measurementName, displayName, precision=2){
        super()
        this.measurementName = measurementName;
        this.displayName = displayName;
        this.precision = precision;
    }
    display(){
        var measurement = DisplayableItem.measurementGetter()[this.measurementName];
        
        var measurementValue = DisplayableItem.getRoundedValue(measurement.value, this.precision);
        $("#measurementName").html(this.displayName);
        $("#measurementValue").html(String(measurementValue) + " " + measurement.unit);
        $("#logo").hide();
    }
}

class ImageItem extends DisplayableItem{
    constructor(imageSource, width=800, height=600){
        super()
        this.imageSource = imageSource;
        this.width = width;
        this.height = height;
        this.image = new Image()
        this.image.height = height
        this.image.src = this.imageSource;
        this.image.id = "logo";
        this.loaded = false;
        console.log("Loaded image");
    }
    display(){
        $("#logo").replaceWith(this.image);
        $("#measurementName").html("");
        $("#measurementValue").html("");
        $("#logo").show()
    }
}