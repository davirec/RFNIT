import win32com.client


eng = win32com.client.Dispatch("CAO.CaoEngine")
ctrl = eng.Workspaces(0).AddController("RC8", "caoProv.DENSO.RC8", "", "Server=172.27.9.56")
Arm1 = ctrl.AddRobot("RC8", "")


Arm1.Execute("TakeArm", 0)
Arm1.Execute("ExtSpeed", 100)


Arm1.Execute("Approach", [1, "P2", "@0 30"])
Arm1.Move(1, "@P P2", "")
Arm1.Execute("Approach", [1, "P2", "@0 30"])
# Arm1.Execute("Depart", [1, "@P 100"])
Arm1.Move(1, "@P P1", "")


# p2
# "@P P(312.7559, -81.32734, 198.3072, -90.01537, 89.99992, -90.01537, 257)"


# p1
# "@P P(131.579, -45, 300, 180, 90, -180, 261)"


p1 = "P(131.579, -45, 300, 180, 90, -180, 261)"
p2 = "P(312.7559, -81.32734, 198.3072, -90.01537, 89.99992, -90.01537, 257)"


Arm1.Execute("Approach", [1, p2, "@0 30"])
Arm1.Move(1, f"@P {p2}", "")
Arm1.Execute("Approach", [1, p2, "@0 30"])
# Arm1.Execute("Depart", [1, "@P 100"])
Arm1.Move(1, f"@P {p1}", "")