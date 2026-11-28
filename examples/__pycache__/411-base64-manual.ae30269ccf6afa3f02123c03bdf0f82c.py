
# apl-source:1
# مثال 411 — ترميز Base64 يدويا
# apl-source:2
# Manual Base64 encoding
# apl-source:3
# Demonstrates: تحويل نص إلى base64
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/411-base64-manual.apl
# apl-source:6

# apl-source:7
أبجدية = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
# apl-source:8

# apl-source:9
def إلى_ثنائي8(عدد):
    # apl-source:10
    بتات = ""
    # apl-source:11
    for _ in range(8):
        # apl-source:12
        بتات = str(عدد % 2) + بتات
        # apl-source:13
        عدد = عدد // 2
    # apl-source:14
    return بتات
# apl-source:15

# apl-source:16
def من_ثنائي(بتات):
    # apl-source:17
    قيمة = 0
    # apl-source:18
    for ب in بتات:
        # apl-source:19
        قيمة = قيمة * 2
        # apl-source:20
        if ب == "1":
            # apl-source:21
            قيمة = قيمة + 1
    # apl-source:22
    return قيمة
# apl-source:23

# apl-source:24
def بيس64(نص_الدخل):
    # apl-source:25
    بتات = ""
    # apl-source:26
    for حرف in نص_الدخل:
        # apl-source:27
        بتات = بتات + إلى_ثنائي8(ord(حرف))
    # apl-source:28
    while len(بتات) % 6 != 0:
        # apl-source:29
        بتات = بتات + "0"
    # apl-source:30
    ناتج = ""
    # apl-source:31
    for ي in range(0, len(بتات), 6):
        # apl-source:32
        ناتج = ناتج + أبجدية[من_ثنائي(بتات[ي:ي + 6])]
    # apl-source:33
    return ناتج
# apl-source:34

# apl-source:35
print(بيس64("Hi"))
# apl-source:36
print(بيس64("APL"))
# apl-source:37
