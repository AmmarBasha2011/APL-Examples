
# apl-source:1
# مثال 2062 — العنصر الأكبر رقم ك بالاختيار السريع
# apl-source:2
# Kth largest quickselect
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2062-kth-largest-quickselect-partition.apl
# apl-source:6

# apl-source:7
# # ثلاث قوائم أكبر ومساو وأصغر
# apl-source:8
# # نختار الجزء الذي يحوي الترتيب المطلوب
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
def كاي(ق, ك):
  # apl-source:19
  محور = ق[0]
  # apl-source:20
  اكبر_ق = []
  # apl-source:21
  مساو = []
  # apl-source:22
  اصغر_ق = []
  # apl-source:23
  for ع in ق:
    # apl-source:24
    if ع > محور:
      # apl-source:25
      اكبر_ق = اكبر_ق + [ع]
    # apl-source:26
    elif ع == محور:
      # apl-source:27
      مساو = مساو + [ع]
    # apl-source:28
    else:
      # apl-source:29
      اصغر_ق = اصغر_ق + [ع]
  # apl-source:30
  if ك <= len(اكبر_ق):
    # apl-source:31
    return كاي(اكبر_ق, ك)
  # apl-source:32
  if ك <= len(اكبر_ق) + len(مساو):
    # apl-source:33
    return محور
  # apl-source:34
  return كاي(اصغر_ق, ك - len(اكبر_ق) - len(مساو))
# apl-source:35

# apl-source:36
تأكد_يساوي(كاي([3, 2, 1, 5, 6, 4], 2), 5, "الثاني")
# apl-source:37
تأكد_يساوي(كاي([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4, "الرابع")
# apl-source:38
تأكد_يساوي(كاي([7], 1), 7, "واحد")
# apl-source:39
