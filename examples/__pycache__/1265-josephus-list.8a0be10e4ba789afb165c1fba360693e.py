
# apl-source:1
# مثال 1265 — يوسيفوس بقائمة
# apl-source:2
# Josephus elimination order
# apl-source:3
# Demonstrates: محاكاة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1265-josephus-list.apl
# apl-source:6

# apl-source:7
# نعد k خطوات في دائرة
# apl-source:8
# ونقصي من يقع عليه العد
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
def اقصاء(ن, ك):
  # apl-source:19
  دائرة = list(range(1, ن + 1))
  # apl-source:20
  ترتيب = []
  # apl-source:21
  موقع = 0
  # apl-source:22
  while len(دائرة) > 0:
    # apl-source:23
    موقع = (موقع + ك - 1) % len(دائرة)
    # apl-source:24
    ترتيب = ترتيب + [دائرة.pop(موقع)]
  # apl-source:25
  return ترتيب
# apl-source:26

# apl-source:27
تأكد_يساوي(اقصاء(7, 3), [3, 6, 2, 7, 5, 1, 4], "سبعة وثلاثة")
# apl-source:28
تأكد_يساوي(اقصاء(5, 2), [2, 4, 1, 5, 3], "خمسة واثنان")
# apl-source:29
تأكد_يساوي(اقصاء(1, 5), [1], "واحد")
# apl-source:30
