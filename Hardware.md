# **Hardware Integration**

## **UART Communication**
A modified copy of`detect.py` named [detect_communicate.py`](./scripts/detect_communicate.py) was created to enable hardware communication:
- The scripts initialize a communication with the serial 
  ```python
     try:
        serial_port = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
        print("Serial communication initialized.")
     except Exception as e:
        print(f"Error initializing serial communication: {e}")
        serial_port = None
  ```
  So you have  to use the appropriate port at which your arduino  is connected on
  ```python
    if serial_port:
        signal = f"{label}\n"  # Format signal with newline
        try:
            serial_port.write(signal.encode())  # Send signal
            print(f"Signal sent: {signal.strip()}")
        except Exception as write_error:
            print(f"Error sending signal: {write_error}")
  ```
  the above codes are used to send  a detected class (label) and the below are used to  close the port after Performing inference
  ```python
    if serial_port:
        serial_port.close()
        print("Serial communication closed.")
  ```
- The script are already in [`detect_communicate.py`](./scripts/detect_communicate.py) sends detected classes (e.g., car plate numbers) over a serial connection.
- Arduino reads the class and performs corresponding actions (e.g., lighting LEDs).

### **Arduino Code**
Below is the Arduino code used to control LEDs based on the detected number plate class:

```C++
// Define the LED pins (9 to 13)
const int ledPin9 = 9;
const int ledPin10 = 10;
const int ledPin11 = 11;
const int ledPin12 = 12;
const int ledPin13 = 13;

void setup() {
  // Start the Serial communication at 9600 baud rate
  Serial.begin(9600);

  // Initialize the LED pins as OUTPUT
  pinMode(ledPin9, OUTPUT);
  pinMode(ledPin10, OUTPUT);
  pinMode(ledPin11, OUTPUT);
  pinMode(ledPin12, OUTPUT);
  pinMode(ledPin13, OUTPUT);

  // Turn off all LEDs initially
  digitalWrite(ledPin9, LOW);
  digitalWrite(ledPin10, LOW);
  digitalWrite(ledPin11, LOW);
  digitalWrite(ledPin12, LOW);
  digitalWrite(ledPin13, LOW);
}

void loop() {
  // Check if data is available to read
  if (Serial.available() > 0) {
    // Read the entire line from the Serial input
    String inputLine = Serial.readStringUntil('\n');  // Reads until a newline character
    
    // Remove leading and trailing whitespace
    inputLine.trim();  // .trim() removes spaces from both ends of the string

    // Print the received line to the Serial Monitor
    Serial.print("Received: ");
    Serial.println(inputLine);

    // Turn off all LEDs first (this will reset all LEDs when no valid input is found)
    digitalWrite(ledPin9, LOW);
    digitalWrite(ledPin10, LOW);
    digitalWrite(ledPin11, LOW);
    digitalWrite(ledPin12, LOW);
    digitalWrite(ledPin13, LOW);

    // Check the value of the received input and light the appropriate LED
    if (inputLine == "RAH213T") {
      digitalWrite(ledPin13, HIGH);  // Light LED at pin 13
    } else if (inputLine == "RAG320P") {
      digitalWrite(ledPin12, HIGH);  // Light LED at pin 12
    } else if (inputLine == "RAH593C") {
      digitalWrite(ledPin11, HIGH);  // Light LED at pin 11
    } else if (inputLine == "RAC697T") {
      digitalWrite(ledPin10, HIGH);  // Light LED at pin 10
    } else if (inputLine == "RAF418N") {
      digitalWrite(ledPin9, HIGH);   // Light LED at pin 9
    }
  } else {
    // If no data is available, turn off all LEDs
    digitalWrite(ledPin9, LOW);
    digitalWrite(ledPin10, LOW);
    digitalWrite(ledPin11, LOW);
    digitalWrite(ledPin12, LOW);
    digitalWrite(ledPin13, LOW);
  }

  // Add a 50ms delay before the next loop iteration
  delay(50);
}

```
Upload the above Arduino codes on your Arduino then  disconnect it and reconnect it to your PC and  then Perform again the inference \
This to prevent  python code to send error   of being unable to access the arduino port