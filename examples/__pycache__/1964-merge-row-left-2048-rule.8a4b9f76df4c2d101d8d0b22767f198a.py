
# apl-source:1
# مثال 1964 — دمج صف في لعبة 2048
# apl-source:2
# 2048 row merge left
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1964-merge-row-left-2048-rule.apl
# apl-source:6

# apl-source:7
# # نحذف الأصفار ثم ندمج الأزواج المتساوية
# apl-source:8
# # ونملأ الباقي بأصفار
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
def ادمج(صف):
  # apl-source:19
  ق = []
  # apl-source:20
  for ع in صف:
    # apl-source:21
    if ع != 0:
      # apl-source:22
      ق = ق + [ع]
  # apl-source:23
  خرج = []
  # apl-source:24
  ك = 0
  # apl-source:25
  while ك < len(ق):
    # apl-source:26
    if ك + 1 < len(ق) and ق[ك] == ق[ك + 1]:
      # apl-source:27
      خرج = خرج + [ق[ك] * 2]
      # apl-source:28
      ك = ك + 2
    # apl-source:29
    else:
      # apl-source:30
      خرج = خرج + [ق[ك]]
      # apl-source:31
      ك = ك + 1
  # apl-source:32
  while len(خرج) < len(صف):
    # apl-source:33
    خرج = خرج + [0]
  # apl-source:34
  return خرج
# apl-source:35

# apl-source:36
تأكد_يساوي(ادمج([2, 2, 2, 2]), [4, 4, 0, 0], "أربعة متساوية")
# apl-source:37
تأكد_يساوي(ادمج([2, 0, 2, 4]), [4, 4, 0, 0], "مع صفر")
# apl-source:38
تأكد_يساوي(ادمج([4, 2, 2, 0]), [4, 4, 0, 0], "وسط")
# apl-source:39
تأكد_يساوي(ادمج([2, 4, 8, 16]), [2, 4, 8, 16], "لا دمج")
# apl-source:40
