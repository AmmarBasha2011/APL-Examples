
# apl-source:1
# مثال 2061 — دمج قائمتين مرتبتين بلا تكرار
# apl-source:2
# Merge sorted lists dedupe
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2061-merge-sorted-lists-drop-duplicates.apl
# apl-source:6

# apl-source:7
# # مؤشر على كل قائمة
# apl-source:8
# # لا نضيف قيمة تساوي آخر ما أضفناه
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
def ادمج(ا, ب):
  # apl-source:19
  ي = 0
  # apl-source:20
  ل = 0
  # apl-source:21
  خرج = []
  # apl-source:22
  while ي < len(ا) or ل < len(ب):
    # apl-source:23
    if ل >= len(ب) or (ي < len(ا) and ا[ي] <= ب[ل]):
      # apl-source:24
      ق = ا[ي]
      # apl-source:25
      ي = ي + 1
    # apl-source:26
    else:
      # apl-source:27
      ق = ب[ل]
      # apl-source:28
      ل = ل + 1
    # apl-source:29
    if len(خرج) == 0 or خرج[len(خرج) - 1] != ق:
      # apl-source:30
      خرج = خرج + [ق]
  # apl-source:31
  return خرج
# apl-source:32

# apl-source:33
تأكد_يساوي(ادمج([1, 3, 5, 5], [2, 3, 6]), [1, 2, 3, 5, 6], "كلاسيكي")
# apl-source:34
تأكد_يساوي(ادمج([], [1, 1]), [1], "فارغة")
# apl-source:35
تأكد_يساوي(ادمج([], []), [], "كلتاهما فارغة")
# apl-source:36
