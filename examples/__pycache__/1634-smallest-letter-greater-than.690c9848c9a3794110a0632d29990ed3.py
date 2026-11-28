
# apl-source:1
# مثال 1634 — أصغر حرف أكبر من الهدف
# apl-source:2
# Smallest letter greater than target
# apl-source:3
# Demonstrates: بحث ثنائي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1634-smallest-letter-greater-than.apl
# apl-source:6

# apl-source:7
# نبحث عن أول حرف أكبر تماماً
# apl-source:8
# إن لم نجد نعود لأول الحروف
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
def التالي(حروف, هدف):
  # apl-source:19
  ي = 0
  # apl-source:20
  ج = len(حروف)
  # apl-source:21
  while ي < ج:
    # apl-source:22
    م = (ي + ج) // 2
    # apl-source:23
    if حروف[م] <= هدف:
      # apl-source:24
      ي = م + 1
    # apl-source:25
    else:
      # apl-source:26
      ج = م
  # apl-source:27
  if ي == len(حروف):
    # apl-source:28
    return حروف[0]
  # apl-source:29
  return حروف[ي]
# apl-source:30

# apl-source:31
تأكد_يساوي(التالي(["c", "f", "j"], "a"), "c", "قبل الكل")
# apl-source:32
تأكد_يساوي(التالي(["c", "f", "j"], "c"), "f", "المساوي")
# apl-source:33
تأكد_يساوي(التالي(["c", "f", "j"], "j"), "c", "التفاف")
# apl-source:34
