# **Tute_Dude_Python_Assignments_5**
Here I have uploaded two assignment files of python. Which are named as Task1.py and Task2.py respectivelly. Let me describe the functionality of each files separetlly.

#         **Task1.py**
Hear we hane created a dictionary as Nayan_dict and pass key as student names and value as marks of student.
Data on dictionary are :

                       | student name |  Marks |       
                       | Nayan        |      30|
                       | Moni         |      40|
                       | Deka         |      50|
                       | Alice        |      85|
                       | Master       |     100|
                       
Which are in the formate {'Nayan':30,'Moni':40,'Deka':50,'Alice':85,'Master':100}. Then we created a variable Stud_Name and call the input function to take input from user in Stud_Name variable.The we call the try:  Statement as we have to pass an student not found exception. So to do so in the try: part we call the print function and pass Stud_Name variable inside the Nayan_dict variable of dictionary to display the marks of the student. Now if the user enters the right key then it passes the value and gives the output else it moves to the except: part where we call the print function inside which we call Nayan_Dict variable with .get function and inside the .get function we pass the Stud_Name variable which contains the key, so that if the user enters a wrong key it display our custon generated message that student not found.

#         **Task2.py**
