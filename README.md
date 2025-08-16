# **Tute_Dude_Python_Assignments_5**
Here I have uploaded two assignment files of python. Which are named as Task1.py and Task2.py respectivelly. Let me describe the functionality of each files separetlly.

#         **Task1.py**
Hear we hane created a dictionary as Nayan_dict and pass key as student names and value as marks of student.
Data on dictionary are :

                       | student name |  Marks | 
                       -------------------------
                       | Nayan        |      30|
                       | Moni         |      40|
                       | Deka         |      50|
                       | Alice        |      85|
                       | Master       |     100|
                       
Which are in the formate {'Nayan':30,'Moni':40,'Deka':50,'Alice':85,'Master':100}. Then we created a variable Stud_Name and call the input function to take input from user in Stud_Name variable.The we call the try:  Statement as we have to pass an student not found exception. So to do so in the try: part we call the print function and pass Stud_Name variable inside the Nayan_dict variable of dictionary to display the marks of the student. Now if the user enters the right key then it passes the value and gives the output else it moves to the except: part where we call the print function inside which we call Nayan_Dict variable with .get function and inside the .get function we pass the Stud_Name variable which contains the key, so that if the user enters a wrong key it display our custon generated message that student not found.

#         **Task2.py**
Hear we created a list as My_List and put integer items from 1 to 10 as 1,2,3,4,5,6,7,8,9,10 . then we call the print function to display the items of the list.Then we have to do list slicing using the index number of the items of the list. wh have to display the first five items of the list, so to do that we call the print function and pass our list i.e My_List and sliced it according to the index which starts from 0 and ends a number before i.e 5. Demostrating it:

                    List Items    [1,2,3,4,5,6,7,8,9,10]
                    Index----------0-1-2-3-4-5-6-7-8-9

So to display upto 5  we have to put the stop value in list to index 5 as it displays upto item 5 which on index 4 in the list. Now after doing that we have to diplay the number in revers order upto 5 for that we again call the print function and pass our list enement My_List and slice it as 4::-1 hear the list slice from index to 4 to null i.e : and gives a step -1 sothen the steps count in reverse order i.e frist index 4 then 3 and so on.


