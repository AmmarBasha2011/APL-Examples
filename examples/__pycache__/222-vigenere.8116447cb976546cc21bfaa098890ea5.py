
# apl-source:1
# مثال 222 — شيفرة فيجنير
# apl-source:2
# Vigenere cipher
# apl-source:3
# Demonstrates: مفتاح متكرر، إزاحات متغيرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/222-vigenere.apl
# apl-source:6

# apl-source:7
def فيجنير(نص_الدخل, مفتاح, فك):
    # apl-source:8
    نتيجة = ""
    # apl-source:9
    ي = 0
    # apl-source:10
    for حرف in نص_الدخل:
        # apl-source:11
        if حرف >= "a" and حرف <= "z":
            # apl-source:12
            إزاحة = ord(مفتاح[ي % len(مفتاح)]) - 97
            # apl-source:13
            if فك:
                # apl-source:14
                إزاحة = 26 - إزاحة
            # apl-source:15
            نتيجة = نتيجة + chr((ord(حرف) - 97 + إزاحة) % 26 + 97)
            # apl-source:16
            ي = ي + 1
        # apl-source:17
        else:
            # apl-source:18
            نتيجة = نتيجة + حرف
    # apl-source:19
    return نتيجة
# apl-source:20

# apl-source:21
رسالة = "attack at dawn"
# apl-source:22
مشفرة = فيجنير(رسالة, "lemon", False)
# apl-source:23
print("الأصل:", رسالة)
# apl-source:24
print("المشفرة:", مشفرة)
# apl-source:25
print("المفكوكة:", فيجنير(مشفرة, "lemon", True))
# apl-source:26
