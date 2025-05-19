class OnlinePharmacy:
    def __init__(self):
        # Medicine inventory (Tablets and Syrups)
        self.medicine_stock = {
            "tablets": ["Paracetamol", "Ibuprofen", "Aspirin", "Amoxicillin"],
            "syrups": ["Cough Syrup", "Vitamin D Syrup", "Iron Syrup"]
        }

    def check_availability(self, medicine_name):
        # Convert user input to lowercase for case-insensitive search
        medicine_name = medicine_name.lower()

        # Check if the medicine is in stock
        for category, medicines in self.medicine_stock.items():
            if any(medicine_name == med.lower() for med in medicines):
                print(f" {medicine_name.title()} is available in {category}.")
                return
        print(f" {medicine_name.title()} is NOT available.")

# Create an instance of OnlinePharmacy
pharmacy = OnlinePharmacy()

# Get user input
user_medicine = input("Enter the medicine name to check availability: ")
pharmacy.check_availability(user_medicine)
