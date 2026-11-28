
# apl-source:1
# مثال 25 — شيفرة قيصر
# apl-source:2
# Caesar Cipher
# apl-source:3
# Demonstrates: modular arithmetic, ord/chr, string building
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/25-caesar-cipher.apl
# apl-source:6

# apl-source:7
def دالة_شيفرة(النص, الإزاحة):
    # apl-source:8
    النتيجة = ""
    # apl-source:9
    for حرف in النص:
        # apl-source:10
        if حرف >= "a"  and حرف <= "z":
            # apl-source:11
            رمز = (ord(حرف) - 97 + الإزاحة) % 26 + 97
            # apl-source:12
            النتيجة = النتيجة + chr(رمز)
        # apl-source:13
        elif حرف >= "A"  and حرف <= "Z":
            # apl-source:14
            رمز = (ord(حرف) - 65 + الإزاحة) % 26 + 65
            # apl-source:15
            النتيجة = النتيجة + chr(رمز)
        # apl-source:16
        else:
            # apl-source:17
            النتيجة = النتيجة + حرف
    # apl-source:18
    return النتيجة
# apl-source:19

# apl-source:20
شيفرة = دالة_شيفرة
الرسالة = "Hello, World! APL is amazing."
# apl-source:21
المفتاح = 3
# apl-source:22

# apl-source:23
print("=== شيفرة قيصر ===")
# apl-source:24
print("الأصلية : " + الرسالة)
# apl-source:25
المشفر = شيفرة(الرسالة, المفتاح)
# apl-source:26
print("المشفرة : " + المشفر)
# apl-source:27
print("مفكوكة : " + شيفرة(المشفر, 26 - المفتاح))
# apl-source:28
print("")
# apl-source:29
print("مفاتيح مختلفة على APL:")
# apl-source:30
for مفتاح in [1, 5, 13, 25]:
    # apl-source:31
    print("  shift " + str(مفتاح) + ": " + شيفرة("APL", مفتاح))
# apl-source:32
