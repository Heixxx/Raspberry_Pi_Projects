# RGB LED Control System with Raspberry Pi

## Description  
This project demonstrates a basic circuit setup to control an RGB LED using a Raspberry Pi. The circuit uses a **common anode RGB LED**, where the anode is connected to a 5V power source, and the cathode pins (Red, Green, Blue) are controlled via Raspberry Pi GPIO pins. 
Resistors are used to safely reduce the voltage and current flowing through the LED to prevent damage. 

---

## How It Works  
### Circuit Design  
1. **Common Anode Configuration**:  
   - The RGB LED's anode is connected to **5V** (Raspberry Pi or external power supply).  
   - Each cathode (R/G/B) is connected to a GPIO pin through a current-limiting resistor.  

2. **Resistor Calculations**:  
   - Resistors are chosen to limit current based on Ohm's Law (`V = I × R`).  
   - Values used:  
     - **Red**: 100Ω (average)  
     - **Green**: 150Ω (average)  
     - **Blue**: 120Ω (average)  

3. **GPIO Control**:  
   - The Raspberry Pi’s GPIO pins toggle between `HIGH` (3.3V) and `LOW` (0V) to turn the LED on/off.   

---

## Some Pictures
![IMG_6740](https://github.com/user-attachments/assets/5a3983e1-64fb-4b22-b9f2-7e9bd9565b75)

![IMG_6737](https://github.com/user-attachments/assets/582c65b8-182b-43fb-9175-84d6a408e6d6)

## Voltage Conversion & Power Calculations  
### Ohm's Law Application  
To ensure the LED operates safely within its rated current (typically 20mA):  

1. **Voltage Drop Across Resistor**:
2. 
  - Example for the **Red LED**:  
  - `V_source = 5V`  
  - `V_LED (Red) ≈ 2.0V`  
  - `V_resistor = 5V - 2.0V = 3.0V`  

2. **Resistor Value Calculation**:
   
  - For `I = 20mA`:  
  - `R = 3.0V / 0.02A = 150Ω`  
  - **Note**: (100Ω, 120Ω, 150Ω) int this script.  

3. **Power Dissipation**:

   - Standard 0.25W resistors are sufficient.  

### Summary Table  
| Color  | Resistor (Ω) | Voltage Drop (V) | Current (mA) | Power (W) |  
|--------|--------------|-------------------|--------------|-----------|  
| Red    | 100          | 3.0               | 30           | 0.09      |  
| Green  | 150          | 3.0               | 20           | 0.06      |  
| Blue   | 120          | 3.0               | 25           | 0.075     |  
