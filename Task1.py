Nayan_Dict = {'Nayan': 30,'Moni':40,'Deka':50,'Alice':85,'Master':100}  # Dictionary created with name is key and marks as value
  
Stud_Name = input("Enter the student's name : ")                       # Takes user input
try:
    print(Stud_Name,"'s Marks : ",Nayan_Dict[Stud_Name])              # Display the key value
except:
    print(Nayan_Dict.get(Stud_Name,"Student not found"))              # Key not found

