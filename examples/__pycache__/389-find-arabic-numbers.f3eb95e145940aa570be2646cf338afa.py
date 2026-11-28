
# apl-source:1
# مثال 389 — الأرقام العربية المشرقية في نص
# apl-source:2
# Eastern Arabic digits
# apl-source:3
# Demonstrates: تحويل ٠١٢٣ إلى 0123
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/389-find-arabic-numbers.apl
# apl-source:6

# apl-source:7
شرقية = "٠١٢٣٤٥٦٧٨٩"
# apl-source:8

# apl-source:9
def إلى_غربية(نص_الدخل):
    # apl-source:10
    نتيجة = ""
    # apl-source:11
    for حرف in نص_الدخل:
        # apl-source:12
        موضع = شرقية.find(حرف)
        # apl-source:13
        if موضع >= 0:
            # apl-source:14
            نتيجة = نتيجة + str(موضع)
        # apl-source:15
        else:
            # apl-source:16
            نتيجة = نتيجة + حرف
    # apl-source:17
    return نتيجة
# apl-source:18

# apl-source:19
print(إلى_غربية("الرقم ٤٢ والعام ٢٠٢٦"))
# apl-source:20
print(إلى_غربية("٣٦٥"))
# apl-source:21
