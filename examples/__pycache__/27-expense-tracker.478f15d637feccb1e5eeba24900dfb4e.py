
# apl-source:1
# مثال 27 — متتبع المصروفات
# apl-source:2
# Expense Tracker
# apl-source:3
# Demonstrates: lists of dicts, aggregation, sorting, formatting
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/27-expense-tracker.apl
# apl-source:6

# apl-source:7
المصروفات = [
    # apl-source:8
    {"الفئة": "طعام", "المبلغ": 250, "الوصف": "عشاء"},
    # apl-source:9
    {"الفئة": "نقل", "المبلغ": 80, "الوصف": "تاكسي"},
    # apl-source:10
    {"الفئة": "طعام", "المبلغ": 120, "الوصف": "غداء"},
    # apl-source:11
    {"الفئة": "تسوق", "المبلغ": 600, "الوصف": "ملابس"},
    # apl-source:12
    {"الفئة": "نقل", "المبلغ": 200, "الوصف": "مواصلات"},
    # apl-source:13
    {"الفئة": "تسوق", "المبلغ": 150, "الوصف": "كتب"}
# apl-source:14
]
# apl-source:15

# apl-source:16
def دالة_إجمالي():
    # apl-source:17
    المجموع = 0
    # apl-source:18
    for عنصر in المصروفات:
        # apl-source:19
        المجموع = المجموع + عنصر["المبلغ"]
    # apl-source:20
    return المجموع
# apl-source:21

# apl-source:22
إجمالي = دالة_إجمالي
def دالة_حسب_الفئة(الفئة):
    # apl-source:23
    المجموع = 0
    # apl-source:24
    for عنصر in المصروفات:
        # apl-source:25
        if عنصر["الفئة"] == الفئة:
            # apl-source:26
            المجموع = المجموع + عنصر["المبلغ"]
    # apl-source:27
    return المجموع
# apl-source:28

# apl-source:29
حسب_الفئة = دالة_حسب_الفئة
def دالة_أعلى_مصروف():
    # apl-source:30
    الأعلى = 0
    # apl-source:31
    الوصف = ""
    # apl-source:32
    for عنصر in المصروفات:
        # apl-source:33
        if عنصر["المبلغ"] > الأعلى:
            # apl-source:34
            الأعلى = عنصر["المبلغ"]
            # apl-source:35
            الوصف = عنصر["الوصف"]
    # apl-source:36
    return [الوصف, الأعلى]
# apl-source:37

# apl-source:38
أعلى_مصروف = دالة_أعلى_مصروف
print("=== متتبع المصروفات ===")
# apl-source:39
print("عدد المصروفات: " + str(len(المصروفات)))
# apl-source:40
print("")
# apl-source:41
print("--- حسب الفئة ---")
# apl-source:42
for فئة in ["طعام", "نقل", "تسوق"]:
    # apl-source:43
    print("  " + فئة + ": " + str(حسب_الفئة(فئة)))
# apl-source:44
print("")
# apl-source:45
print("--- التفاصيل ---")
# apl-source:46
for عنصر in المصروفات:
    # apl-source:47
    print("  " + عنصر["الوصف"] + ": " + str(عنصر["المبلغ"]) + " (" + عنصر["الفئة"] + ")")
# apl-source:48
print("")
# apl-source:49
print("الإجمالي الكلي: " + str(إجمالي()))
# apl-source:50
print("أعلى مصروف: " + أعلى_مصروف()[0] + " (" + str(أعلى_مصروف()[1]) + ")")
# apl-source:51
