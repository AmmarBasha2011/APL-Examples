
# apl-source:1
# مثال 262 — قياس قوة كلمة المرور
# apl-source:2
# Password strength checker
# apl-source:3
# Demonstrates: فحص شروط متعددة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/262-password-strength.apl
# apl-source:6

# apl-source:7
def قوة(كلمة):
    # apl-source:8
    نقاط = 0
    # apl-source:9
    if len(كلمة) >= 8:
        # apl-source:10
        نقاط = نقاط + 1
    # apl-source:11
    if len(كلمة) >= 12:
        # apl-source:12
        نقاط = نقاط + 1
    # apl-source:13
    فيها_رقم = False
    # apl-source:14
    فيها_كبير = False
    # apl-source:15
    فيها_رمز = False
    # apl-source:16
    for حرف in كلمة:
        # apl-source:17
        if حرف >= "0" and حرف <= "9":
            # apl-source:18
            فيها_رقم = True
        # apl-source:19
        if حرف >= "A" and حرف <= "Z":
            # apl-source:20
            فيها_كبير = True
        # apl-source:21
        if حرف in "!@#$%":
            # apl-source:22
            فيها_رمز = True
    # apl-source:23
    if فيها_رقم:
        # apl-source:24
        نقاط = نقاط + 1
    # apl-source:25
    if فيها_كبير:
        # apl-source:26
        نقاط = نقاط + 1
    # apl-source:27
    if فيها_رمز:
        # apl-source:28
        نقاط = نقاط + 1
    # apl-source:29
    match نقاط:
        # apl-source:30
        case 5:
            # apl-source:31
            return "قوية جدا"
        # apl-source:32
        case 4:
            # apl-source:33
            return "قوية"
        # apl-source:34
        case 3:
            # apl-source:35
            return "متوسطة"
        # apl-source:36
        case _:
            # apl-source:37
            return "ضعيفة"
# apl-source:38

# apl-source:39
print("abc:", قوة("abc"))
# apl-source:40
print("Password1:", قوة("Password1"))
# apl-source:41
print("Str0ng!Pass#:", قوة("Str0ng!Pass#"))
# apl-source:42
