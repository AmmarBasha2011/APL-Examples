
# apl-source:1
# مثال 4947 — تدوير القائمة 8 خانات لليسار
# apl-source:2
# Rotate list left by 8
# apl-source:3
# Demonstrates: خوارزميات متقدمة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/4947-rotate-left-8.apl
# apl-source:6

# apl-source:7
# نقسم القائمة ونعيد ترتيبها
# apl-source:8

# apl-source:9
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:10
  if فعلي != متوقع:
    # apl-source:11
    print("فشل:", اسم)
    # apl-source:12
    print("  متوقع:", متوقع)
    # apl-source:13
    print("  فعلي:", فعلي)
    # apl-source:14
    قياسي_نظام_اخرج(1)
  # apl-source:15
  print("ناجح:", اسم)
# apl-source:16

# apl-source:17
def ف(ق):
  # apl-source:18
  if len(ق) == 0:
    # apl-source:19
    return ق
  # apl-source:20
  ك = 8 % len(ق)
  # apl-source:21
  return ق[ك:] + ق[:ك]
# apl-source:22

# apl-source:23
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6, 7]), [2, 3, 4, 5, 6, 7, 1], "حالة 1")
# apl-source:24
تأكد_يساوي(ف([1, 2]), [1, 2], "حالة 2")
# apl-source:25
تأكد_يساوي(ف([]), [], "حالة 3")
# apl-source:26
تأكد_يساوي(ف(["a", "b", "c", "d", "e", "f"]), ["c", "d", "e", "f", "a", "b"], "حالة 4")
# apl-source:27
