
# apl-source:1
# مثال 474 — مولد رموز تحقق
# apl-source:2
# OTP generator
# apl-source:3
# Demonstrates: رمز 6 خانات حتمي من بذرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/474-otp-generator.apl
# apl-source:6

# apl-source:7
def رمز_تحقق(سر, عداد):
    # apl-source:8
    قيمة = سر * 1103515245 + عداد * 12345
    # apl-source:9
    قيمة = قيمة % 2147483648
    # apl-source:10
    return قيمة % 1000000
# apl-source:11

# apl-source:12
print("الرمز الأول:", رمز_تحقق(987654, 1))
# apl-source:13
print("الرمز الثاني:", رمز_تحقق(987654, 2))
# apl-source:14
print("نفس العداد = نفس الرمز:", رمز_تحقق(987654, 1))
# apl-source:15
