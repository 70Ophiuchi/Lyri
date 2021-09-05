from lyri_imports import *
from lyri_config import *

# Error handling using Try... Except statement.
try:
    # Looping over the methods and using each method to get back a response.
    for x in METHODS:

        # Checking current method for request
        if x == "GET":
            response = requests.get(URL, BODY).status_code
        elif x == "POST":
            response = requests.post(URL, BODY).status_code
        elif x == "PUT":
            response = requests.put(URL, BODY).status_code
        elif x == "PATCH":
            response = requests.patch(URL, BODY).status_code
        elif x == "DELETE":
            response = requests.delete(URL).status_code
        else:
            response = 'Current setup does not have current method'

        # Appending response to results list.
        RESULTS.append(
                        { 
                        "Method" : x, 
                        "Status_Code": response
                        }
                    )

    # Taking user input for desired result method.
    while True:
        inpt = input("Return results as:\n" +
                    "1. List\n" +
                    "2. File\n" +
                    "OPTION (1 or 2): ")

    # Checking user input.
        if inpt == '1':
            # Printing Results list.
            print(RESULTS)
            exit()
        else:
            file_exists = os.path.isfile("Results.txt")
            
            # Checking if the Results file exists.
            if file_exists:
                while True:

                    # If the file exists, it will be overwritten, warning the user.
                    caution = input("The file Results.txt already exists in this directory," +
                                    "continuing will overwrite the contents of your file\n" +
                                    "Do you want to continue? (Y/N): ")
                    
                    # Checking user input.
                    if caution == 'Y':

                        # Adding results to a file.
                        with open('Results.txt', 'w') as f:
                            for x in RESULTS:
                                f.writelines(f"{x} \n")
                        print('Results File: ' + os.getcwd() + '\\Results.txt')
                        exit()
                    elif caution == 'N':
                        print("exiting...")
                        time.sleep(2)
                        exit()
                    else:
                        print("Please choose a valid option, Y or N.")

            elif inpt == '2':

                # Adding results to a file.
                with open('Results.txt', 'w') as f:
                    for x in RESULTS:
                        f.writelines(f"{x} \n")
                print('Results File Path: ' + os.getcwd() + '\\Results.txt')
                exit()

            else:
                print("Please choose a valid option, 1 or 2.")

# Error handling
except Exception as error:
        print('Could not connect to the given server, please try again later.\n' + f"ERROR: {str(error)}")
        exit()