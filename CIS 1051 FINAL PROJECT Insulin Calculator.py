#CIS 1051 FINAL PROJECT: INSULIN DOSAGE CALCULATOR
#GROUP MEMBERS: Daniel Samsonov, Tomas Chaparro
'''
1. The program will prompt the user for their blood sugar, target blood sugar, 
carb intake, insulin to carb ratio, and correction factor, which it will then save.

2. If the current blood glucose is too low, the program will warn the user about it
and will re-prompt for a new glucose reading.

3. Once the program gets the previous 2 values, it will calcucate and display the
insulin dosage for the carbs, the blood glucose correction, and the total amount of insulin units.

4. The registered carbs, blood glucose, and the total insulin units will be stored in a list 
(or multiple lists), and the program will ask the user if they want to calculate another insulin shot.

5. If the user decides to calculate another shot , the program will return the output of step 4, and this
new output will be added/saved to the previously mentioned list(s).

6. If the user doesn't want to calculate another insulin shot, the program will display a graph/histogram 
consisting of the logged grams of carbs, glucose, and total insulin units.
'''
# %%
import matplotlib.pyplot as plt

def insulin_calculator():
    while True:
        blood_sugar = float(input("Enter blood sugar level in (mg/dL): "))
        if blood_sugar < 70:
            blood_sugar = float(input("Blood glucose too low, enter another reading or treat your hypoglycemia."))
        else:
            break
    target_sugar = float(input("Enter target blood sugar level in (mg/dL): "))
    carb_intake = float(input("Enter carbohydrates to be consumed in (grams): "))
    correction_factor = float(input("Enter correction factor in (mg/dL per unit of insulin): "))
    carb_ratio = float(input("Enter insulin-to-carb ratio in (grams per unit of insulin): "))

    #Insulin dosage formula
    carb_dose = carb_intake / carb_ratio
    correction_dose = (blood_sugar - target_sugar) / correction_factor

    total_dosage = carb_dose + correction_dose

    #Check blood sugar level
    if blood_sugar > 180:
        print("Blood sugar level is too high.")
    elif blood_sugar < 70:
        print("Blood sugar level is too low.")
    else:
        print("Blood sugar level is in range.")

    print('')
    print(f"Carbohydrate Dose: {carb_dose} units")
    print(f"Correction Dose: {correction_dose} units")
    print(f"Total Insulin Dosage: {total_dosage} units")

    return blood_sugar, total_dosage

if __name__ == "__main__":
    blood_sugar_values = []
    total_dosage_values = []

    while True:
        blood_sugar, total_dosage = insulin_calculator()
        blood_sugar_values.append(blood_sugar)
        total_dosage_values.append(total_dosage)

        another_sample = input("Do you want to input another sample? (yes/no): ")
        if another_sample.lower() != "yes":
            break

    #Visualization of data
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(blood_sugar_values)), total_dosage_values, color='blue')
    plt.xlabel('Sample')
    plt.ylabel('Total Dosage (units)')
    plt.title('Total Insulin Dosage for Blood Sugar Levels')
    plt.xticks(range(len(blood_sugar_values)), [f'Sample {i+1}' for i in range(len(blood_sugar_values))])
    plt.show()

#%%
import matplotlib.pyplot as plt
import random

def insulin_calculator_simulations(simulations, target_sugar, correction_factor, carb_ratio):
    blood_sugar_values = []
    total_dosage_values = []

    for x in range(simulations):
        blood_sugar = random.randrange(70, 401)
        carb_intake = random.randrange(226)
        #Insulin dosage formula
        carb_dose = carb_intake / carb_ratio
        correction_dose = (blood_sugar - target_sugar) / correction_factor
        total_dosage = carb_dose + correction_dose

        blood_sugar_values += [blood_sugar]
        total_dosage_values += [total_dosage]
        #Check blood sugar level
        if blood_sugar > 180:
            print("Blood sugar level is too high.")
        elif blood_sugar < 70:
            print("Blood sugar level is too low.")
        else:
            print("Blood sugar level is in range.")

        print('')
        print(f"Carbohydrate Dose: {carb_dose} units")
        print(f"Correction Dose: {correction_dose} units")
        print(f"Total Insulin Dosage: {total_dosage} units")

    #Visualization of data
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(blood_sugar_values)), total_dosage_values, color='blue')
    plt.xlabel('Sample')
    plt.ylabel('Total Dosage (units)')
    plt.title('Total Insulin Dosage for Blood Sugar Levels')
    plt.xticks(range(len(blood_sugar_values)), [f'Sample {i+1}' for i in range(len(blood_sugar_values))])
    plt.show()

insulin_calculator_simulations(20, 100, 32, 10)

#%%
#SAMPLE VARIABLES
'''Sample 1:
Blood sugar level: 120 mg/dL
Target blood sugar level: 100 mg/dL
Carbohydrates to be consumed: 60 grams
Insulin-to-carb ratio: 10 grams per unit of insulin
Correction factor: 50 mg/dL per unit of insulin
Sample 2:
Blood sugar level: 90 mg/dL
Target blood sugar level: 110 mg/dL
Carbohydrates to be consumed: 45 grams
Insulin dose for the carb intake: 4 units
Correction factor: 30 mg/dL per unit of insulin
Sample 3:
Blood sugar level: 160 mg/dL
Target blood sugar level: 120 mg/dL
Carbohydrates to be consumed: 75 grams
Insulin-to-carb ratio: 12 grams per unit of insulin
Correction factor: 40 mg/dL per unit of insulin'''

# %%
#WORKS CITED
    #"""Michałowska, Joanna, "Insulin Dosage Calculator",
   # Omni Calculator, 2023 August 15,www.omnicalculator.com/health/insulin-dosage.
    #Accessed 2023 November 3"""   


#Example
#avg blood sugar of diabetic: 140
#desirable targer blood sugar: 100
#Avg carb intake: 30 **3 units of insulin per 10grams of carbs
#Avg carb ratio: 9
#Correction factor: 32 