import os

dir_path = r''
if __name__ == '__main__':
    x_file = os.path.join(os.getcwd(), "example.txt")
else:
    x_file = os.path.join(
        r'C:\Users\morozoval\OneDrive\PythonProjects\pydata-book\datasets\bitly_usagov', "example.txt"
    )