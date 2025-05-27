class Payment:
    def process_payment(self):
        print("Processing generic payment")

class CreditCardPayment(Payment):
    def process_payment(self):  # Overrides parent's method
        print("Processing credit card payment")

# Usage
payment = CreditCardPayment()
payment.process_payment()  # Output: "Processing credit card payment"