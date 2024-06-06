from rfnit_tools.RobotCobotta import RobotCobotta


def main():
    robots = [RobotCobotta()]

    for robot in robots:
        robot.screenshot()
        robot.touch(100, 200)
        robot.swipe(100, 200, 300, 400)
        robot.double_rotation()
        robot.write_text("Hello World")
        robot.read_nfc()
        robot.calibration()
        dimensions = robot.device_dimensions()
        print(f"Dimensions: {dimensions}")

if __name__ == "__main__":
    main()
