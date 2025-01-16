# BotProductRegistration
This project is a Python-based automation bot designed to register products from a database into a company's system. It leverages the PyAutoGUI library to simulate user interactions (mouse clicks, keyboard strokes, etc.) for automating the registration process.

## Table of Contents
<a name="Features"></a>
<a name="Requirements"></a>
<a name="Installation"></a>
<a name="Configuration"></a>
<a name="Usage"></a>
<a name="Additional Information"></a>
<a name="License"></a>

## Features
- Automated data entry into the company's system using GUI automation.
- Reads product data from a predefined database.
- Handles UI interactions seamlessly using PyAutoGUI.

## Requirements
- Python 3.6 or higher
- PyAutoGUI library
- Time library
- cv2 library

## Installation
1. Clone the repository (bash)
```
git clone https://github.com/yourusername/product-registration-bot.git
cd product-registration-bot
```
2. (Optional) Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the required Python libraries:
```
pip install -r "read in requirements"
```
## Configuration
Before running the bot, ensure you have:

- The database with the product information properly configured and accessible.
- Correct screen resolution and GUI layout expected by the bot. PyAutoGUI relies on pixel-based interaction, so changes in the interface may require updating coordinates in the script.
- Required access permissions for automating tasks on your system.
Modify any configuration files or script parameters as needed to match your environment. For example, update the database connection settings or UI element coordinates if necessary.

## Usage
Run the bot with Python:
```
python product_registration_bot.py
```
The bot will start reading from the database and performing the necessary actions to register each product in the system. Monitor the console output for status messages and potential errors.

***Pyautogui has a security interrupt for the bot. just go with the mouse to the top left corner of the screen.***

## Aditional Information
- Error Handling: The script includes basic error handling for interruptions or failures during the registration process. Ensure all UI elements are accessible and correctly positioned to avoid misclicks.
- Extending Functionality: If you need to adapt the bot for different tasks, consider studying the PyAutoGUI documentation and modifying the script accordingly.
- Security: Be cautious when automating login credentials or sensitive data inputs. Secure and obfuscate any sensitive information as necessary.

## Suggestions for Further Improvements
- Dynamic UI Handling: Currently, the script may rely on fixed coordinates. Integrating image recognition or more dynamic UI element targeting could make the bot more robust.
- Logging: Implement detailed logging to track each product registration attempt, successes, failures, and unexpected behavior.
- Configuration File: Use a configuration file (e.g., YAML, JSON) for settings such as database paths, UI coordinates, and other parameters to make the script more flexible.

