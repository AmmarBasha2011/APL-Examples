
# apl-source:1
# مثال 1997 — تدوير القائمة لليسار بعدد خطوات
# apl-source:2
# Rotate list left by k
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1997-rotate-list-left-by-k-steps.apl
# apl-source:6

# apl-source:7
# # التدوير بطول القائمة لا يغير شيئا
# apl-source:8
# # لذلك نأخذ الباقي
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
def دور(ق, ك):
  # apl-source:19
  if len(ق) == 0:
    # apl-source:20
    return []
  # apl-source:21
  ك = ك % len(ق)
  # apl-source:22
  return ق[ك:] + ق[:ك]
# apl-source:23

# apl-source:24
تأكد_يساوي(دور([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2], "خطوتان")
# apl-source:25
تأكد_يساوي(دور([1, 2, 3, 4, 5], 7), [3, 4, 5, 1, 2], "أكبر من الطول")
# apl-source:26
تأكد_يساوي(دور([], 3), [], "فارغة")
# apl-source:27
