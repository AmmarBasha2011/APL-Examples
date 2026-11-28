
# apl-source:1
# مثال 40 — تحويل بين الأرقام العربية والهندية
# apl-source:2
# Arabic-Indic Digit Converter
# apl-source:3
# Demonstrates: ord/chr, string building, loops
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/40-latin-converter.apl
# apl-source:6

# apl-source:7
def دالة_إلى_عربية(رقم_نص):
    # apl-source:8
    الناتج = ""
    # apl-source:9
    for حرف in رقم_نص:
        # apl-source:10
        if حرف >= "0"  and حرف <= "9":
            # apl-source:11
            الناتج = الناتج + chr(ord(حرف) - 48 + 1632)
        # apl-source:12
        else:
            # apl-source:13
            الناتج = الناتج + حرف
    # apl-source:14
    return الناتج
# apl-source:15

# apl-source:16
إلى_عربية = دالة_إلى_عربية
def دالة_إلى_لاتينية(رقم_نص):
    # apl-source:17
    الناتج = ""
    # apl-source:18
    for حرف in رقم_نص:
        # apl-source:19
        if حرف >= "\u0660"  and حرف <= "\u0669":
            # apl-source:20
            الناتج = الناتج + chr(ord(حرف) - 1632 + 48)
        # apl-source:21
        else:
            # apl-source:22
            الناتج = الناتج + حرف
    # apl-source:23
    return الناتج
# apl-source:24

# apl-source:25
إلى_لاتينية = دالة_إلى_لاتينية
print("=== تحويل الأرقام ===")
# apl-source:26
print("")
# apl-source:27
أمثلة = ["2026", "3.14", "1000", "42"]
# apl-source:28
for رقم in أمثلة:
    # apl-source:29
    عربي = إلى_عربية(رقم)
    # apl-source:30
    لاتيني = إلى_لاتينية(عربي)
    # apl-source:31
    print("  " + رقم + " -> " + عربي + " -> " + لاتيني)
# apl-source:32
print("")
# apl-source:33
print("التحقق: " + str(إلى_لاتينية(إلى_عربية("2026")) == "2026"))
# apl-source:34
