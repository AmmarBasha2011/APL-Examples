
# apl-source:1
# مثال 22 — محول درجات الحرارة
# apl-source:2
# Temperature Converter
# apl-source:3
# Demonstrates: math library, user functions, loops, formatting
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/22-temperature-converter.apl
# apl-source:6

# apl-source:7
def دالة_إلى_فهرنهايت(مئوية):
    # apl-source:8
    return مئوية * 9 / 5 + 32
# apl-source:9

# apl-source:10
إلى_فهرنهايت = دالة_إلى_فهرنهايت
def دالة_إلى_مئوية(فهرنهايت):
    # apl-source:11
    return (فهرنهايت - 32) * 5 / 9
# apl-source:12

# apl-source:13
إلى_مئوية = دالة_إلى_مئوية
def دالة_إلى_كلفين(مئوية):
    # apl-source:14
    return مئوية + 273.15
# apl-source:15

# apl-source:16
إلى_كلفين = دالة_إلى_كلفين
print("=== محول درجات الحرارة ===")
# apl-source:17
print("")
# apl-source:18
print("مئوية -> فهرنهايت -> كلفن")
# apl-source:19
print("-----------------------------------")
# apl-source:20
الحرارة = [-10, 0, 20, 25, 37, 100]
# apl-source:21
for مئوية in الحرارة:
    # apl-source:22
    ف = إلى_فهرنهايت(مئوية)
    # apl-source:23
    ك = إلى_كلفين(مئوية)
    # apl-source:24
    print(f"{مئوية:>6} -> {round(ف, 1):>6} -> {round(ك, 1):>7}")
# apl-source:25
print("")
# apl-source:26
print("عكس الاتجاه:")
# apl-source:27
for ف in [32, 68, 98, 212]:
    # apl-source:28
    print(f"  {ف} فهرنهايت = {round(دالة_إلى_مئوية(ف), 1)} مئوية")
# apl-source:29
