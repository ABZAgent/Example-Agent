from dotenv import load_dotenv
load_dotenv()
import os
from abagentsdk import Agent, Memory, function_tool

@function_tool
def create_invoice(customer: str, amount: float, description: str):
    """Create an invoice for a customer with given amount and description."""
    return f"🧾 Invoice created for {customer} — Amount: ${amount}, Description: {description}"

@function_tool
def check_payment_status(invoice_id: str):
    """Check the payment status of a given invoice."""
    return f"Invoice {invoice_id} is currently marked as 'Paid '"

@function_tool
def send_invoice_email(customer_email: str, invoice_id: str):
    """Send the invoice to the customer via email."""
    return f"📧 Invoice {invoice_id} has been sent to {customer_email}"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def main():
    agent = Agent(
        name="Billing Agent",
        instructions=(
            "You're a helpful Billing Assistant. "
            "You can create invoices, check payment status, and send invoices by email."
        ),
        model="gemini-2.0-flash",
        memory=Memory(),
        tools=[create_invoice, check_payment_status, send_invoice_email],
        api_key=GEMINI_API_KEY,
    )

    print("Billing Agent is ready! (type 'exit' to quit)")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        try:
            result = agent.run(user_input)
            print(f"Agent: {result.content}")
        except Exception as e:
            print(f" Error: {e}")

if __name__ == "__main__":
    main()
