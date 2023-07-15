# Function Plotter Application

> **Function Plotter is a Python application built using PySide2 and Matplotlib libraries that allows users to plot mathematical functions and perform various plot-related actions.**

## Features

> 🔹 Plot mathematical functions on a canvas using user-defined inputs. 📈  
>
> 🔹 Clear the existing plot and prepare for a new one. 🧹
> 
> 🔹 Add subplots on the canvas without erasing the previous plot. 📊
> 
> 🔹 Save the plot as an image file in PNG format. 💾
> 
> 🔹 Export the plot as a PDF file. 📄
> 
> 🔹 Zoom in and out of the plot by adjusting the x-axis and y-axis limits. 🔎
> 
> 🔹 Responsive and user-friendly graphical user interface (GUI). 🖥️

## Project Hierarchy
```
├── 🐍 main.py                     # Main entry point of the application
├── 🐍 main_window.py              # Contains the main window for the whole app sets up the user interface
├── 🐍 toolbar.py                  # Contains the Toolbar class for the GUI toolbar
├── 🐍 function_plotter.py         # Contains the FunctionPlotter class for inputting and plotting mathematical functions
├── 🐍 widgets_actions.py          # Contains the WidgetActions class with various actions for the application
├── 📂 assets/                     # Directory for storing application-related assets
│   ├── 📈 function.png
│   ├── 📊 blueprint--plus.png
│   ├── 💾 document-image.png
│   ├── 📄 blue-document-pdf-text.png
│   ├── 🔍+ magnifier-zoom-in.png
│   ├── 🔍- magnifier-zoom-out.png
│   └── 🌐 cross-script.png
└── 📃 README.md                   # Detailed documentation and information about the project
```



## Project Structure

The project follows a structured organization to maintain code modularity and separation of concerns. Here is an overview of the project structure and the purpose of each file:

- `🐍 main.py`: The main entry point of the application.
- `🐍 main_window.py`: It initializes the main window and sets up the user interface.
- `🐍 toolbar.py`: Contains the implementation of the toolbar widget, including actions for various functionality like new plot, add subplot, save image, etc.
- `🐍 function_plotter.py`: Defines the function plotter widget that allows users to input mathematical functions and set the range of the x-axis.
- `🐍 widgets_actions.py`: Implements the actions performed by the widgets, such as plotting a function, saving images, zooming in/out, etc.
- `📂 assets/`:
  - `📈 function.png`: Icon for the "New Plot" action.
  - `📊 blueprint--plus.png`: Icon for the "Add Subplot" action.
  - `💾 document-image.png`: Icon for the "Save Image" action.
  - `📄 blue-document-pdf-text.png`: Icon for the "Export PDF" action.
  - `🔍+ magnifier-zoom-in.png`: Icon for the "Zoom In" action.
  - `🔍- magnifier-zoom-out.png`: Icon for the "Zoom Out" action.
  - `🌐 cross-script.png`: Icon for the "Exit App" action.
- `📃 README.md`: The README file you are currently reading.

## Dependencies

- PySide2: The PySide2 library is used to create the GUI components of the application.
- Matplotlib: Matplotlib is used for generating the plots and customizing their appearance.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using the following command:
```
pip install PySide2 matplotlib
```
3. Run the `main.py` file to start the application.


## Acknowledgments

- [PySide2](https://wiki.qt.io/Qt_for_Python): PySide2 is a Python binding for the Qt framework used for creating cross-platform applications.
- [Matplotlib](https://matplotlib.org/): Matplotlib is a plotting library for the Python programming language.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a pull request or submit an issue in the GitHub repository.

## Contact

**For any inquiries or questions, please contact [ahmed88hamdi99@gmail.com](ahmed88hamdi99@gmail.com)**
