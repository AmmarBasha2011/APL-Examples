
# apl-source:1
# مثال 1541 — دمج قاموسين بجمع القيم
# apl-source:2
# Merge dictionaries summing values
# apl-source:3
# Demonstrates: قواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1541-merge-dicts-sum.apl
# apl-source:6

# apl-source:7
# ننسخ الأول
# apl-source:8
# ثم نضيف الثاني مع الجمع
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
def ادمج(أ, ب):
  # apl-source:19
  ناتج = {}
  # apl-source:20
  for ك in أ:
    # apl-source:21
    ناتج[ك] = أ[ك]
  # apl-source:22
  for ك in ب:
    # apl-source:23
    ناتج[ك] = ناتج.get(ك, 0) + ب[ك]
  # apl-source:24
  return ناتج
# apl-source:25

# apl-source:26
تأكد_يساوي(ادمج({"x": 1, "y": 2}, {"y": 3, "z": 4}), {"x": 1, "y": 5, "z": 4}, "تقاطع")
# apl-source:27
تأكد_يساوي(ادمج({}, {"a": 1}), {"a": 1}, "الأول فارغ")
# apl-source:28
تأكد_يساوي(ادمج({"a": 1}, {}), {"a": 1}, "الثاني فارغ")
# apl-source:29
