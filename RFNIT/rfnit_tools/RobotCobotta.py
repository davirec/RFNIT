from rfnit_tools.RFNIT import RFNIT
import win32com.client


class RobotCobotta(RFNIT):

    def __init__(self, parameter, smartphone, arm, touch_pen, speed=50):
        super().__init__("Cobotta", smartphone, arm, touch_pen)
        eng = win32com.client.Dispatch("CAO.CaoEngine")
        self.ctrl = eng.Workspaces(0).AddController("RC8", "caoProv.DENSO.RC8", "", parameter)
        self.arm1 = self.ctrl.AddRobot("RC8", "")
        self.arm1.Execute("TakeArm", 0)
        self.arm1.Execute("ExtSpeed", speed)

    def touch(self, x, y):
        print(f"RobotA touch at ({x}, {y})")
        p2 = "P(312.7559, -81.32734, 198.3072, -90.01537, 89.99992, -90.01537, 257)"

        self.arm1.Execute("Approach", [1, p2, "@0 30"])
        self.arm1.Move(1, f"@P {p2}", "")
        self.arm1.Execute("Approach", [1, p2, "@0 30"])

    def swipe(self, start_x, start_y, end_x, end_y):
        print(f"RobotA swipe from ({start_x}, {start_y}) to ({end_x}, {end_y})")

        # arm1.Execute("Approach", [1, "P2", "@0 30"])
        # arm1.Move(1, "@P P2", "")
        # arm1.Execute("Approach", [1, "P2", "@0 30"])
        # # arm1.Execute("Depart", [1, "@P 100"])
        # arm1.Move(1, "@P P1", "")
        #
        # # p2
        # # "@P P(312.7559, -81.32734, 198.3072, -90.01537, 89.99992, -90.01537, 257)"
        #
        # # p1
        # # "@P P(131.579, -45, 300, 180, 90, -180, 261)"
        #
        # p1 = "P(131.579, -45, 300, 180, 90, -180, 261)"
        # p2 = "P(312.7559, -81.32734, 198.3072, -90.01537, 89.99992, -90.01537, 257)"
        #
        # arm1.Execute("Approach", [1, p2, "@0 30"])
        # arm1.Move(1, f"@P {p2}", "")
        # arm1.Execute("Approach", [1, p2, "@0 30"])
        # # arm1.Execute("Depart", [1, "@P 100"])
        # arm1.Move(1, f"@P {p1}", "")

    def double_rotation(self):
        print("RobotA performing double rotation")

    def write_text(self, text):
        print(f"RobotA writing text: {text}")

    def read_nfc(self):
        print("RobotA reading NFC")

    def calibration(self):
        print("RobotA calibration")

    def home(self):
        p1 = "P(131.579, -45, 300, 180, 90, -180, 261)"
        self.arm1.Move(1, f"@P {p1}", "")

    # meio do smartphone tocando
    #
    # 312.7559 - 81.32734
    # 198.3072 - 90.01537
    # 89.99992 - 90.01537
    # 257 - Lefty | Above | Flip | J6Single | J4Single | J1Single | NonFlip2
    # 0
    #
    # superior meio
    # 312.7559 - 81.32734
    # 151.5203 - 90.09206
    # 89.99992 - 90.09206
    # 257 - Lefty | Above | Flip | J6Single | J4Single | J1Single | NonFlip2
    # 0
    #
    # inferior meio
    # 312.7559 - 81.32734
    # 257.6063 - 90.05091
    # 89.99992 - 90.05092
    # 257 - Lefty | Above | Flip | J6Single | J4Single | J1Single | NonFlip2
    # 0
    #
    # quina 0, 0 do smartphone máximo
    # 307.0894 - 2.760088
    # 115.1852 - 38.45113
    # 89.99981 - 38.45123
    # 257 - Lefty | Above | Flip | J6Single | J4Single | J1Single | NonFlip2
    # 0
    #
    # quina n, 0 do smartphone máximo
    # 307.0894 - 2.760192
    # 289.1236 - 35.42788
    # 89.99978 - 35.42802
    # 257 - Lefty | Above | Flip | J6Single | J4Single | J1Single | NonFlip2
    # 0
    #
    # quina n, n do smartphone
    # área
    # 312.7559 - 110.6938
    # 270.8528 - 62.16542
    # 89.99995 - 62.16543
    # 257 - Lefty | Above | Flip | J6Single | J4Single | J1Single | NonFlip2
    # 0
    #
    # quina 0, 0 do smartphne área
    # 312.7559 - 53.87764
    # 128.2277 - 60.27183
    # 89.99995 - 60.27185
    # 257 - Lefty | Above | Flip | J6Single | J4Single | J1Single | NonFlip2
    # 0
