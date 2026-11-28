
# apl-source:1
# مثال 227 — لغة الليت (1337)
# apl-source:2
# Leet speak
# apl-source:3
# Demonstrates: قاموس استبدال أحرف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/227-leet-speak.apl
# apl-source:6

# apl-source:7
ليت = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5", "t": "7", "l": "1", "g": "9"}
# apl-source:8

# apl-source:9
def إلى_ليت(نص_الدخل):
    # apl-source:10
    نتيجة = ""
    # apl-source:11
    for حرف in نص_الدخل.lower():
        # apl-source:12
        if حرف in ليت:
            # apl-source:13
            نتيجة = نتيجة + ليت[حرف]
        # apl-source:14
        else:
            # apl-source:15
            نتيجة = نتيجة + حرف
    # apl-source:16
    return نتيجة
# apl-source:17

# apl-source:18
print(إلى_ليت("elite hacker"))
# apl-source:19
print(إلى_ليت("aplnguage is great"))
# apl-source:20
