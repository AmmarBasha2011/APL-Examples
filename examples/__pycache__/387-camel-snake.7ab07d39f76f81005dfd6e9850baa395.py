
# apl-source:1
# مثال 387 — تحويل camelCase إلى snake_case
# apl-source:2
# Camel to snake case
# apl-source:3
# Demonstrates: إدراج شرطة قبل الحروف الكبيرة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/387-camel-snake.apl
# apl-source:6

# apl-source:7
def إلى_ثعبان(نص_الدخل):
    # apl-source:8
    نتيجة = ""
    # apl-source:9
    for حرف in نص_الدخل:
        # apl-source:10
        if حرف >= "A" and حرف <= "Z":
            # apl-source:11
            if len(نتيجة) > 0:
                # apl-source:12
                نتيجة = نتيجة + "_"
            # apl-source:13
            نتيجة = نتيجة + حرف.lower()
        # apl-source:14
        else:
            # apl-source:15
            نتيجة = نتيجة + حرف
    # apl-source:16
    return نتيجة
# apl-source:17

# apl-source:18
def إلى_جمل(نص_الدخل):
    # apl-source:19
    أجزاء = نص_الدخل.split("_")
    # apl-source:20
    نتيجة = أجزاء[0]
    # apl-source:21
    for ي in range(1, len(أجزاء)):
        # apl-source:22
        نتيجة = نتيجة + أجزاء[ي][0].upper() + أجزاء[ي][1:]
    # apl-source:23
    return نتيجة
# apl-source:24

# apl-source:25
print(إلى_ثعبان("helloWorldExample"))
# apl-source:26
print(إلى_جمل("hello_world_example"))
# apl-source:27
