# CyberSafe Password Manager

CyberSafe Password Manager is a command-line application that securely stores and manages user passwords using encryption.

## Features

- Master login password for security
- Add new passwords
- View stored passwords
- Delete stored passwords
- List all saved websites
- Generate strong random passwords
- Encryption using Fernet symmetric encryption

## Technologies Used

- Python 3
- Cryptography library
- JSON file storage
- Command Line Interface (CLI)

## Project Structure

main.py – Main program and user interface

password_manager.py – Handles password storage and retrieval

encryption.py – Encrypts and decrypts passwords

storage.json – Stores encrypted passwords

secret.key – Encryption key

requirements.txt – Project dependencies

## Installation

Clone the repository:

git clone https://github.com/bhavin-01/cybersafe-password-manager.git

Go to project directory:

cd cybersafe-password-manager

Install dependencies:

pip install -r requirements.txt

## Run the Program

Run the program using:

python3 main.py

## Example Menu

CyberSafe Password Manager

1 Add Password  
2 View Password  
3 Delete Password  
4 List Saved Sites  
5 Generate Strong Password  
6 Exit  

## Author

Bhavin
