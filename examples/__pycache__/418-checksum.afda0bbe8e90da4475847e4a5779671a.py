
# apl-source:1
# مثال 418 — مجاميع تحقق
# apl-source:2
# Checksums
# apl-source:3
# Demonstrates: مجموع بسيط و XOR
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/418-checksum.apl
# apl-source:6

# apl-source:7
def مجموع_تحقق(نص_الدخل):
    # apl-source:8
    مجموع = 0
    # apl-source:9
    for حرف in نص_الدخل:
        # apl-source:10
        مجموع = (مجموع + ord(حرف)) % 256
    # apl-source:11
    return مجموع
# apl-source:12

# apl-source:13
def تحقق_سطر(سطر):
    # apl-source:14
    أجزاء = سطر.split("|")
    # apl-source:15
    return مجموع_تحقق(أجزاء[0]) == int(أجزاء[1])
# apl-source:16

# apl-source:17
بيانات = "HELLO"
# apl-source:18
print("المجموع:", مجموع_تحقق(بيانات))
# apl-source:19
print("سطر صحيح؟", تحقق_سطر("HELLO|" + str(مجموع_تحقق("HELLO"))))
# apl-source:20
print("سطر فاسد؟", تحقق_سطر("HELLO|1"))
# apl-source:21
