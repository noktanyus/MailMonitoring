
# Server Connection Monitoring & Alert System

This project is a server monitoring system that attempts to connect to a specified mail server at regular intervals. If the connection fails, it sends an email alert to a designated email address via an alternative mail server.

## Features
- Monitors server connection and detects failures.
- Sends alert emails if the primary server fails.
- Configurable to work with different mail servers (primary and alternative).

## Installation

### Prerequisites
- Python 3.x
- SMTP library for sending emails
- Socket library for server connection

You can install the required dependencies using the following command:

```bash
pip install smtplib
```

### Clone the Repository
Clone this repository to your local machine using:

```bash
git clone https://github.com/yourusername/server-connection-monitor.git
```

### Running the Application

1. Make sure to update the server and email configuration in the script.
2. Run the main script to start monitoring:

```bash
python main.py
```

### Configuration

In the script, you can configure:

- **Primary Mail Server**: The main SMTP server that will be used for sending emails if it is reachable.
- **Alternative Mail Server**: A fallback SMTP server that will send emails if the primary server is unreachable.
- **Alert Email**: The email address that will receive the alert notifications.

### Example Configuration:
```python
PRIMARY_MAIL_SERVER = 'smtp.noktanyus.com'
PRIMARY_MAIL_PORT = 587
PRIMARY_USERNAME = 'kullanici@noktanyus.com'
PRIMARY_PASSWORD = 'sifre'

ALTERNATIVE_MAIL_SERVER = 'smtp.gmail.com'
ALTERNATIVE_MAIL_PORT = 587
ALTERNATIVE_USERNAME = 'alternatif@gmail.com'
ALTERNATIVE_PASSWORD = 'alternatif_sifre'

ALERT_EMAIL = 'alert@ornek.com'
```

## Languages Used
- **Python**: The core logic is implemented in Python for handling SMTP and server connection.

## Contributing
Feel free to submit issues or pull requests for improvements!

## License
This project is licensed under the MIT License.
