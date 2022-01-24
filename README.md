# Attendence-Manager
- This is a program to check **attendence** of zoom classes
- The program checks attendence with a list of student and returns the people who are absent
- version 2

# Installation
1. To clone the repo type:
`git clone https://github.com/mathew4STAR/Attendence-Manager`
in cmd

2. change the directory
`cd Attendece-Manager`

3. run the file 
`python3 main.py`

# Setup

1. Run the main file

2. When the GUI opens click on `edit classes list`

3. Enter the class and section followed by the name of the students in that class (this has to be the same name they enter the zoom classes with) in the boxes. (This step has to be done every time a new class is added) (Every time you add a class please reload the program)

4. Change the second line in config file with your class stregth.

5. You can also change the first line if you want to add a buffer before the program starts running.

# Additional Setup

`This needs to be done only if there is a problem when the program is run (incase the program misclicks) `

1. Run *findloc.py* and search bar. The program should record your current mouse position after 5 seconds. The recording should print in the console copy it and paste it in the third line *config.txt*

2. Repeat step 1 but instead of hovering over the searchbox hover over your username and over the blue box.
And replace this value with the third line.

Note: *findloc.py* was added to make it easier to find the cordinates on the screen

 
# Usage
1. Open Zoom and open the participants list

2. Open cmd and change the directory

3. Run the file
`python3 main.py`

4. Once the GUI opens, click on `T1` and choose the class you want to check for.

5. Click on  `CHECK ATTENDANCE` button.

6. The program should print a list of participants and absentees in the Text box below the picture. 

`Note you may have to make small changes to the program for your use case, this program may have errors.`
