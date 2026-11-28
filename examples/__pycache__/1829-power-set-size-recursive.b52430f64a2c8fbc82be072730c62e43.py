
# apl-source:1
# مثال 1829 — حجم مجموعة القوى
# apl-source:2
# Recursive subset enumeration count
# apl-source:3
# Demonstrates: تكرار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1829-power-set-size-recursive.apl
# apl-source:6

# apl-source:7
# كل عنصر إما داخل أو خارج
# apl-source:8
# العدد يتضاعف مع كل عنصر
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
def عد_المجموعات(ق, ك):
  # apl-source:19
  if ك == len(ق):
    # apl-source:20
    return 1
  # apl-source:21
  return عد_المجموعات(ق, ك + 1) * 2
# apl-source:22

# apl-source:23
تأكد_يساوي(عد_المجموعات([1, 2, 3], 0), 8, "ثلاثة")
# apl-source:24
تأكد_يساوي(عد_المجموعات([], 0), 1, "فارغة")
# apl-source:25
تأكد_يساوي(عد_المجموعات([1, 2, 3, 4, 5], 0), 32, "خمسة")
# apl-source:26
