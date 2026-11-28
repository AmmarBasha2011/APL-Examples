
# apl-source:1
# مثال 1581 — تنبيهات إعادة التخزين
# apl-source:2
# Inventory restock alerts
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1581-inventory-restock-alerts.apl
# apl-source:6

# apl-source:7
# لكل صنف كمية وحد أدنى
# apl-source:8
# نرجع الأصناف الناقصة مرتبة
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
def ناقصة(مخزون, حدود):
  # apl-source:19
  نتيجة = []
  # apl-source:20
  for ص in مخزون:
    # apl-source:21
    if مخزون[ص] < حدود.get(ص, 0):
      # apl-source:22
      نتيجة.append(ص)
  # apl-source:23
  نتيجة.sort()
  # apl-source:24
  return نتيجة
# apl-source:25

# apl-source:26
تأكد_يساوي(ناقصة({"a": 5, "b": 1, "c": 0}, {"a": 3, "b": 2, "c": 1}), ["b", "c"], "صنفان")
# apl-source:27
تأكد_يساوي(ناقصة({"x": 10}, {"x": 10}), [], "على الحد")
# apl-source:28
تأكد_يساوي(ناقصة({"y": 1}, {}), [], "بلا حد")
# apl-source:29
