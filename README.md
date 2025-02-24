# Password Generator

A simple and customizable password generator built in Python. This tool allows you to generate secure passwords with a mix of letters, numbers, and symbols, and saves them to a file for future reference.

---

## Features

- **Customizable Passwords**: Choose the number of letters, symbols, and numbers in your password.
- **Platform-Specific Passwords**: Associate each password with a platform (e.g., Google, Facebook).
- **Save Passwords**: Automatically saves generated passwords to a file (`password.txt`) for easy retrieval.
- **User-Friendly**: Interactive command-line interface for ease of use.
- **Randomization**: Passwords are shuffled to ensure maximum security.

---

## How It Works

The password generator uses Python's `random` module to randomly select characters from predefined lists of letters, numbers, and symbols. The generated password is then shuffled to enhance security and saved to a file along with the associated platform name.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/chinonsojacobs/Password-Generator.git
   cd password-generator
   ```

2. **Run the Script**:
   Ensure you have Python installed (Python 3.6 or higher recommended). Run the script using:
   ```bash
   python PasswordGenerator.py
   ```

---

## Usage

1. **Run the Script**:
   Execute the script by running:
   ```bash
   python PasswordGenerator.py
   ```

2. **Follow the Prompts**:
   - Enter the platform name (e.g., Google, Facebook).
   - Specify the number of letters, symbols, and numbers you want in your password.

3. **Save the Password**:
   The generated password will be displayed and saved to `password.txt` in the following format:
   ```
   -> Platform : 'GeneratedPassword'
   ```

4. **Generate Another Password**:
   You can choose to generate another password or exit the program.

---

## Example

Here’s an example of how the program works:

```
Password Generator!
What platform are you generating the password for:
> Google
How many letters would you like in your password?
> 8
How many symbols would you like?
> 2
How many numbers would you like?
> 2
Your password for Google : aB3$dE7!gH
Would you like to generate another password (Type yes or no):
> no
Thank you
```

The generated password will be saved in `password.txt`:
```
-> Google : 'aB3$dE7!gH'
```

---

## File Structure

- `PasswordGenerator.py`: The main Python script for generating passwords.
- `password.txt`: A file where generated passwords are stored.

---

## Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch and submit a pull request.

---

## License

This project is licensed under the MIT License.

---