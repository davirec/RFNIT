from abc import ABC, abstractmethod


class RFNIT(ABC):
    def __init__(self, name, smartphone, arm, touch_pen):
        # init robot
        self.name = name
        self.smartphone_width = smartphone.get('smartphone_width')
        self.smartphone_height = smartphone.get('smartphone_height')

        self.arm_central_x = arm.get('central_x')
        self.arm_central_y = arm.get('central_y')
        self.arm_central_z = arm.get('central_z')

        self.touch_pen_offset_x = touch_pen.get('touch_pen_offset_x')
        self.touch_pen_offset_y = touch_pen.get('touch_pen_offset_y')
        self.touch_pen_offset_z = touch_pen.get('touch_pen_offset_z')

    def convert_to_robot_coords(self, screen_x, screen_y):
        # Calculates the displacement in millimeters relative to the center of the screen
        offset_x = (screen_x - self.smartphone_width / 2)
        offset_y = (screen_y - self.smartphone_height / 2)

        # The spatial coordinates of the robot relative to the robot base
        robot_x = self.arm_central_x + offset_x + self.touch_pen_offset_x
        robot_y = self.arm_central_y + offset_y + self.touch_pen_offset_y
        robot_z = self.arm_central_z + self.touch_pen_offset_z

        return robot_x, robot_y, robot_z

    # Métodos comuns a todos os robôs
    def screenshot(self):
        print("Capturando screenshot")
        # Screenshot implementation

    def compare_screenshot(self, image1, image2):
        print("Comparando screenshots")
        # Implementação da comparação de screenshots

    def device_dimensions(self):
        print("Obtendo dimensões do dispositivo")
        # Implementação para obter dimensões do dispositivo

    def print_red(self, text):
        print('\x1b[6;30;43m' + text + '\x1b[0m')

    # Métodos que precisam ser implementados por cada robô específico
    @abstractmethod
    def touch(self, x, y):
        pass

    @abstractmethod
    def swipe(self, start_x, start_y, end_x, end_y):
        pass

    @abstractmethod
    def double_rotation(self):
        pass

    @abstractmethod
    def write_text(self, text):
        pass

    @abstractmethod
    def read_nfc(self):
        pass

    @abstractmethod
    def calibration(self):
        pass

    @abstractmethod
    def home(self):
        pass
