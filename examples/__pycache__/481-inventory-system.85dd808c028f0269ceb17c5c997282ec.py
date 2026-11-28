
# apl-source:1
# مثال 481 — نظام مخزون
# apl-source:2
# Inventory system
# apl-source:3
# Demonstrates: أصناف وكميات وتنبيه نقص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/481-inventory-system.apl
# apl-source:6

# apl-source:7
مخزون = [
    # apl-source:8
    {"صنف": "أرز", "كمية": 50, "حد": 10},
    # apl-source:9
    {"صنف": "سكر", "كمية": 5, "حد": 10},
    # apl-source:10
    {"صنف": "زيت", "كمية": 20, "حد": 8}
# apl-source:11
]
# apl-source:12

# apl-source:13
print("تقرير المخزون:")
# apl-source:14
for صنف_مخزون in مخزون:
    # apl-source:15
    حالة = "متوفر"
    # apl-source:16
    if صنف_مخزون["كمية"] < صنف_مخزون["حد"]:
        # apl-source:17
        حالة = "تحتاج إعادة طلب"
    # apl-source:18
    print(صنف_مخزون["صنف"], صنف_مخزون["كمية"], "->", حالة)
# apl-source:19
