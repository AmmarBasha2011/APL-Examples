
# apl-source:1
# مثال 181 — الوراثة وتعدد الأشكال
# apl-source:2
# Inheritance and polymorphism
# apl-source:3
# Demonstrates: صنف، وراثة، تجاوز الدوال
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/181-inheritance.apl
# apl-source:6

# apl-source:7
class حيوان:
    # apl-source:8
    def __init__(ذات, اسم):
        # apl-source:9
        ذات.اسم = اسم
# apl-source:10

    # apl-source:11
    def صوت(ذات):
        # apl-source:12
        return "..."
# apl-source:13

    # apl-source:14
    def صف(ذات):
        # apl-source:15
        return ذات.اسم + " يقول " + ذات.صوت()
# apl-source:16

# apl-source:17
class قطة(حيوان):
    # apl-source:18
    def صوت(ذات):
        # apl-source:19
        return "مواء"
# apl-source:20

# apl-source:21
class كلب(حيوان):
    # apl-source:22
    def صوت(ذات):
        # apl-source:23
        return "نباح"
# apl-source:24

# apl-source:25
class بقرة(حيوان):
    # apl-source:26
    def صوت(ذات):
        # apl-source:27
        return "خوار"
# apl-source:28

# apl-source:29
حيوانات = [قطة("مشمش"), كلب("ركس"), بقرة("بقرة")]
# apl-source:30
for ح in حيوانات:
    # apl-source:31
    print(ح.صف())
# apl-source:32
