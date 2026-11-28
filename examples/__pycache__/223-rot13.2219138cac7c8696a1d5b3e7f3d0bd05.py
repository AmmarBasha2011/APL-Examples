
# apl-source:1
# مثال 223 — ROT13
# apl-source:2
# ROT13 encoding
# apl-source:3
# Demonstrates: إزاحة ثابتة ذاتية العكس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/223-rot13.apl
# apl-source:6

# apl-source:7
def روت13(نص_الدخل):
    # apl-source:8
    نتيجة = ""
    # apl-source:9
    for حرف in نص_الدخل:
        # apl-source:10
        if حرف >= "a" and حرف <= "z":
            # apl-source:11
            نتيجة = نتيجة + chr((ord(حرف) - 97 + 13) % 26 + 97)
        # apl-source:12
        elif حرف >= "A" and حرف <= "Z":
            # apl-source:13
            نتيجة = نتيجة + chr((ord(حرف) - 65 + 13) % 26 + 65)
        # apl-source:14
        else:
            # apl-source:15
            نتيجة = نتيجة + حرف
    # apl-source:16
    return نتيجة
# apl-source:17

# apl-source:18
مشفر = روت13("APL Language")
# apl-source:19
print("مشفر:", مشفر)
# apl-source:20
print("مرتين = الأصل:", روت13(مشفر))
# apl-source:21
