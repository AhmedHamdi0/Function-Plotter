class WidgetActions:
    def __init__(self, parent):
        self.parent = parent

    # Check input validation
    def validate_input(self, function_str, min_value_str, max_value_str):
        print("Validate input")

    # To plot a mathematical function on a canvas using matplotlib
    def plot(self):
        print("Plot")

    # Clear the existing figure and prepare for a new plot
    def new_plot(self):
        print("New plot")

    # To add subplot on the canvas without erasing the previous plot
    def add_subplot(self):
        print("Add subplot")

    # Save the plot as an image file with the chosen file name
    def save_image(self):
        print("Save image")

    # Export the plot as a PDF file with the chosen file name
    def export_pdf(self):
        print("Export PDF")

    # Zoom in of the plot by decreasing the x-axis and y-axis limits.
    def zoom_in(self):
        print("Zoom in")

    # Zoom out of the plot by increasing the x-axis and y-axis limits.
    def zoom_out(self):
        print("Zoom out")

    # Exit the application
    def exit_application(self):
        print("Exit")
