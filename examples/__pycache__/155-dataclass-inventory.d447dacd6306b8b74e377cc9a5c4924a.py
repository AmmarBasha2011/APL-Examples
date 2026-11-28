from dataclasses import dataclass, field, asdict, astuple, replace
from dataclasses import dataclass, field, asdict, astuple, replace

# apl-source:1
# مثال 155 — جرد المنتجات بفئات البيانات
# apl-source:2
# Product inventory with dataclasses
# apl-source:3
# Demonstrates: @فئة_بيانات، حقول، قيم افتراضية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/155-dataclass-inventory.apl
# apl-source:6

# apl-source:7
@dataclass
# apl-source:8
class منتج:
    # apl-source:9
    اسم: str
    # apl-source:10
    سعر: float
    # apl-source:11
    كمية: int = 0
# apl-source:12

# apl-source:13
أ = منتج("تفاح", 5.5, 100)
# apl-source:14
ب = منتج("موز", 3.25)
# apl-source:15
print(أ)
# apl-source:16
print("إجمالي قيمة التفاح:", أ.سعر * أ.كمية)
# apl-source:17
print("موز بدون كمية:", ب.كمية)
# apl-source:18
print("متساويان؟", أ == منتج("تفاح", 5.5, 100))
# apl-source:19
