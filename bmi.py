def calculate_bmi(height, weight):
 print("Height = " , height)
 print("Weight = " , weight)
 BMI = weight/(height**2)
 print ("BMI=", round(BMI,2))
 if BMI<18.5:
     print ("undeweight")
 elif BMI > 25.0:
        print ("fat")
 else:
        print("Normal")

calculate_bmi(weight=57, height=1.73)
