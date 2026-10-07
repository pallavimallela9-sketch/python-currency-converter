print("==========================================")
print("           CURRENCY CONVERTER")
print("==========================================")

# Sample fixed exchange rates
rates = {
    "USD": {
        "INR": 83.50,
        "EUR": 0.92,
        "GBP": 0.79
    },
    "INR": {
        "USD": 1 / 83.50,
        "EUR": 1 / 90.70,
        "GBP": 1 / 105.80
    },
    "EUR": {
        "USD": 1.09,
        "INR": 90.70,
        "GBP": 0.86
    },
    "GBP": {
        "USD": 1.27,
        "INR": 105.80,
        "EUR": 1.16
    }
}

print("\nSupported currencies:")
print("1. INR - Indian Rupee")
print("2. USD - US Dollar")
print("3. EUR - Euro")
print("4. GBP - British Pound")

while True:
    print("\n============== MENU ==============")
    print("1. Convert Currency")
    print("2. View Exchange Rates")
    print("3. Exit")
    print("==================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        from_currency = input(
            "Enter source currency (INR/USD/EUR/GBP): "
        ).upper()

        to_currency = input(
            "Enter target currency (INR/USD/EUR/GBP): "
        ).upper()

        if from_currency not in rates:
            print("Invalid source currency.")
            continue

        if to_currency not in rates:
            print("Invalid target currency.")
            continue

        try:
            amount = float(input("Enter amount: "))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            if from_currency == to_currency:
                converted_amount = amount
            else:
                exchange_rate = rates[from_currency][to_currency]
                converted_amount = amount * exchange_rate

            print("\n========== CONVERSION ==========")
            print("From Currency :", from_currency)
            print("To Currency   :", to_currency)
            print("Amount        :", amount)
            print("Converted     :", round(converted_amount, 2))
            print("================================")

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        print("\n========== EXCHANGE RATES ==========")

        for currency, values in rates.items():
            print("\n1", currency, "equals:")

            for target, rate in values.items():
                print("  ", target, ":", round(rate, 4))

    elif choice == "3":
        print("\nThank you for using the Currency Converter.")
        break

    else:
        print("Invalid choice. Please try again.")
