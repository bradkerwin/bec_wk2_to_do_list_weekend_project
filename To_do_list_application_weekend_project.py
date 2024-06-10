your_current_tasks = []
completed_tasks = []

def new_task(): # Creating a function that adds a new task to our list.
   while True: # while loop created for to execute code as long as our condition is True.
       users_new_task = input("Please enter the details of the new task you would like to create. ") # Asks the user to enter the task they wish to add to their list.
       print(f"Your new task: ", {users_new_task})
       correct = input("Does this information look correct? ") # Confirming the user input is correct.
       if correct == 'yes': # If the user input is 'yes'.
           your_current_tasks.append(users_new_task) # Adding the users new task to the list your_current_tasks.
           print(f"Thank you. Your new task has been added successfully. ", {users_new_task})
           break # Breaks out of the while loop
       else: # If the user input for the variable correct is anything other than 'yes'.
           continue # Continues the while loop by going back to the top.

def mark_complete():
    while True: # while loop created for to execute code as long as our condition is True.
        try: # try statement added for what the function will do if the user enters a VALID input.
            finished = input("Which task would you like to mark as complete? ") # Asks the user which task they completed.
            completion_mark = ': X' # A variable that contains a string that will be  used to mark a task has been completed.
            if finished in your_current_tasks: # Iterates through the current tasks list to confirm the users input is found in the list.
                finish = finished + completion_mark # String concatenation if the user input and the completion mark, saved in a new variable.
                your_current_tasks.remove(finished) # Removes the finished task from the current tasks list.
                completed_tasks.append(finish) # Adds the finished task to the finished tasks list.
                print(f"Congrats!, {finished}, has been completed! Keep up the great work!")
                break # Breaks out of the while loop.
            else: # Executes in case the if statement's condition is not met.
                continue # Returns to the beginning of the loop if user input is invalid.
        except: # except statement added in case the user enters a task that is not found on the list to avoid errors.
            print("Task not found. Please try again. ")
            continue # Returns to the beginning of the while loop.

def view_tasks(): # Function to view our tasks.
    print(f"Here are your current tasks: {your_current_tasks} ") # Prints the list of current tasks.
    print(f"Completed tasks: {completed_tasks}") # Prints the list of completed tasks.

def delete_task(): # Function to delete a task.
    while True: # while loop created for to execute code as long as our condition is True.
        try: # try statement added for if the user enters a VALID input.
            delete = input("Which task would you like to delete from your list? ") # Asks user what task they want to delete.
            confirm = input("Are you sure you would like to delete this item? ") # Confirmation that the user entered the task they want to delete.
            if confirm == 'yes':
                your_current_tasks.remove(delete) # Removes the task from the list your_current_tasks.
                print(f"{delete} has been removed from your list. ")
                break # Breaks out of the while loop.
            else: # Executes if the user does not input 'yes'.
                continue # Returns to the beginning of the loop if user input is anything other than 'yes'.
        except: # except statement added in case the user enters a task that is not found on the list to avoid errors.
            print("Task not found. Please try again. ")
            continue # Returns the user to the beginning of the loop.

def main(): # Defining our main function. We will be calling all of our existing functions within this main function based on user input.
    while True: # while loop created for to execute code as long as our condition is True.
        user_decision = input('''
Welcome to the To-Do List App!

 Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit
''') # Multi-line string that asks the user to input an option 1-5.
        if user_decision == '1':
            new_task() # Function for adding a new task.
        elif user_decision == '2':
            view_tasks() # Function for viewing current tasks.
        elif user_decision == '3':
            mark_complete() # Function to mark a task as complete.
        elif user_decision == '4':
            delete_task() # Function to delete an existing task.
        elif user_decision == '5':
            print("Thank you for using our To Do List app! Have a great day!")
            break # break statement added so that the user does not get stuck in an infinite loop.
        else: # Executes if the user does not input a valid entry.
            print("Invalid entry. Please try again.") # If the user enters an invalid input, this message is printed to the terminal.
main() # Calling our main function.