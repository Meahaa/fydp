import processing.serial.*; //import the Serial library

 Serial myPort;  //the Serial port object
 String val;
 boolean firstContact = false;

Table dataTable; //table where we will read in and store values. You can name it something more creative!
 
//int numReadings = 10; //keeps track of how many readings you'd like to take before writing the file. 
//int readingCounter = 0; //counts each reading to compare to numReadings. 
 
String fileName;

int xPos = 1;         // horizontal position of the graph 
int lastxPos=1;
int lastheight=0;
int lastheight2=0;
float inByte;
float inByte2;

void setup()
{
  size(600, 400);    //make our canvas 200 x 200 pixels big
  background(0);      // set inital background:
  
  myPort = new Serial(this, Serial.list()[1], 115200); //  initialize your serial port and set the baud rate
  myPort.bufferUntil('\n'); 
  
  dataTable = new Table();
  
  dataTable.addColumn("id"); //This column stores a unique identifier for each record. We will just count up from 0 - so your first reading will be ID 0, your second will be ID 1, etc. 
  
  //the following adds columns for time. You can also add milliseconds. See the Time/Date functions for Processing: https://www.processing.org/reference/ 
  dataTable.addColumn("year");
  dataTable.addColumn("month");
  dataTable.addColumn("day");
  dataTable.addColumn("hour");
  dataTable.addColumn("minute");
  dataTable.addColumn("second");
  
  //the following are dummy columns for each data value. Add as many columns as you have data values. Customize the names as needed. Make sure they are in the same order as the order that Arduino is sending them!
  dataTable.addColumn("sensor1");
  dataTable.addColumn("sensor2");
  
  
}

void serialEvent(Serial myPort) {
//put the incoming data into a String - 
//the '\n' is our end delimiter indicating the end of a complete packet
val = myPort.readStringUntil('\n');
//make sure our data isn't empty before continuing
if (val != null) {
  //trim whitespace and formatting characters (like carriage return)
  val = trim(val);
  //println(val); 
  
  float[] sensorVal = float(split(val, ','));
  // list[0] is now "Chernenko", list[1] is "Andropov"...
  print(sensorVal[0]);
  print(",");
  println(sensorVal[1]);
  
  inByte = sensorVal[0];           // convert to a number.
  inByte = map(inByte, 0, 150, 0, height); //map to the screen height.
  inByte2 = sensorVal[1];           // convert to a number.
  inByte2 = map(inByte2, 0, 150, 0, height); //map to the screen height.
 
  
    
  //float sensorVals[] = float(split(val, ',')); //parses the packet from Arduino and places the valeus into the sensorVals array. I am assuming floats. Change the data type to match the datatype coming from Arduino. 
    
    TableRow newRow = dataTable.addRow(); //add a row for this new reading
    newRow.setInt("id", dataTable.lastRowIndex());//record a unique identifier (the row's index)
  
     //record time stamp
    newRow.setInt("year", year());
    newRow.setInt("month", month());
    newRow.setInt("day", day());
    newRow.setInt("hour", hour());
    newRow.setInt("minute", minute());
    newRow.setInt("second", second());
    
    //record sensor information. Customize the names so they match your sensor column names. 
    newRow.setFloat("sensor1", sensorVal[0]);
    newRow.setFloat("sensor2", sensorVal[1]);
  
  //readingCounter++; //optional, use if you'd like to write your file every numReadings reading cycles
  }
      ////saves the table as a csv in the same folder as the sketch every numReadings. 
    //if (readingCounter % numReadings ==0)//The % is a modulus, a math operator that signifies remainder after division. The if statement checks if readingCounter is a multiple of numReadings (the remainder of readingCounter/numReadings is 0)
    //{
      saveTable(dataTable, "highknees.csv"); //Woo! save it to your computer. It is read
    //}

}

void draw()
{
    line(lastxPos, lastheight, xPos, height - inByte); 
    lastxPos= xPos;
    lastheight= int(height-inByte);
    stroke(127,34,255);     //stroke color
    strokeWeight(4);        //stroke wider

    line(lastxPos, lastheight2, xPos, height - inByte2); 
    lastxPos= xPos;
    lastheight2= int(height-inByte2);
    stroke(225,34,123);     //stroke color
    strokeWeight(4);        //stroke wider

    // at the edge of the window, go back to the beginning:
    if (xPos >= width) {
      xPos = 0;
      lastxPos= 0;
      background(0);  //Clear the screen.
    } 
    else {
      // increment the horizontal position:
      xPos++;
    }
}