
# apl-source:1
# مثال 2958 — أكبر مجموع لنافذة بحجم 4
# apl-source:2
# Max window sum size 4
# apl-source:3
# Demonstrates: قوائم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2958-max-sum-of-window-size-4.apl
# apl-source:6

# apl-source:7
# # ندخل القيم
# apl-source:8
# # ونقارن النتيجة
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
def ف(ق):
  # apl-source:19
  ك = sum(ق[:4])
  # apl-source:20
  for ي in range(len(ق) - 4 + 1):
    # apl-source:21
    م = sum(ق[ي:ي + 4])
    # apl-source:22
    if م > ك:
      # apl-source:23
      ك = م
  # apl-source:24
  return ك
# apl-source:25

# apl-source:26
تأكد_يساوي(ف([1, 2, 3, 4, 5, 6]), 18, "حالة 1")
# apl-source:27
تأكد_يساوي(ف([5, 1, 5, 1, 5, 1, 9]), 16, "حالة 2")
# apl-source:28
تأكد_يساوي(ف([3, 3, 3, 3]), 12, "حالة 3")
# apl-source:29
تأكد_يساوي(ف([-1, 2, -3, 4, 5, 6]), 12, "حالة 4")
# apl-source:30
