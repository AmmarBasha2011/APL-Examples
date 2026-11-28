
# apl-source:1
# مثال 221 — شيفرة قيصر
# apl-source:2
# Caesar cipher
# apl-source:3
# Demonstrates: ترميز_حرف، فك_ترميز_حرف، الإزاحة الدائرية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/221-caesar-cipher.apl
# apl-source:6

# apl-source:7
def قيصر(نص_الدخل, إزاحة):
    # apl-source:8
    نتيجة = ""
    # apl-source:9
    for حرف in نص_الدخل:
        # apl-source:10
        if حرف >= "a" and حرف <= "z":
            # apl-source:11
            نتيجة = نتيجة + chr((ord(حرف) - 97 + إزاحة) % 26 + 97)
        # apl-source:12
        elif حرف >= "A" and حرف <= "Z":
            # apl-source:13
            نتيجة = نتيجة + chr((ord(حرف) - 65 + إزاحة) % 26 + 65)
        # apl-source:14
        else:
            # apl-source:15
            نتيجة = نتيجة + حرف
    # apl-source:16
    return نتيجة
# apl-source:17

# apl-source:18
رسالة = "Hello World"
# apl-source:19
مشفرة = قيصر(رسالة, 3)
# apl-source:20
print("الأصل:", رسالة)
# apl-source:21
print("المشفرة:", مشفرة)
# apl-source:22
print("فك التشفير:", قيصر(مشفرة, 23))
# apl-source:23
