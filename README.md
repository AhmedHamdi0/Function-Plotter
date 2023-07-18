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


## Demo Video

https://github.com/AhmedHamdi0/creative-agency/assets/119865529/43867742-e232-42e4-814d-56fe7f060ee6




## Screenshots
|                      Function Plotter App                      |                     Function Plot                     |                   Function Subplot                    |
|:--------------------------------------------------------------:|:-----------------------------------------------------:|:-----------------------------------------------------:|
|   <img width="1604"  src="GUI Figures/function plotter.png">   |    <img width="1604"  src="GUI Figures/plot.png">     |   <img width="1604"  src="GUI Figures/subplot.png">   |
|                        Invalid Function                        |                   Invalid Min value                   |                   Invalid Max Value                   |
|   <img width="1604"  src="GUI Figures/invalid function.png">   | <img width="1604"  src="GUI Figures/invalid min.png"> | <img width="1604"  src="GUI Figures/invalid max.png"> |
|                       Invalid Min > Max                        |                  Save Plot as Images                  |                      Export PDF                       |
| <img width="1604"  src="GUI Figures/min greater than max.png"> | <img width="1604"  src="GUI Figures/save image.png">  | <img width="1604"  src="GUI Figures/export pdf.png">  |
|                            Zoom In                             |                       Zoom Out                        |                       Exit App                        |
|       <img width="1604"  src="GUI Figures/zoom in.png">        |  <img width="1604"  src="GUI Figures/zoom out.png">   |  <img width="1604"  src="GUI Figures/exit app.png">   |

## Project Hierarchy
```
├── 🐍 main.py                       # Main entry point of the application
├── 🐍 main_window.py                # Contains the main window for the whole app sets up the user interface
├── 🐍 toolbar.py                    # Contains the Toolbar class for the GUI toolbar
├── 🐍 function_plotter.py           # Contains the FunctionPlotter class for inputting and plotting mathematical functions
├── 🐍 widgets_actions.py            # Contains the WidgetActions class with various actions for the application
├── 🐍 styles.py                     # Contains styles and themes for the GUI
├── 📂 Tests/                        # Directory for storing application-related assets
│   ├── 🐍 test_plotting_actions.py  # Contains test cases for the plot, add_subplot, and new_plot functions
│   └── 🐍 test_toolbar_actions.py   # Contains test cases for the save_image, export_pdf, zoom_in, zoom_out, and exit_app
│   └── 🐍 test_toolbar_widgets.py   # Contains test cases for the toolbar icons
│   ├── 🐍 test_validate_input.py    # Contains test cases for the validate_input function
├── 📂 Assets/                       # Directory for storing application-related assets
│   ├── 📈 function.png
│   ├── 📊 blueprint--plus.png
│   ├── 💾 document-image.png
│   ├── 📄 blue-document-pdf-text.png
│   ├── 🔍+ magnifier-zoom-in.png
│   ├── 🔍- magnifier-zoom-out.png
│   └── 🌐 cross-script.png
└── 📃 README.md                     # Detailed documentation and information about the project
```



## Project Structure

The project follows a structured organization to maintain code modularity and separation of concerns. Here is an overview of the project structure and the purpose of each file:

- `🐍 main.py`: The main entry point of the application.
- `🐍 main_window.py`: It initializes the main window and sets up the user interface.
- `🐍 toolbar.py`: Contains the implementation of the toolbar widget, including actions for various functionality like new plot, add subplot, save image, etc.
- `🐍 function_plotter.py`: Defines the function plotter widget that allows users to input mathematical functions and set the range of the x-axis.
- `🐍 widgets_actions.py`: Implements the actions performed by the widgets, such as plotting a function, saving images, zooming in/out, etc.
- `📂 Tests/`: 
  - `🐍 test_plotting_actions.py`:   Contains test cases for the plot, add_subplot, and new_plot functions
  - `🐍 test_toolbar_actions.py`:    Contains test cases for the save_image, export_pdf, zoom_in, zoom_out, and exit_app
  - `🐍 test_toolbar_widgets.py`:    Contains test cases for the toolbar icons
  - `🐍 test_validate_input.py`:     Contains test cases for the validate_input function
- `📂 Assets/`:
  - `📈 function.png`: Icon for the "New Plot" action.
  - `📊 blueprint--plus.png`: Icon for the "Add Subplot" action.
  - `💾 document-image.png`: Icon for the "Save Image" action.
  - `📄 blue-document-pdf-text.png`: Icon for the "Export PDF" action.
  - `🔍+ magnifier-zoom-in.png`: Icon for the "Zoom In" action.
  - `🔍- magnifier-zoom-out.png`: Icon for the "Zoom Out" action.
  - `🌐 cross-script.png`: Icon for the "Exit App" action.
- `📃 README.md`: The README file you are currently reading.

## Dependencies

- `PySide2`: The PySide2 library is used to create the GUI components of the application.
- `Matplotlib`: Matplotlib is used for generating the plots and customizing their appearance.
- `pytest`: a popular testing tool for Python. The pytest library simplifies writing test cases, making assertions, and handling fixtures.
- `pytest-qt`: is a plugin for the pytest testing framework that provides additional capabilities for testing PyQt and PySide applications. It simplifies the process of testing GUI applications by offering various fixtures and helper functions

## Installation and Using

> 1. Clone the repository to your local machine.
> 2. Install the required dependencies using the following command:
>```
> pip install PySide2 matplotlib
> ```
> 3. Run the `main.py` file to start the application.


## Testing and Mocking

> 🔹 The Function Plotter application uses the `pytest` testing framework to create unit tests for various components 
of the application. Additionally, it employs the `pytest-qt` plugin to facilitate GUI testing with PyQt or PySide. 
In some test cases, the application also utilizes the concept of mocking to isolate specific parts of the application for testing.
> 
> 🔹 Unit testing is a crucial part of the Function Plotter project to ensure the accuracy and reliability
of its functionality. The application's core features and actions are covered by unit tests, 
which verify the behavior of individual components in isolation.


### Test Framework and Dependencies

> 🔹 The unit tests are written using the `pytest` framework, a popular testing tool for Python. The `pytest` 
> library simplifies writing test cases, making assertions, and handling fixtures.
> 
> 🔹 Also using `pytest-qt`, a plugin for the pytest testing framework that provides additional
capabilities for testing PyQt and PySide applications. 
It simplifies the process of testing GUI applications by offering various fixtures and helper functions.

### Pytest Fixtures and QtBot

> The application uses the `pytest-qt` plugin to create a `qtbot` fixture that allows programmatic 
> interaction with the GUI. The `qtbot` fixture is used to simulate user interactions like button clicks,
> text inputs, and other widget interactions during the test cases. By using `qtbot`, we can verify that GUI components 
> behave as expected when subjected to various user actions.

### Mocking with Mocker

> To isolate specific functionalities and dependencies during testing, the application uses the `pytest-mock` 
library to create mock objects. Mocking allows us to replace real objects or functions with custom mock implementations 
that simulate the behavior of the real objects without executing the actual code. By doing so, we can control the responses 
of mocked functions and focus on testing specific parts of the application in isolation.

To run the unit tests, make sure you have installed the required dependencies by running:

```
pip install pytest pytest-qt
```

### Running the Unit Tests

To run the unit tests, execute the following command from the project's root directory:

```
pytest
```

## Contributing

> Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a pull request or submit an issue in the GitHub repository.

## Contact

> **For any inquiries or questions, please contact [ahmed88hamdi99@gmail.com](ahmed88hamdi99@gmail.com)**
