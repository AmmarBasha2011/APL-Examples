
# apl-source:1
# مثال 412 — ترميز URL يدويا
# apl-source:2
# Manual URL encoding
# apl-source:3
# Demonstrates: تحويل الأحرف الخاصة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/412-url-encode.apl
# apl-source:6

# apl-source:7
آمنة = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~"
# apl-source:8

# apl-source:9
def سداسي(عدد):
    # apl-source:10
    أرقام = "0123456789ABCDEF"
    # apl-source:11
    return أرقام[عدد // 16] + أرقام[عدد % 16]
# apl-source:12

# apl-source:13
def رمز_رابط(نص_الدخل):
    # apl-source:14
    ناتج = ""
    # apl-source:15
    for حرف in نص_الدخل:
        # apl-source:16
        if آمنة.find(حرف) >= 0:
            # apl-source:17
            ناتج = ناتج + حرف
        # apl-source:18
        elif حرف == " ":
            # apl-source:19
            ناتج = ناتج + "%20"
        # apl-source:20
        else:
            # apl-source:21
            ناتج = ناتج + "%" + سداسي(ord(حرف) % 256)
    # apl-source:22
    return ناتج
# apl-source:23

# apl-source:24
print(رمز_رابط("hello world!"))
# apl-source:25

# apl-source:26
آمنة = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~"
# apl-source:27
