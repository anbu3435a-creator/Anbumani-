
import getpass
import string

# Terminal colors
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"

def banner():
    print(BLUE + BOLD + r"""
  ____   _    ____ ____
 |  _ \ / \  / ___/ ___|
 | |_) / _ \ \___ \___ \
 |  __/ ___ \ ___) |__) |
 |_| /_/   \_\____/____/
""" + RESET)
    print(CYAN + BOLD + "     PASSWORD STRENGTH CHECKER" + RESET)
    print(BLUE + "-" * 36 + RESET)

def check_password(password):
    checks = [
        len(password) >= 8,
        len(password) >= 12,
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password)
    ]

    score = sum(checks)

    print("\n" + CYAN + "===== PASSWORD REPORT =====" + RESET)
    print(f"Length: {len(password)} characters")
    print(f"Checks passed: {score}/6")
    if score <= 2:
        print(RED + BOLD + "[!] STRENGTH: WEAK" + RESET)
        print(RED + "Try a longer, less predictable password." + RESET)
    elif score <= 4:
        print(YELLOW + BOLD + "[!] STRENGTH: MEDIUM" + RESET)
        print(YELLOW + "Try improving its length and variety." + RESET)
    else:
        print(GREEN + BOLD + "[+] STRENGTH: STRONG" + RESET)
        print(GREEN + "Good mix of length and character types!" + RESET)

    print(CYAN + "=" * 28 + RESET)
    print("Note: This is a basic checker, not a guarantee.")

def main():
    while True:
        banner()
        print("1. Check password")
        print("2. Exit")

        choice = input(CYAN + "\nChoose an option: " + RESET)

        if choice == "1":
            password = getpass.getpass("Enter test password: ")
            if password:
                check_password(password)
            else:
                print(RED + "Password cannot be empty." + RESET)

            input("\nPress Enter to continue...")
        elif choice == "2":
            print(GREEN + "Goodbye, bro!" + RESET)
            break
        else:
            print(RED + "Invalid choice. Select 1 or 2." + RESET)

if __name__ == "__main__":
    main()

