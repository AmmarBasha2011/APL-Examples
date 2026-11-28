
# apl-source:1
# مثال 416 — تحويلات عددية
# apl-source:2
# Number base conversions
# apl-source:3
# Demonstrates: ثنائي وسداسي وثماني يدويا
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/416-hex-binary.apl
# apl-source:6

# apl-source:7
def إلى_أساس(عدد, أساس_التحويل):
    # apl-source:8
    if عدد == 0:
        # apl-source:9
        return "0"
    # apl-source:10
    أرقام = "0123456789ABCDEF"
    # apl-source:11
    ناتج = ""
    # apl-source:12
    while عدد > 0:
        # apl-source:13
        ناتج = أرقام[عدد % أساس_التحويل] + ناتج
        # apl-source:14
        عدد = عدد // أساس_التحويل
    # apl-source:15
    return ناتج
# apl-source:16

# apl-source:17
print("255 ثنائي:", إلى_أساس(255, 2))
# apl-source:18
print("255 سداسي:", إلى_أساس(255, 16))
# apl-source:19
print("255 ثماني:", إلى_أساس(255, 8))
# apl-source:20
