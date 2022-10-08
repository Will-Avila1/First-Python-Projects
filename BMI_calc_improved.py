#!/usr/bin/env python3

## BMI CALCULATOR Learning Functions and Inputs, basically incorporating everything I have learned.

## 10/8/22 notes: I defined the functions outside of the 'main' loop. I still have 2 'main' loops, I think. If... and While... I'm unsure how to fix that.
##          I also fixed the variable data types. They should now be consistent. If it started as a string, it remains a string, etc.
calc = 1

def convert_kg(lbs):
    kg = lbs / 2.2
    return kg
def imp_to_cm(ft, inches):
    cm = (ft * 12 + inches) * 2.54
    return cm


def BMI_calc_esp(name, kg, height):
    bmi = kg / ((height / 100) **2)
    print("El IMC de " + name + " es " + str(bmi))
    if bmi < 18.5:
        return name + " esta bajo peso."
    elif bmi >= 18.5 and bmi < 25:
        return name + " esta en rango optimo."
    elif bmi >= 25 and bmi < 30:
        return name + " esta exceso de peso."
    elif bmi >= 30 and bmi < 35:
        return name + " esta en obesa clase I. Hay tres clases, este es el mejor."
    elif bmi >= 35 and bmi < 40:
        return name + " esta en obesa clase II. Hay tres clases, este esta en el centro."
    else:
        return name + " esta en obesa clase III. Hay tres clases, este es el peor."
    
def BMI_calc_eng(name, kg, height):
    bmi = kg / ((height / 100) **2)
    print (name + "'s bmi is " + str(bmi) + ".")
    if bmi < 18.5:
        return name + " is underweight."
    elif bmi >= 18.5 and bmi < 25:
        return name + " is in the optimum range."
    elif bmi >= 25 and bmi < 30:
        return name + " is overweight."
    elif bmi >= 30 and bmi < 35:
        return name + " is class I obese. This is the most mild of the three types of obesity."
    elif bmi >= 35 and bmi < 40:
        return name + " is class II obese. This is the middle class of obesity."
    else:
        return name + " is class III obese. This is the worst class of obesity."

print("Welcome to Will's awesome BMI (body mass index) calculator! Follow the prompts below!")

language = input("For English, press any key. Para espanol, pone 'esp' ")

if "ESP" in language.upper():
    print("Bienvenidos a la calculadora asombrosa de Will para IMC (indice de masa corporal)! Sigue los istrucciones abajo!")
    while True:
        name = input("Como se llama esta persona? ")
    
        print("Cuanto pesa, en kg?")
        weight_str = input("Si solo sabe en libras, pone 'imperial' ")
        if "IMPERIAL" in weight_str.upper():
            weight_input = input("Quanto pesa, en libras? ")
            weight_float = convert_kg(float(weight_input))
        else:
            weight_float = float(weight_str)
            
        print("Cuanto es su altura, en cm?")
        height_str = input("Si solo sabe en pies y pulgadas, pone 'imperial' ")
        if "IMPERIAL" in height_str.upper():
            height_ft = input("Primero, cuantos pies? ") 
            height_inches = input("Ahora, cuantos pulgadas? ")
            height_float = imp_to_cm(float(height_ft), float(height_inches))
        else:
            height_float = float(height_str)
        print(BMI_calc_esp(name, weight_float, height_float))

        print("Pone 'F' para parar, o cualquier otro llave para hacer otra vez.")
        end = input()
        if "F" in end.upper():
            exit()
        else:
            calc = calc + 1
            print("Esta proxima calculacion sera numero " + str(calc) + ".")


## This is where the English part of the code begins!

    
while True:
    
    name = input("What is this peron's name? ")
    
    print("What is their weight, in kg?")
    weight_str = input("If you only know their weight in lbs, type 'imperial' ")
    if "IMPERIAL" in weight_str.upper():
        weight_str = input("What is their weight, in lbs? ")
        weight_float = convert_kg(float(weight_str))
    else:
        weight_float = float(weight_str)

    print("What is their height, in cm?")
    height_str = input("If you only know their height in feet and inches, type 'imperial' ")
    if "IMPERIAL" in height_str.upper():
        height_ft = float(input("First, how many feet tall? ")) 
        height_inches = float(input("Now, how many more inches? "))
        height_float = imp_to_cm((height_ft),(height_inches))
    else:
        height_float = float(height_str)
        
    print(BMI_calc_eng(name,weight_float,height_float))

    print("Press 'F' to quit, or any other key to restart.")
    end = input()
    if "F" in end.upper():
        break
    else:
        calc = calc + 1
        print("You are now beginning calculation #" + str(calc) + ".")
