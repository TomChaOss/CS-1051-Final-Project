#GROUP MEMBERS: Daniel Samsonov, Jayden Millwood, Tomas Chaparro
#INSULIN DOSAGE CALCULATOR

#STEP 1 Sugar/Carb info in inputs
#blood sugar, target sugar, carb_intake, carb_ratio, carb_dose, correction_dose
#STEP 2 
#formula to correctly calculate the dosage/correction doses needed for patient
#STEP 3
#print statements
#STEP 4
#calling the function

#%%
def insulin_calculator():

    blood_sugar = float(input("Enter blood sugar level in(mg/dL): "))
    target_sugar = float(input("Enter target blood sugar level in (mg/dL): "))
    carb_intake = float(input("Enter carbohydrates to be consumed in (grams): "))
    carb_ratio = float(input("Enter insulin-to-carb ratio in(grams per unit of insulin): "))
    correction_factor = float(input("Enter correction factor in(mg/dL per unit of insulin): "))
#%%
#Insulin dosage formula
    carb_dose = carb_intake / carb_ratio
    correction_dose = (blood_sugar - target_sugar) / correction_factor

    total_dosage = carb_dose + correction_dose
    #Typically 1 insulin unit per 10 to 15 grams of carbs
#%%    
#Print statements
    print("\nInsulin Dosage Calculation:")
    print(f"Carbohydrate Dose: {carb_dose} units")
    print(f"Correction Dose: {correction_dose} units")
    print(f"Total Insulin Dosage: {total_dosage} units")
#%%
if __name__ == "__main__":
    insulin_calculator()

#WORKS CITED
    """Michałowska, Joanna, "Insulin Dosage Calculator",
    Omni Calculator, 2023 August 15,www.omnicalculator.com/health/insulin-dosage.
    Accessed 2023 November 3"""


#show graph (matplotlib), create calander.


    #9PM BGC 120
    #10AM BGC 80
    #Create time delays 