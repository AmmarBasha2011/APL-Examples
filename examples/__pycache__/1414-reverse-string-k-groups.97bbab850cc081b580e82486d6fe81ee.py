
# apl-source:1
# مثال 1414 — عكس نص بمجموعات
# apl-source:2
# Reverse first k of every 2k
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1414-reverse-string-k-groups.apl
# apl-source:6

# apl-source:7
# نقسم النص إلى كتل بطول 2ك
# apl-source:8
# نعكس أول ك في كل كتلة
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
def اعكس_جزء(ج):
  # apl-source:19
  ناتج = ""
  # apl-source:20
  for ح in ج:
    # apl-source:21
    ناتج = ح + ناتج
  # apl-source:22
  return ناتج
# apl-source:23

# apl-source:24
def اعكس_ك(نص_, ك):
  # apl-source:25
  ناتج = ""
  # apl-source:26
  ع = 0
  # apl-source:27
  while ع < len(نص_):
    # apl-source:28
    ناتج = ناتج + اعكس_جزء(نص_[ع:ع + ك]) + نص_[ع + ك:ع + 2 * ك]
    # apl-source:29
    ع = ع + 2 * ك
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(اعكس_ك("abcdefg", 2), "bacdfeg", "سبعة حروف")
# apl-source:33
تأكد_يساوي(اعكس_ك("abcd", 2), "bacd", "أربعة")
# apl-source:34
تأكد_يساوي(اعكس_ك("abc", 5), "cba", "ك كبيرة")
# apl-source:35
