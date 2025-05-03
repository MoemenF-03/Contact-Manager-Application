# 📇 Contact Manager Application
Academic Project :
A desktop application for managing institutional contacts built with PyQt5. This application provides a complete contact management system with authentication, allowing users to add, modify, display, and delete contacts while ensuring data validation and security.

## ✨ Features

* **User Authentication**
  * Secure login system
  * New user registration
  * Validation of email format and password strength

* **Contact Management**
  * Add new contacts with name, email, and phone number
  * Modify existing contact information
  * Display all contacts or search by name
  * Delete individual contacts
  * Clear all contacts
  * Import contacts from external CSV files

* **Data Validation**
  * Name validation (alphanumeric, max 30 characters)
  * Email validation (institutional format: username@isi.utm.tn)
  * Phone number validation (6-digit numeric)
  * Prevention of duplicate email entries

* **User Experience**
  * Reset form fields
  * Keyboard shortcuts (Ctrl+Q, Ctrl+R, Ctrl+S)
  * Date display
  * Responsive messages for actions

## 🛠️ Technologies Used

* **Frontend & Backend**:
  * Python 3.x
  * PyQt5 for GUI components
  * Qt Designer for UI layout (.ui files)

* **Data Storage**:
  * CSV files for contacts and user accounts
  * File I/O operations for data persistence

## 🚀 Setup & Installation

### Prerequisites
* Python 3.6 or higher
* PyQt5 library

### Steps to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/contact-manager.git
   cd contact-manager
   ```

2. **Install dependencies**:
   ```bash
   pip install PyQt5
   ```

3. **Prepare data files**:
   - Create an empty `data.csv` file for contacts
   - Create `admin_list.csv` with at least one admin account:
     ```
     admin@isi.utm.tn,password
     ```

4. **Run the application**:
   ```bash
   python main.py
   ```

## 🌍 How to Use

### Login / Registration
1. Start the application to see the login screen
2. Enter email and password to log in
3. Click "Sign Up" if you need to create a new account

### Managing Contacts
1. **Add a contact**:
   * Fill in name, email (@isi.utm.tn format), and 6-digit phone number
   * Click "Ajouter" (Add)

2. **Modify a contact**:
   * Enter the name of the contact to modify
   * Enter new email and phone number
   * Click "Modifier" (Modify)

3. **Display contacts**:
   * To display all contacts, leave the search field empty and click "Afficher" (Display)
   * To search for a specific contact, enter the name and click "Afficher"

4. **Delete a contact**:
   * Enter the name of the contact to delete
   * Click "Supprimer" (Delete)

5. **Clear all contacts**:
   * Click "Vider" (Clear) to remove all contacts
   * Confirm the action in the dialog box

6. **Import contacts**:
   * Click "Upload" to select a CSV file containing contacts
   * The application will import all contacts from the selected file

### Keyboard Shortcuts
* **Ctrl+Q**: Quit the application
* **Ctrl+R**: Reset all form fields
* **Ctrl+S**: Clear all contacts

## 📂 Project Structure

```
contact-manager/
├── main.py              # Main Python script
├── qt.ui                # Main window UI design
├── login.ui             # Login screen UI design
├── create.ui            # Registration screen UI design
├── data.csv             # Contact data storage
├── admin_list.csv       # Admin account storage
├── screenshots/         # Application screenshots
└── README.md            # This file
```

## 🔍 Code Structure

The application follows a modular design with functions for:

### Authentication
- `check_login()`: Validates user credentials
- `check_signup()`: Creates new admin accounts
- `is_valid_email()`: Validates email format
- `is_valid_password()`: Ensures password meets requirements

### Contact Management
- `remplir1()`: Adds a new contact
- `modifier()`: Updates existing contact information
- `afficher()`: Displays contacts
- `supprimer()`: Removes a single contact
- `vider()`: Clears all contacts
- `import_contacts()`: Imports contacts from CSV

### Utility Functions
- `verifnom()`: Validates contact names
- `verifemail()`: Validates institutional emails
- `reinitialiser()`: Clears form fields
- `keyPressEvent()`: Handles keyboard shortcuts

## 📝 Notes

- The application is designed for institutional use with a specific email format (@isi.utm.tn)
- All contact data is stored locally in CSV format
- No encryption is used for password storage in this version

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -m 'Add your feature'`)
4. Push to branch (`git push origin feature/your-feature`)
5. Open a Pull Request
