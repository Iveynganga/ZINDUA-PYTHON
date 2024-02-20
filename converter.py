def temp_converter(temp_from, temp_to, temp_value):

    if (temp_from == "DEGREE" and temp_to == "FARENHEIT") :
        temp= temp_value - 25.5
        print(f"{temp_value} degree is equivalent to {temp} Farenheit!")
    
    elif(temp_from == "FARENHEIT" and temp_to == "DEGREE") :
     temp = temp_value - 35.5
    print(f"{temp_value} farenheit is equivalent to {temp} degree!")

    temp_from = input("Are you converting from 'Farenheit' or 'Degree': ") . upper()
    temp_to = input("Are you converting to 'Farenheit' or 'Degree' : ") . upper ()
    temp_value = float(input("Enter temp value: "))

temp_from = input("Are you converting from 'Degree' or 'Farenheit': ") . upper()
temp_to = input("Are you converting to 'Degree' or 'Farenheit' : ") . upper ()
temp_value = float(input("Enter temp value: "))

temp_converter(temp_from, temp_to, temp_value)

temp_degree =float(input ("Enter the temperature in degrees celcius: "))
temp_farenheit =float(input ("Enter the temperature in degrees farenheit: "))


def temp_converter(temp_from, temp_to, temp_value) :
    if (temp_from == "FARENHEIT" and temp_to == "DEGREE") :
        temp= temp_value -33.5
        print(f"{temp_value} Farenheit is equivalent to {temp} degree celcius!")

        temp_from = input("Are you converting from 'Farenheit' or 'Degree': ") . upper()
        temp_to = input("Are you converting to 'Farenheit' or 'Degree' : ") . upper ()
        temp_value = float(input("Enter temp value: "))

        temp_converter(temp_from, temp_to, temp_value)