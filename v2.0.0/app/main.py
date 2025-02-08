from window import *

def size_window(window):
    window_width = int(window.winfo_screenwidth())
    window_height = int(window.winfo_screenheight() * 0.875)
    window.geometry(f"{window_width}x{window_height}+0+0")
    window.minsize(window_width, window_height)
    window.resizable(True, True)

def main():
    window = Tk()
    window.title('Python L-System Parser & Visualizer v2.0.0')
    size_window(window)  
    Window(window)
    window.configure(bg='black')  
    window.mainloop()

if __name__ == '__main__':
    main()