def hospital_expert_system():
         print("Welcome to Hospital Expert System")
         print("Answer the following questions with yes/no \n")
    
         fever=input("Do you have fever?").lower()
         cough=input("Do you have cough?").lower()
         chest_pain=input("Do you have chest_pain?").lower() 
         headache=input("Do you have headache?").lower()

         print("\n--- Diagnosis Result ---")
     
      
         if fever =="yes" and cough =="yes":
              print("Possible Condition: Flu or Inflection")
              print("Recommended:Visit General Physician")
              
         elif chest_pain =="yes":
              print("Possible Condition: Heart-related issue")
              print("Recommended:Consult CardioLogist immediately")
         
     
         elif headache == "yes" and fever == "yes":
            print("Possible Condition: Migraine or Viral Fever")
            print("Recommended: Visit Neurologist / General Physician")
    
         else:
            print("Condition unclear")
            print("Recommended: General check-up")
    
         print("\nStay safe and take care!")
    
 
hospital_expert_system()