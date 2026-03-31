# Steam Price Checker
This project is my "First Personal Project" for Boot.dev as my first submission. This is a CLI tool to compare Steam game prices across global regions using the Steam Store API using Python. Basically, I chose this idea since I very often check regional prices ever since I've moved abroad. 

Input two regions from the available list, write down the game you want to compare and you'll get the prices of said game for both regions and currencies.
Additionally, if both currencies are supported by the exchange API that is being used (Frankfurter API) you will see exactly how much money you would be saving. 

## 1. Install Python

Ensure **Python 3.8 or newer** is installed.

Check your version:

```bash
python --version
```

## 2. Install Dependencies

The project requires the **requests** library to communicate with the Steam API and the currency exchange API.

Install it using pip:

```bash
pip install requests
```

---

## 3. Navigate to the Project Folder

Open a terminal and move to the project directory.

Example:

```bash
cd steam-price-checker
```

---

## 4. Run the Program

```bash
python main.py
```
