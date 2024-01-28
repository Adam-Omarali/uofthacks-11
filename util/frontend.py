from taipy import Gui

# Define the layout for the GUI
gui = Gui(
    menu_bar=False,
    layout="""
    <FilePicker bind="image_path" />
    <Button label="Process Image" on_click="process_image" />
    <Audio bind="audio_path" />
    """
)

# Initialize the state
gui.state.image_path = None
gui.state.audio_path = None
