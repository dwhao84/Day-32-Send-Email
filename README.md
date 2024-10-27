# Email Sender Script

A simple Python script for sending emails through Yahoo SMTP server using TLS encryption.

## Features

- Sends emails through Yahoo Mail SMTP server
- Uses TLS encryption for secure communication
- Supports plain text email content
- Handles connection errors gracefully

## Prerequisites

The script requires the following Python modules:
- `smtplib`
- `email`

You'll also need to create a `mail.py` file with your email credentials:
```python
my_email = "your_recipient_email@domain.com"
my_password = "your_password"
yahoo_address = "your_yahoo_email@yahoo.com"
yahoo_password = "your_yahoo_app_password"
```

## Configuration

Make sure to:
1. Enable "Allow less secure app access" in your Yahoo account settings
2. Use an App Password if you have 2-factor authentication enabled

## Usage

The script will:
1. Create a new email message with specified sender, recipient, and subject
2. Connect to Yahoo's SMTP server on port 587
3. Enable TLS encryption
4. Authenticate using your Yahoo credentials
5. Send the email
6. Close the connection

## Error Handling

The script includes error handling that will:
- Catch any exceptions during the email sending process
- Print error messages if something goes wrong
- Ensure the SMTP connection is properly closed

## Note

Keep your email credentials secure and never commit them directly to your repository. Consider using environment variables or a secure configuration file for storing sensitive information.