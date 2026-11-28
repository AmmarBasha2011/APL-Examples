
# apl-source:1
# مثال 565 — ترميز base62
# apl-source:2
# Base62 codec
# apl-source:3
# Demonstrates: base62، روابط قصيرة، ترميز وفك
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/565-base62-codec.apl
# apl-source:6

# apl-source:7
def تأكد_يساوي(فعلي, متوقع, اسم):
    # apl-source:8
    if فعلي != متوقع:
        # apl-source:9
        print("فشل:", اسم, "| متوقع:", متوقع, "| فعلي:", فعلي)
        # apl-source:10
        قياسي_نظام_اخرج(1)
    # apl-source:11
    print("ناجح:", اسم)
# apl-source:12

# apl-source:13

# apl-source:14
# ترميز base62 لروابط قصيرة
# apl-source:15
أبجدية = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# apl-source:16

# apl-source:17
def رمّز(ن):
    # apl-source:18
    if ن == 0:
        # apl-source:19
        return "0"
    # apl-source:20
    م = ""
    # apl-source:21
    while ن > 0:
        # apl-source:22
        م = أبجدية[(ن % 62)] + م
        # apl-source:23
        ن = ن // 62
    # apl-source:24
    return م
# apl-source:25

# apl-source:26
def فكّ(نص):
    # apl-source:27
    ن = 0
    # apl-source:28
    for حرف in نص:
        # apl-source:29
        فهرس = 0
        # apl-source:30
        for i in range(62):
            # apl-source:31
            if أبجدية[i] == حرف:
                # apl-source:32
                فهرس = i
        # apl-source:33
        ن = ن * 62 + فهرس
    # apl-source:34
    return ن
# apl-source:35

# apl-source:36
تأكد_يساوي(رمّز(12345), "3d7", "ترميز 12345")
# apl-source:37
تأكد_يساوي(فكّ("3d7"), 12345, "فك 3d7")
# apl-source:38
تأكد_يساوي(فكّ(رمّز(987654321)), 987654321, "رحلة ذهاب وعودة")
# apl-source:39
تأكد_يساوي(رمّز(0), "0", "الصفر")
# apl-source:40
