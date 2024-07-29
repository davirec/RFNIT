from rfnit_tools.RobotCobotta import RobotCobotta


smartphone = {"smartphone_width": 78, "smartphone_height": 160}
parameter = r"WPJ=C:\projetos_git\RFNIT\wincaps_cobotta\wincaps_cobotta.WPJ"
arm = {"central_x": 78, "central_y": 160,"central_z": 78}
touch_pen = {"touch_pen_offset_x": 78, "touch_pen_offset_y": 160,"touch_pen_offset_z": 78}

robot = RobotCobotta(parameter, smartphone, arm, touch_pen,100)

robot.touch(-30, -90)
robot.touch(230, 290)
robot.touch(30, 90)
robot.double_rotation()
robot.touch(70, 40)

robot.touch(10, 130)

robot.home()





