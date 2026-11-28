
# apl-source:1
# مثال 564 — تحقق IBAN
# apl-source:2
# IBAN validation
# apl-source:3
# Demonstrates: IBAN، mod 97، رقم تحقق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/564-iban-check.apl
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
# تحقق IBAN بمعيار mod-97 وتوليد رقم تحقق سليم
# apl-source:15
def رقم_تحويل(iban):
    # apl-source:16
    م = ""
    # apl-source:17
    for حرف in iban:
        # apl-source:18
        if حرف >= "0" and حرف <= "9":
            # apl-source:19
            م = م + حرف
        # apl-source:20
        else:
            # apl-source:21
            م = م + str(ord(حرف) - 55)
    # apl-source:22
    return م
# apl-source:23

# apl-source:24
def باقي97(iban):
    # apl-source:25
    ب = 0
    # apl-source:26
    for حرف in رقم_تحويل(iban):
        # apl-source:27
        ب = (ب * 10 + int(حرف)) % 97
    # apl-source:28
    return ب
# apl-source:29

# apl-source:30
def iban_صالح(iban):
    # apl-source:31
    if len(iban) != 29:
        # apl-source:32
        return False
    # apl-source:33
    return باقي97(iban[4:] + iban[:4]) == 1
# apl-source:34

# apl-source:35
جسم = "0001900500000000263180002"
# apl-source:36
سليم = ""
# apl-source:37
for تحقق in range(2, 99):
    # apl-source:38
    رقم = str(تحقق)
    # apl-source:39
    if تحقق < 10:
        # apl-source:40
        رقم = "0" + رقم
    # apl-source:41
    مرشح = "EG" + رقم + جسم
    # apl-source:42
    if iban_صالح(مرشح):
        # apl-source:43
        سليم = مرشح
# apl-source:44
print("IBAN سليم:", سليم)
# apl-source:45
تأكد_يساوي(iban_صالح(سليم), True, "المولد يمر")
# apl-source:46
تأكد_يساوي(iban_صالح(سليم[:6] + "9" + سليم[7:]), False, "المعدل يفشل")
# apl-source:47
تأكد_يساوي(iban_صالح("EG38"), False, "القصير يرفض")
# apl-source:48
