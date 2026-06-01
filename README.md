# SecurePass-CLI

A secure, command-line based password generator and manager with master password encryption.

## Features
- **Customizable:** Choose the length of your password.
- **Secure Storage:** Passwords are encrypted using Fernet symmetric encryption.
- **Master Password Protection:** Your stored passwords are locked behind a Master Password.

## ⚠️ Important Disclaimer
This tool uses Master Password-based encryption. **If you lose or forget your Master Password, your encrypted data cannot be recovered.** Please handle your Master Password with care.

## How to use
1. Install requirements: 
   `pip install cryptography`
2. Run the tool: 
   `python generator.py`
3. Follow the on-screen prompts to generate and save your passwords.

## License
This project is licensed under the MIT License.
