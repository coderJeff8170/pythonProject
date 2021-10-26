import tkinter as tk
# The main class that accepts user input and saves it into a file from a window.
class Data:
    def __init__(self):
        # Attributes
        self.__window = tk.Tk()
        self.__username_password = {}


        # Method execution
        self.__window_properties()
        self.__window_widgets()
        self.__window_loop()

    # Properties that alter the main window.
    def __window_properties(self):
        # Sets the window size and location it appears on screen.
        self.__window.geometry('550x350+680+350')

    # Adds widgets and packs them into the window.
    def __window_widgets(self):
        # Create widgets for the window here.
        username_label = tk.Label(text="Username")
        username_entry = tk.Entry()
        password_label = tk.Label(text="Password")
        self.password_entry = tk.Entry(show="*")
        login_button = tk.Button(text="Login", command=self.__on_button)
        welcome_label = tk.Label(text="Hello! Welcome to a simple program that let's you input basic information and store it.")

        # Pack widgets into the window here.
        username_label.pack()
        username_entry.pack()
        password_label.pack()
        self.password_entry.pack()
        login_button.pack()
        welcome_label.pack()

    def __on_button(self):
        print(self.password_entry.get())
    # Handles various information that the user inputs.
    def __information_handling(self):
        pass

    # This method listens for events, such as button clicks or keypresses, and blocks any code that comes after it from running until the window it’s called on is closed.
    def __window_loop(self):
        self.__window.mainloop()

def main():
    data = Data()

main()