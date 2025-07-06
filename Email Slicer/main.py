import re

# Regex pattern to validate email
def verify(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def main():
    print("Welcome to Email Slicer")
    print("")

    while True:
        email_input = input("Input your email address: ").strip()

        if verify(email_input):
            username, domain_ext = email_input.split("@")
            if '.' in domain_ext:
                domain, extension = domain_ext.split(".", 1)
                print("\ni Valid Email!")
                print("Username   :", username)
                print("Domain     :", domain)
                print("Extension  :", extension)
                break
            else:
                print(" Email missing domain extension (e.g., '.com'). Try again.\n")
        else:
            print(" Invalid email format. Please try again.\n")

if __name__ == "__main__":
    main()
