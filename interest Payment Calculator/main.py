class Account:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def show(self):
        print(f"\nYour account '{self.name}' has ${self.amount}.")


class Loan(Account):
    def __init__(self, name, amount, loan, apr, years):
        super().__init__(name, amount)
        self.loan = loan
        self.apr = apr
        self.years = years

    def monthly_payment(self):
        r = self.apr / 1200 
        n = self.years * 12  
        if r == 0:
            payment = self.loan / n
        else:
            payment = self.loan * r / (1 - (1 + r) ** -n)
        print(f"\nMonthly payment: ${payment:.2f} for {self.years} years at {self.apr}% APR.")
        return payment

    def loan_summary(self):
        print(f"\nLoan Summary:")
        print(f"Account name: {self.name}")
        print(f"Loan amount: ${self.loan}")
        print(f"APR: {self.apr}%")
        print(f"Years: {self.years}")
        self.monthly_payment()


if __name__ == "__main__":
    print("******** Welcome to the Interest Payment Calculator ********")

    f = None  
    while True:
        x = input("\nChoose an option:\n 1 - Create an account\n 2 - Show account details\n 3 - Take a loan\n 4 - Exit\n> ")

        if x == "1":
            name = input("\nEnter account name: ")
            amount = float(input("Enter initial amount: $"))
            f = Account(name, amount)
            f.show()

        elif x == "2":
            if f:
                f.show()
            else:
                print(" You need to create an account first.")

        elif x == "3":
            if f:
                loan_amount = float(input("\nEnter loan amount: $"))
                apr = float(input("Enter APR (%): "))
                years = int(input("Enter loan term (years): "))
                f = Loan(f.name, f.amount, loan_amount, apr, years)
                f.loan_summary()
            else:
                print(" You need to create an account before taking a loan.")

        elif x == "4":
            print("\nThank you for using our services.")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")
