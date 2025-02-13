import random #biblioteka do wyboru randomowej liczby 

random_number = random.randint(1,100)  #automatycznie wybiera liczbe od 1 do 100
print("Welcome to the number guessing game!")
B = 0

while True:  #pentla nieskończona
  try:
      a = int(input("Guess number from 1 to 100: "))#wybranie liczby przez gracza
    
  except ValueError:
    print("That's not corect number! Please enter a valid integer.")
    continue #jeśli pląd to wracamy do początku petli

  B += 1 # zwiększamy licznik prob 

  if int(a) > random_number:  #sprawdznie czy liczba jest większa czy mniejsza od wylosowaniej przez program
    print("Your number is too HIGH, try again.")
  elif int(a)< random_number:
    print("Your number is too LOW, try again.")

  else:  #po zgadnięciu liczby program wyświetla gratulacje i sie kończy
    print("You guess the number! Congraulations!")
    print(f"Yours attempts: {B} " )

    break



