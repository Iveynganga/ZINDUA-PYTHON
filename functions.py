def currency_converter(currency_from, currency_to, currency_value):

    #self_exchange_rates = 
            #'USD': 'EUR'; 0.85, 
           # 'EUR': 'USD'; 1.18,
           # 'GBP': 'USD'; 1.33, 
            #'JPY': 'USD'; 0.0091,
            #'INR': 'USD'; 0.0135,
        
    if(currency_from == "USD", currency_to == "EUR"):
        currency_value = 10
        currency = 0.85
        print(f"{currency_value} USD is equivalent to {currency*currency_value} EUR")
    
    elif(currency_from == "EUR" and currency_to == "USD") :
        currency_value = 10
        currency = 1.18
        print(f"{currency_value} EUR is equivalent to {currency*currency_value} USD!")

    else:
        "Not Valid"

currency_from = input("Are you converting from 'USD' or 'EUR': ") . upper()
currency_to = input("Are you converting to 'EUR' or 'USD' : ") . upper ()
currency_value = float(input("Enter currency value: "))

currency_converter(currency_from, currency_to, currency_value)


     
    



