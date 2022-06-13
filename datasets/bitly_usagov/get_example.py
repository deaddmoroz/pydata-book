import os
import pathlib as p

dir_path = r''
if __name__ == '__main__':
    x_file = os.path.join(os.getcwd(), "example.txt")
else:
    x_file = os.path.join(
        p.Path(__file__).parent.resolve(), "example.txt"
    )