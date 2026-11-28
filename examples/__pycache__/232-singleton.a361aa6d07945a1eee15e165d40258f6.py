
# apl-source:1
# مثال 232 — نمط المفرد
# apl-source:2
# Singleton pattern
# apl-source:3
# Demonstrates: نسخة واحدة مشتركة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/232-singleton.apl
# apl-source:6

# apl-source:7
class إعدادات:
    # apl-source:8
    def __init__(ذات):
        # apl-source:9
        ذات.قيم = {}
# apl-source:10

    # apl-source:11
    def ضع(ذات, مفتاح, قيمة):
        # apl-source:12
        ذات.قيم[مفتاح] = قيمة
# apl-source:13

    # apl-source:14
    def خذ(ذات, مفتاح):
        # apl-source:15
        return ذات.قيم.get(مفتاح, "غير موجود")
# apl-source:16

# apl-source:17
صندوق = {"نسخة": None}
# apl-source:18

# apl-source:19
def إعدادات_التطبيق():
    # apl-source:20
    if صندوق["نسخة"] == None:
        # apl-source:21
        صندوق["نسخة"] = إعدادات()
    # apl-source:22
    return صندوق["نسخة"]
# apl-source:23

# apl-source:24
أ = إعدادات_التطبيق()
# apl-source:25
أ.ضع("اللغة", "العربية")
# apl-source:26
ب = إعدادات_التطبيق()
# apl-source:27
print("نفس النسخة؟", أ == ب)
# apl-source:28
print("اللغة من ب:", ب.خذ("اللغة"))
# apl-source:29
