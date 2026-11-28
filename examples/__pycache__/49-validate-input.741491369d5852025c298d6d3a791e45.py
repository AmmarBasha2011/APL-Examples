
# apl-source:1
# مثال 49 — التحقق من صحة المدخلات
# apl-source:2
# Input Validation
# apl-source:3
# Demonstrates: validation logic, error messages, re
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/49-validate-input.apl
# apl-source:6

# apl-source:7
def دالة_تحقق_بريد(نص):
    # apl-source:8
    if len(نص) < 5:
        # apl-source:9
        return False
    # apl-source:10
    if "@" not in نص:
        # apl-source:11
        return False
    # apl-source:12
    if "." not in نص:
        # apl-source:13
        return False
    # apl-source:14
    return True
# apl-source:15

# apl-source:16
تحقق_بريد = دالة_تحقق_بريد
def دالة_تحقق_رقم(نص):
    # apl-source:17
    for حرف in نص:
        # apl-source:18
        if حرف < "0" or حرف > "9":
            # apl-source:19
            return False
    # apl-source:20
    return True
# apl-source:21

# apl-source:22
تحقق_رقم = دالة_تحقق_رقم
def دالة_طول_كلمة_مرور(نص, الحد):
    # apl-source:23
    if len(نص) < الحد:
        # apl-source:24
        return False
    # apl-source:25
    return True
# apl-source:26

# apl-source:27
طول_كلمة_مرور = دالة_طول_كلمة_مرور
print("=== التحقق من المدخلات ===")
# apl-source:28
print("")
# apl-source:29
print("--- بريد إلكتروني ---")
# apl-source:30
for بريد in ["user@example.com", "bad-email", "a@b", "name@site.org"]:
    # apl-source:31
    if تحقق_بريد(بريد):
        # apl-source:32
        print("  ✓ " + بريد + ": صالح")
    # apl-source:33
    else:
        # apl-source:34
        print("  ✗ " + بريد + ": غير صالح")
# apl-source:35

# apl-source:36
print("")
# apl-source:37
print("--- رقم ---")
# apl-source:38
for رقم in ["12345", "12a45", "999"]:
    # apl-source:39
    if تحقق_رقم(رقم):
        # apl-source:40
        print("  ✓ " + رقم + ": رقم صحيح")
    # apl-source:41
    else:
        # apl-source:42
        print("  ✗ " + رقم + ": يحتوي حروف")
# apl-source:43

# apl-source:44
print("")
# apl-source:45
print("--- كلمة مرور ---")
# apl-source:46
for كلمة in ["short", "longenoughpassword"]:
    # apl-source:47
    if طول_كلمة_مرور(كلمة, 8):
        # apl-source:48
        print("  ✓ " + كلمة + ": قوية")
    # apl-source:49
    else:
        # apl-source:50
        print("  ✗ " + كلمة + ": قصيرة")
# apl-source:51
