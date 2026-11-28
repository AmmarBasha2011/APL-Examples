
# apl-source:1
# مثال 531 — الأرقام المشرقية
# apl-source:2
# Arabic-Indic digits
# apl-source:3
# Demonstrates: أرقام مشرقية، تحويل ترميز أرقام
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/531-arabic-indic-digits.apl
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
# تحويل الأرقام بين العربية الغربية والمشرقية
# apl-source:15
مشرقية = "٠١٢٣٤٥٦٧٨٩"
# apl-source:16

# apl-source:17
def إلى_مشرقية(نص):
    # apl-source:18
    ناتج = ""
    # apl-source:19
    for حرف in نص:
        # apl-source:20
        if حرف in "0123456789":
            # apl-source:21
            ناتج = ناتج + مشرقية[int(حرف)]
        # apl-source:22
        else:
            # apl-source:23
            ناتج = ناتج + حرف
    # apl-source:24
    return ناتج
# apl-source:25

# apl-source:26
def إلى_غربية(مدخل):
    # apl-source:27
    ناتج = ""
    # apl-source:28
    for حرف in مدخل:
        # apl-source:29
        وجد = False
        # apl-source:30
        for i in range(10):
            # apl-source:31
            if حرف == مشرقية[i]:
                # apl-source:32
                ناتج = ناتج + str(i)
                # apl-source:33
                وجد = True
        # apl-source:34
        if not وجد:
            # apl-source:35
            ناتج = ناتج + حرف
    # apl-source:36
    return ناتج
# apl-source:37

# apl-source:38
تأكد_يساوي(إلى_مشرقية("السعر 125 جنيه"), "السعر ١٢٥ جنيه", "غربية إلى مشرقية")
# apl-source:39
تأكد_يساوي(إلى_غربية("السنة ٢٠٢٤"), "السنة 2024", "مشرقية إلى غربية")
# apl-source:40
