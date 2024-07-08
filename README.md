Name:Uchagaonkar Jay Sachin
Company:CODTECH IT SOLUTIONS
ID:62jfeh397
Domain:Cyber Security & Ethical Hacking
Duration:June 27,2024 to July 26,2024
Mentor:S.K.Lahari

Overview of the project

Project Name:-Password Strength Checker

This project is a password strength checker implemented using Python and Tkinter. The application provides a graphical user interface (GUI) where users can enter a username and a password to evaluate the strength of the password. The assessment is based on several criteria, including length, complexity, and uniqueness.

Features

- Username and Password Input: Users can input their username and password into dedicated fields.
- Password Strength Assessment: The password is evaluated against various criteria:
  - Minimum length requirement.
  - Similarity to the username.
  - Inclusion of lowercase and uppercase letters.
  - Presence of digits and special characters.
- Strength Categories: The password strength is categorized as very strong, strong, medium, or weak.
- Color-Coded Feedback: The strength of the password is displayed with color-coded feedback for easy identification.
- Password Visibility Toggle: Users can toggle the visibility of the password between plain text and hidden.

How It Works

1. Input Validation: The application checks if the password meets the minimum length requirement and if it is too similar to the username.
2. Complexity and Uniqueness Scoring: The password is scored based on its length, the presence of various character types (lowercase, uppercase, digits, special characters), and the uniqueness of characters.
3. Strength Display: The total score determines the strength category, which is displayed to the user along with a score and color-coded label.
4. Password Toggle: The visibility of the password can be toggled using a button to show or hide the password text.

Getting Started

To run this project, you need to have Python installed on your machine. Follow these steps to get started:

1. Clone the repository:
   ```
   git clone https://github.com/Jay2212004/CODTECH-Task-1.git
   ```
2. Navigate to the project directory:
   ```
   cd CODTECH-Task-1
   ```
3. Run the application:
   ```
   python Task_1.py
   ```

Requirements

- Python 3.x
- Tkinter library (usually included with Python)

Usage

1. Launch the application.
2. Enter your username in the "Enter your username" field.
3. Enter your password in the "Enter your password" field.
4. Click the "Check Strength" button to evaluate the password strength.
5. The result will be displayed below the button with a color-coded label indicating the password strength.
6. Use the "Show Password" button to toggle the visibility of the password.

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

License

This project is licensed under the MIT License. See the LICENSE file for details.
