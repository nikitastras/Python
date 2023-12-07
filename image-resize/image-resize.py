import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resized_pixmap = None
        self.initializeUI()

    def initializeUI(self):
        """Initialize the window and display its contents to the screen."""
        self.setWindowTitle('PyQt5 Image Resizer and Saver')
        self.setGeometry(100, 100, 500, 400)

        # Create a QVBoxLayout instance
        layout = QVBoxLayout()

        # Create a QPushButton for image selection and connect to the method
        self.img_button = QPushButton('Select Image', self)
        self.img_button.clicked.connect(self.openImageFileDialog)

        # Create a QPushButton to save the resized image
        self.save_button = QPushButton('Save Resized Image', self)
        self.save_button.clicked.connect(self.saveResizedImage)
        self.save_button.setEnabled(False)  # Disabled until an image is selected

        # Label to display the image
        self.image_label = QLabel('No image selected', self)
        self.image_label.setFixedSize(185, 185)  # Set fixed size for the label
        self.image_label.setScaledContents(True)  # The image will scale to fill the label

        # Add widgets to the layout
        layout.addWidget(self.img_button)
        layout.addWidget(self.image_label)
        layout.addWidget(self.save_button)

        # Set the layout for the main window
        self.setLayout(layout)

    def openImageFileDialog(self):
        """Open a file dialog to select an image and display it."""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "",
                                                   "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        if file_name:
            # Load image
            pixmap = QPixmap(file_name)
            # Resize the image
            self.resized_pixmap = pixmap.scaled(32, 32)
            self.image_label.setPixmap(self.resized_pixmap)
            # self.image_label.adjustSize()  # Not needed as the label size is now fixed
            self.save_button.setEnabled(True)  # Enable the save button

    def saveResizedImage(self):
        """Save the resized image to a new file."""
        if self.resized_pixmap:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                       "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg)",
                                                       options=options)
            if file_name:
                if not os.path.splitext(file_name)[1]:
                    file_name += '.png'  # Default to PNG if no extension is given
                self.resized_pixmap.save(file_name)
                QMessageBox.information(self, "Image Saved", "The resized image has been saved.")

def main():
    """Main function."""
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
