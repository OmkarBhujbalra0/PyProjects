measure = input("Enter the number and unit: (ex : 10 kg)")
convert = input("Enter the unit in which you want to convert:")
lizt = list(measure)

num,unit = int(lizt[0]),str(lizt[1])

if (unit == "Kg" or "kg" or "KG") and convert == "mg" or "MG" or "Mg":
    result = num*1000000
    print("Result is",result,"mg")
elif (unit == "Kg" or "kg" or "KG") and convert == "g" or "G":
    result = num*1000
    print("Result is",result,"g")
elif (unit == "G" or "g") and convert == "mg" or "MG" or "Mg":
    result = num*1000
    print("Result is",result,"mg")
elif (unit == "Km" or "km" or "KM") and convert == "m" or "M":
    result = num*1000
    print("Result is",result,"m")
elif (unit == "M" or "m") and convert == "Cm" or "CM" or "cm":
    result = num*100
    print("Result is",result,"cm")
elif (unit == "Cm" or "cm" or "CM") and convert == "mm" or "Mm" or "MM":
    result = num*10
    print("Result is",result,"mm")
elif (unit == "Km" or "km" or "KM") and convert == "Cm" or "CM" or "cm":
    result = num*10000
    print("Result is",result,"cm")
elif (unit == "Km" or "km" or "KM") and convert == "Mm" or "MM" or "mm":
    result = num*100000
    print("Result is",result,"mm")
else:
    print("Sorry,Unit or Number you enter is either wrong or not available for now!")
