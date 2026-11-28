
# apl-source:1
# مثال 1935 — حشو نص لعمود بعرض ثابت
# apl-source:2
# Pad text to a fixed width column
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1935-pad-right-fixed-width-column.apl
# apl-source:6

# apl-source:7
# إن كان النص أقصر نضيف حشوا
# apl-source:8
# وإلا نتركه كما هو
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
def حشو(س, عرض, ح):
  # apl-source:19
  خرج = س
  # apl-source:20
  while len(خرج) < عرض:
    # apl-source:21
    خرج = خرج + ح
  # apl-source:22
  return خرج
# apl-source:23

# apl-source:24
def صف(أ, ب):
  # apl-source:25
  return حشو(أ, 6, ".") + "|" + ب
# apl-source:26

# apl-source:27
تأكد_يساوي(حشو("ab", 5, "."), "ab...", "حشو")
# apl-source:28
تأكد_يساوي(حشو("abcdef", 3, "."), "abcdef", "أطول")
# apl-source:29
تأكد_يساوي(صف("id", "7"), "id....|7", "صف")
# apl-source:30
