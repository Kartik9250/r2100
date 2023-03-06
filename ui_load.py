import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib
import r2100_communication.r2100_comm as r
import serial


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
        request = (0xde, 0x01, 0x05, 0x59, 0x83)
        self.get_data = r.get_Data(ser, request)

        self.setWindowTitle('Set Matplotlib Chart Value with QLineEdit Widget')
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.canvas = FigureCanvas(plt.Figure(figsize=(15, 6)))
        layout.addWidget(self.canvas)

        self.insert_ax()
        while True:
            self.update_chart()
            yield 0
    def insert_ax(self):
        font = {
            'weight': 'normal',
            'size': 16
        }
        matplotlib.rc('font', **font)

        self.ax = self.canvas.figure.subplots()

        self.bar = None

    def update_chart(self):
        value = self.get_data.decimal_dist()

        x_position = [1,2,3,4,5,6,7,8,9,10,11]

        if self.bar:
            self.bar.remove()
        self.bar = self.ax.bar(x_position, value, width=0.5, color='g')
        self.canvas.draw()

if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 30px;
        }
    ''')
    
    myApp = MyApp()
    plt.autoscale()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')