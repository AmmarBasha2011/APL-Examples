
# apl-source:1
# مثال 19 — نظام إدارة مخزون
# apl-source:2
# Inventory Management System
# apl-source:3
# Demonstrates: dictionaries, dataclasses-like, search, reports
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/19-inventory-system.apl
# apl-source:6

# apl-source:7
المخزون = {
    # apl-source:8
    "قلم": {"الكمية": 150, "السعر": 2, "الحد_الأدنى": 50},
    # apl-source:9
    "دفتر": {"الكمية": 30, "السعر": 15, "الحد_الأدنى": 20},
    # apl-source:10
    "ممحاة": {"الكمية": 10, "السعر": 5, "الحد_الأدنى": 25},
    # apl-source:11
    "مسطرة": {"الكمية": 80, "السعر": 8, "الحد_الأدنى": 30}
# apl-source:12
}
# apl-source:13

# apl-source:14
def قيمة_المخزون():
    # apl-source:15
    الإجمالي = 0
    # apl-source:16
    for صنف in المخزون:
        # apl-source:17
        الإجمالي = الإجمالي + المخزون[صنف]["الكمية"] * المخزون[صنف]["السعر"]
    # apl-source:18
    return الإجمالي
# apl-source:19

# apl-source:20
def أصناف_منخفضة():
    # apl-source:21
    النتيجة = []
    # apl-source:22
    for صنف in المخزون:
        # apl-source:23
        if المخزون[صنف]["الكمية"] < المخزون[صنف]["الحد_الأدنى"]:
            # apl-source:24
            النتيجة = النتيجة + [صنف]
    # apl-source:25
    return النتيجة
# apl-source:26

# apl-source:27
def إعادة_تعبئة(صنف, كمية):
    # apl-source:28
    المخزون[صنف]["الكمية"] = المخزون[صنف]["الكمية"] + كمية
# apl-source:29

# apl-source:30
print("=== إدارة المخزون ===")
# apl-source:31
print("")
# apl-source:32
print("--- تقرير الأصناف ---")
# apl-source:33
for صنف in المخزون:
    # apl-source:34
    ع = المخزون[صنف]
    # apl-source:35
    print("  " + صنف + ": كمية " + str(ع["الكمية"]) + " × " + str(ع["السعر"]) + " = " + str(ع["الكمية"] * ع["السعر"]))
# apl-source:36
print("")
# apl-source:37
print("قيمة المخزون الكلية: " + str(قيمة_المخزون()))
# apl-source:38
print("")
# apl-source:39
print("--- أصناف تحتاج إعادة تعبئة ---")
# apl-source:40
for صنف in أصناف_منخفضة():
    # apl-source:41
    print("  " + صنف + " (" + str(المخزون[صنف]["الكمية"]) + " < " + str(المخزون[صنف]["الحد_الأدنى"]) + ")")
# apl-source:42
print("")
# apl-source:43
إعادة_تعبئة("ممحاة", 40)
# apl-source:44
إعادة_تعبئة("دفتر", 10)
# apl-source:45
print("--- بعد إعادة التعبئة ---")
# apl-source:46
print("  ممحاة: " + str(المخزون["ممحاة"]["الكمية"]))
# apl-source:47
print("  دفتر:  " + str(المخزون["دفتر"]["الكمية"]))
# apl-source:48
print("  ما زال منخفضاً: " + str(أصناف_منخفضة()))
# apl-source:49
