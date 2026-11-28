
# apl-source:1
# مثال 255 — السنوات الكبيسة
# apl-source:2
# Leap years
# apl-source:3
# Demonstrates: قاعدة الكبس، توليد قائمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/255-leap-years.apl
# apl-source:6

# apl-source:7
def كبيسة(سنة):
    # apl-source:8
    if سنة % 400 == 0:
        # apl-source:9
        return True
    # apl-source:10
    if سنة % 100 == 0:
        # apl-source:11
        return False
    # apl-source:12
    return سنة % 4 == 0
# apl-source:13

# apl-source:14
print("2024:", كبيسة(2024))
# apl-source:15
print("2100:", كبيسة(2100))
# apl-source:16
print("2000:", كبيسة(2000))
# apl-source:17

# apl-source:18
قائمة = [سنة for سنة in range(2020, 2051) if كبيسة(سنة)]
# apl-source:19
print("الكبيسة 2020-2050:", قائمة)
# apl-source:20
