from rfnit_tools.RFNIT import RFNIT
import win32com.client
import time
# file:///C:/ORiN2/CAO/ProviderLib/DENSO/RC8/Doc/RC8_ProvGuide_en.pdf p91

class RobotCobotta(RFNIT):

    def __init__(self, parameter, smartphone, arm, touch_pen, speed=50):
        p_center = [312.7559, -81.32734, 198.3072, -90.01537, 89.99992, -90.01537, 257]
        p_home = [131.579, -45, 300, 180, 90, -180, 261]
        p_camera = [252.6023, -151.48, 198.3072, -113.342, 89.99997, -113.342, 257]

        super().__init__("Cobotta", smartphone, arm, touch_pen, p_center, p_home, p_camera)

        eng = win32com.client.Dispatch("CAO.CaoEngine")
        self.ctrl = eng.Workspaces(0).AddController("RC8", "caoProv.DENSO.RC8", "", parameter)
        self.arm1 = self.ctrl.AddRobot("RC8", "")
        self.arm1.Execute("TakeArm", 0)
        self.arm1.Execute("ExtSpeed", speed)


    def touch(self, x, y):
        if x > self.smartphone_width or y > self.smartphone_height:
            self.print_red(f"Coordinate outside the smartphone area: {self.smartphone_width} x {self.smartphone_height}")
            self.print_red(f" x={x}, y={y}")
            return
        if x < 0 or y < 0:
            self.print_red(f"Negative value x={x}, y={y}")
            return
        print(f"RobotA touch at ({x}, {y})")
        target = self.initial_coordinate.copy()
        target[1] -= x
        target[2] += y
        # target = (312.7559, -81.32734+self.smartphone_width/2-x, 198.3072-self.smartphone_height/2+y, -90.01537, 89.99992, -90.01537, 257)
        self.arm1.Execute("Approach", [1, f"P{tuple(target)}", "@0 30"])
        self.arm1.Move(1, f"@P P{tuple(target)}", "")
        self.arm1.Execute("Approach", [1, f"P{tuple(target)}", "@0 30"])

    def swipe(self, start_x, start_y, end_x, end_y):
        print(f"RobotA swipe from ({start_x}, {start_y}) to ({end_x}, {end_y})")

        target_start = self.initial_coordinate.copy()
        target_start[1] -= start_x
        target_start[2] += start_y

        target_end = self.initial_coordinate.copy()
        target_end[1] -= end_x
        target_end[2] += end_y
        self.arm1.Execute("Approach", [1, f"P{tuple(target_start)}", "@0 30"])
        self.arm1.Move(2, f"@P P{tuple(target_start)}", "")
        self.arm1.Move(2, f"@P P{tuple(target_end)}", "")
        self.arm1.Execute("Approach", [1, f"P{tuple(target_end)}", "@0 30"])

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
        self.print_green(f"Robot {self.name} performing double rotation")

        self.arm1.Move(1, f"@P P{tuple(self.p_camera)}", "")
        time.sleep(1)

        posi_end2 = list(self.arm1.Execute("CurJnt"))
        posi_end2[5] += 90
        self.arm1.Move(1, f"J{tuple(posi_end2)}", "")
        time.sleep(1)

        self.arm1.Move(1, f"@P P{tuple(self.p_camera)}", "")
        time.sleep(1)

    def write_text(self, text):
        print(f"RobotA writing text: {text}")

    def read_nfc(self):
        print("RobotA reading NFC")

    def calibration(self):
        print("RobotA calibration")

    def home(self):
        self.arm1.Move(1, f"@P P{tuple(self.p_home)}", "")

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
