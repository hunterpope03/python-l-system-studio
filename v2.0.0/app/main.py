from window import *

# def size_window():


def main():
    window = Tk()
    window.title('Python L-System Parser & Visualizer')
    size_window(window)
    window.resizable(True, True)
    Window(window)
    window.mainloop()

if __name__ == '__main__':
    main()