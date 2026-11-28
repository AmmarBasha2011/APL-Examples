
# apl-source:1
# مثال 2148 — التبديلة رقم ن بالمضروب
# apl-source:2
# Nth permutation factoradic
# apl-source:3
# Demonstrates: توافيق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2148-nth-permutation-of-string-factoradic.apl
# apl-source:6

# apl-source:7
# # نحذف الحرف المختار
# apl-source:8
# # ونكمل بالباقي
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
def تبديلة(س, ن):
  # apl-source:19
  باقي = sorted(س)
  # apl-source:20
  مض = 1
  # apl-source:21
  for ك in range(2, len(س)):
    # apl-source:22
    مض = مض * ك
  # apl-source:23
  خرج = ""
  # apl-source:24
  for ك in range(len(س)):
    # apl-source:25
    ف = ن // مض
    # apl-source:26
    خرج = خرج + باقي[ف]
    # apl-source:27
    باقي.pop(ف)
    # apl-source:28
    ن = ن % مض
    # apl-source:29
    if len(س) - 1 - ك > 0:
      # apl-source:30
      مض = مض // (len(س) - 1 - ك)
  # apl-source:31
  return خرج
# apl-source:32

# apl-source:33
تأكد_يساوي(تبديلة("abc", 3), "bca", "الرابعة")
# apl-source:34
تأكد_يساوي(تبديلة("abc", 5), "cba", "الأخيرة")
# apl-source:35
تأكد_يساوي(تبديلة("abcd", 0), "abcd", "الأولى")
# apl-source:36
تأكد_يساوي(تبديلة("abcd", 23), "dcba", "آخر أربعة")
# apl-source:37
