# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
# PSrianomai,8/23/2025,Created Script
# ------------------------------------------------------------------------------------------ #
import io as _io #needed to try closing in the finally block
import json #import code from Python's JSON module into my script

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = '' # Hold the choice made by the user.


# TODO Create a Person Class (Done)
class Person: # no need to specify object. Python automatically do it
    """
    A class representing person data.

    Properties:
        student_first_name(str): The student's first name.
        student_last_name(str): The student's last name.

    ChangeLog:
        - PSrianomai, 8.23.2025: Created the class.
    """

# TODO Add first_name and last_name properties to the constructor (Done)
    #Per Assignment Class Properties section: The program includes properties
    #for student_first_name: str and defaults to an empty string
    #The program includes properties for student_last_name: str and
    #defaults to an empty string
    #constructor with private attributes __init__
    def __init__(self, student_first_name:str = '',
                 student_last_name: str = ''):
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name

# TODO Create a getter and setter for the first_name property (Done)
    @property # (Use this decorator for the getter or accessor)
    def student_first_name(self):
        return self.__student_first_name.title() # formatting code

    @student_first_name.setter
    def student_first_name(self, value: str):
        if value.isalpha() or value == "": # is character or empty string
            self.__student_first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

# TODO Create a getter and setter for the last_name property (Done)
    @property
    def student_last_name(self):
        return self.__student_last_name.title() # formatting code

    @student_last_name.setter
    def student_last_name(self, value: str):
        if value.isalpha() or value == "": # is character or empty string
            self.__student_last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

# TODO Override the __str__() method to return Person data (Done)
    # return a coma-separated string of data
    def __str__(self):
        return f'{self.student_first_name},{self.student_last_name}'

# TODO Create a Student class the inherits from the Person class (Done)
class Student(Person): # we call Student a child or sub class,
# and we call Person a parent or super class
    """
    A class representing student data.

    Properties:
        student_first_name (str): The student's first name.
        student_last_name (str): The student's last name.
        course_name (str): The student's course name.

    Changelog: (Who, When, What)
    PSrianomai, 8.23.2025, Create Class
    PSrianomai, 8.23.2025, Added properties and private attributes
    """
# TODO call to the Person constructor and pass it the first_name and (Done)
# last_name data
    #defines a constructor that accepts three parameters
    def __init__(self, student_first_name: str = '',
                 student_last_name: str = '',
                 course_name: str = ''):
        #use super method to call the constructor of the person class
        super().__init__(student_first_name=student_first_name,
                         student_last_name=student_last_name)

# TODO add a assignment to the course_name property using the
# course_name parameter (Done)
        self.course_name = course_name

# TODO add the getter for course_name
    @property
    def course_name(self):
        return self.__course_name

# TODO add the setter for course_name (Done)
    @course_name.setter
    def course_name(self, value: str): # I removed validation to
                                       # allow input as Python 100 format
        #if value.isalpha() or value == "":  # is character or empty string
        self.__course_name = value
        #else:
            #raise ValueError("The course name should not contain numbers.")

# TODO Override the __str__() method to return the Student data (Done)
    def __str__(self):
        return (f'{self.student_first_name},'
                f'{self.student_last_name},{self.course_name}')

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    PSrianomai,8.23.2025,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ Reads data from a JSON file and appends Student objects to
        the provided list. Also returns a separate list of Student objects.

        ChangeLog: (Who, When, What)
        PSrianomai,8.23.2025,Created function
        PSrianomai,8.23.2025, Converted list of dictionaries to
        list of student objects

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with
        file data

        :return: list of Student objects (also appends to student_data list)
        """
        # Convert the list of dictionary rows into a list of Student objects
        # student_objects = [] --want to move to outside try block as Pycharm
        # flag error because if exception occurs before student_objects is
        # defined, then Python won't know what to return but it doesn't meet
        # what listed in the Processing section in the Assignment.
        file = _io.TextIOWrapper  # add file as a local variable
        try:
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")
            json_students = json.load(file) #load function returns a list of
                                            # JSON dictionary row

            # Convert the list of dictionary rows into a list of Student
            # objects
            student_objects = []
            # TODO replace this line of code to convert dictionary data
            # to Student data (Done)
            #student_objects = json_students
            for student in json_students:
                student_object: Student = Student(
                                    student_first_name=student["FirstName"],
                                    student_last_name=student["LastName"],
                                    course_name=student["CourseName"])
                student_data.append(student_object) #convert dictionary data
                                                    # to Student data
                #student_objects.append(student_object) #append to a
                #Student objects

            file.close()

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem "
                                            "with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()

        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of
        dictionary rows

        ChangeLog: (Who, When, What)
        PSrianomai,8.23.2025,Created function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be written to the file

        :return: None
        """
        file = _io.TextIOWrapper  # add file as a local variable
        try:
            file = open(file_name, "w")
            # TODO Add code to convert Student objects into
            # dictionaries (Done)
            # it was listed as Done by Prof.
            # Create a new list to hold Json data to use with the json.dump()
            # function.
            list_of_dictionary_data: list = []
            for student in student_data:  # Convert List of Student objects
                                          # to list of dictionary rows.
                student_json: dict \
                    = {"FirstName": student.student_first_name,
                       "LastName": student.student_last_name,
                       "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)
            #file = open(file_name, "w")
            # Change the first argument to be the list of dictionary data
            json.dump(list_of_dictionary_data, file)
            #json.dump(student_data, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += ("Please check that the file is not open by "
                        "another program.")
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user
    input and output

    ChangeLog: (Who, When, What)
    PSrianomai,8.23.2025,Created Class, Added menu output and input
    functions, Added a function to display the data, Added a function
    to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        PSrianomai,8.23.2025,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        PSrianomai,8.23.2025,Created function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice() -> str:
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        PSrianomai,8.23.2025,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid
                                                   # the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        PSrianomai,8.23.2025,Created function
        PSrianomai,8.24.2025,Converted code to use student objects
        instead of dictionaries

        :param student_data: list of student object data to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:

            # TODO Add code to access Student object data instead of
            # dictionary data (Done)
            print(student.student_first_name,student.student_last_name,
                  student.course_name, sep=",") # separate by comma
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name,
        with a course name from the user

        ChangeLog: (Who, When, What)
        PSrianomai,8.23.2025,Created function
        PSrianomai,8.24.2030,Converted code to use student objects
        instead of dictionaries

        :param student_data: list of dictionary rows to be filled
        with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")

            # TODO Replace this code to use a Student objects instead of
            # a dictionary objects (Done)
            student = Student(student_first_name=student_first_name,
                              student_last_name=student_last_name,
                              course_name=course_name)
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} "
                  f"{student_last_name} "
                  f"for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the "
                                        "correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem "
                                        "with your entered data.", error=e)
        return student_data
#  End of function definitions

# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME,
                                             student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME,
                                         student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    #else:
        #print("Please only choose option 1, 2, or 3")

print("Program Ended")
