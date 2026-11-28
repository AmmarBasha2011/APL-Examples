
# apl-source:1
# مثال 1589 — تدوير القائمة لليسار
# apl-source:2
# Rotate list left by k
# apl-source:3
# Demonstrates: مصفوفات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1589-rotate-left-by-k.apl
# apl-source:6

# apl-source:7
# ك تؤخذ بالباقي على الطول
# apl-source:8
# نقطع القائمة ونعيد ترتيب الجزأين
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
def دوّر_يسار(أ, ك):
  # apl-source:19
  if len(أ) == 0:
    # apl-source:20
    return []
  # apl-source:21
  ك = ك % len(أ)
  # apl-source:22
  return أ[ك:len(أ)] + أ[0:ك]
# apl-source:23

# apl-source:24
تأكد_يساوي(دوّر_يسار([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2], "اثنان")
# apl-source:25
تأكد_يساوي(دوّر_يسار([1, 2, 3], 4), [2, 3, 1], "أكبر من الطول")
# apl-source:26
تأكد_يساوي(دوّر_يسار([], 3), [], "فارغة")
# apl-source:27
