
# apl-source:1
# مثال 1470 — التفاف الكلمات في أسطر
# apl-source:2
# Greedy word wrap
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1470-greedy-word-wrap.apl
# apl-source:6

# apl-source:7
# نضيف كلمة للسطر الحالي إن كفى العرض
# apl-source:8
# وإلا نبدأ سطراً جديداً
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
def التفاف(كلمات, عرض):
  # apl-source:19
  أسطر = []
  # apl-source:20
  سطر = ""
  # apl-source:21
  for ك in كلمات:
    # apl-source:22
    if سطر == "":
      # apl-source:23
      سطر = ك
    # apl-source:24
    elif len(سطر) + 1 + len(ك) <= عرض:
      # apl-source:25
      سطر = سطر + " " + ك
    # apl-source:26
    else:
      # apl-source:27
      أسطر.append(سطر)
      # apl-source:28
      سطر = ك
  # apl-source:29
  if سطر != "":
    # apl-source:30
    أسطر.append(سطر)
  # apl-source:31
  return أسطر
# apl-source:32

# apl-source:33
تأكد_يساوي(التفاف(["aa", "bb", "cc", "dd"], 5), ["aa bb", "cc dd"], "سطران")
# apl-source:34
تأكد_يساوي(التفاف(["abcdef"], 3), ["abcdef"], "كلمة طويلة")
# apl-source:35
تأكد_يساوي(التفاف([], 5), [], "فارغ")
# apl-source:36
