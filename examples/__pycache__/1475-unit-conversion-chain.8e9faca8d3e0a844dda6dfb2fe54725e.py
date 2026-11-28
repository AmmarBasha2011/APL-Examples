
# apl-source:1
# مثال 1475 — تحويل الوحدات عبر الأساس
# apl-source:2
# Unit conversion via base unit
# apl-source:3
# Demonstrates: حسابات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1475-unit-conversion-chain.apl
# apl-source:6

# apl-source:7
# جدول معاملات إلى الوحدة الأساس
# apl-source:8
# التحويل ضرب ثم قسمة
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def حوّل(قيمة, من_وحدة, إلى_وحدة):
  # apl-source:19
  معامل = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000}
  # apl-source:20
  return قيمة * معامل[من_وحدة] / معامل[إلى_وحدة]
# apl-source:21

# apl-source:22
تأكد_يساوي(حوّل(1, "km", "m"), 1000.0, "كيلومتر")
# apl-source:23
تأكد_يساوي(حوّل(250, "cm", "m"), 2.5, "سنتيمتر")
# apl-source:24
تأكد_يساوي(حوّل(2, "m", "cm"), 200.0, "متر")
# apl-source:25
تأكد_يساوي(حوّل(5, "m", "m"), 5.0, "نفس الوحدة")
# apl-source:26
