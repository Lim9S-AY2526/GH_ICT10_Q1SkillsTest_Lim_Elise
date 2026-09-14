# Skillstest
from pyscript import document, display  

# Calculate Total
def create_order(e):
    document.getElementById('Receipt').innerHTML = " "

    # PROD
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")

    # Subtotal
    subtotal = (
        float(prod1.value) * prod1.checked +
        float(prod2.value) * prod2.checked +
        float(prod3.value) * prod3.checked +
        float(prod4.value) * prod4.checked
    )

    # VAT 
    vat = subtotal * 0.12

    # Total Amount
    total = subtotal + vat

    # Display receipt
    display(f"Subtotal: ₱{subtotal}", target="Receipt")
    display(f"VAT (12%): ₱{vat}", target="Receipt")
    display(f"Total Amount: ₱{total}", target="Receipt")
