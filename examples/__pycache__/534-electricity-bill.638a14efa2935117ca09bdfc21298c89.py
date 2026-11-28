
# apl-source:1
# مثال 534 — فاتورة كهرباء بشرائح
# apl-source:2
# Electricity bill slabs
# apl-source:3
# Demonstrates: شرائح أسعار، فاتورة كهرباء
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/534-electricity-bill.apl
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
# فاتورة كهرباء منزلية بشرائح تقريبية (جنيه/ك.و.س)
# apl-source:15
def فاتورة(استهلاك):
    # apl-source:16
    شرائح = [[50, 0.68], [100, 0.78], [200, 0.95], [350, 1.55], [650, 1.55], [1000, 1.55]]
    # apl-source:17
    متبقي = استهلاك
    # apl-source:18
    سابق = 0
    # apl-source:19
    إجمالي = 0
    # apl-source:20
    for شريحة in شرائح:
        # apl-source:21
        if متبقي <= 0:
            # apl-source:22
            break
        # apl-source:23
        سعة = شريحة[0] - سابق
        # apl-source:24
        كمية = min(متبقي, سعة)
        # apl-source:25
        إجمالي = إجمالي + كمية * شريحة[1]
        # apl-source:26
        متبقي = متبقي - كمية
        # apl-source:27
        سابق = شريحة[0]
    # apl-source:28
    if متبقي > 0:
        # apl-source:29
        إجمالي = إجمالي + متبقي * 1.55
    # apl-source:30
    return round(إجمالي, 2)
# apl-source:31

# apl-source:32
تأكد_يساوي(فاتورة(30), 20.4, "شريحة أولى فقط")
# apl-source:33
تأكد_يساوي(فاتورة(80), 57.4, "شريحتان")
# apl-source:34
تأكد_يساوي(فاتورة(0), 0, "بدون استهلاك")
# apl-source:35
