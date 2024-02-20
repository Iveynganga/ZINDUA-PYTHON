def currency_converter():
    usd_to_ksh = 150  # Exchange rate: 1 USD = 150 KSH
    amount_usd = float(input("Please enter the amount in USD: "))
    
    converted_amount_ksh = amount_usd * usd_to_ksh
    print(f"You are converting {amount_usd:.2f} USD to {converted_amount_ksh:.2f} KSH.")

currency_converter()


