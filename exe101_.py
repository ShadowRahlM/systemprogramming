import os
import subprocess as sp


def os_exc(command):
    """
    Execute a command using os.system and subprocess.run.
    
    Parameters:
    command (str): The command to be executed.

    Returns:
    bool or CompletedProcess: False if the command fails using os.system, 
    otherwise the result of subprocess.run.
    """
    if os.system(command) != 0:
        # If os.system fails, return False
        return False
    else:
        # Run the command using subprocess and return the result
        return sp.run(command, shell=True)


def run():
    """
    Prompt the user to enter a command and execute it until 'exit' is entered.
    Supports 'ls', 'p' (pwd), 'df', and 'uname' commands.
    """
    while True:
        command = input('Enter command here [ls, p, uname, df, exit]: ').lower()
        if command == 'exit':
            break
        elif command == 'ls':
            os_exc('ls')
        elif command == 'p':
            os_exc('pwd')
        elif command == 'df':
            os_exc('df -h')
        elif command == 'uname':
            os_exc('uname -a')
        else:
            print('Invalid command, please try again.')


run()


def area(b, h):
    """
    Calculate the area of a triangle.

    Parameters:
    b (float): The base of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    return 0.5 * b * h


print(area(8, 55))


class RotationCounter:
    """
    A counter that increments and resets with rotation behavior (0-9).
    """
    def __init__(self, start=0):
        """
        Initialize the counter.

        Parameters:
        start (int): The starting value of the counter.
        """
        if not 0 <= start <= 9:
            raise ValueError('Start value must be between 0 and 9')
        self.counter = start

    def increment(self):
        """
        Increment the counter by 1 and rotate back to 0 after 9.

        Returns:
        int: The current value of the counter after increment.
        """
        self.counter += 1
        if self.counter > 9:
            self.counter = 0
        return self.counter

    def reset(self, value=0):
        """
        Reset the counter to a specified value.

        Parameters:
        value (int): The value to reset the counter to (must be between 0 and 9).

        Returns:
        int: The current value of the counter before resetting.
        """
        if not 0 <= value <= 9:
            raise ValueError('Value must be between 0 and 9')
        current_value = self.counter
        self.counter = value
        return current_value


# Uncomment the lines below to test the RotationCounter class
# test = RotationCounter(5)
# print(test.increment())
# print(test.increment())
# print(test.reset(3))
# print(test.increment())
