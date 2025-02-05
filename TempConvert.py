#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("Enter a temperature in Fahrenheit: ")
  tempF = int(tempF)

  tempC = (tempF-32) / 1.8
  tempC = round(tempC, 1)

  print(tempF, "degrees Fahrenheit is", tempC, "degrees Celsius.")
if __name__ == '__main__':
  main()
