
# apl-source:1
# مثال 1756 — هل تتقطع الجملة إلى كلمات
# apl-source:2
# Word break possible
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1756-word-break-possible.apl
# apl-source:6

# apl-source:7
# جدول للمواضع الممكنة
# apl-source:8
# نختبر كل كلمة عند كل موضع
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
def تتقطع(س, كلمات):
  # apl-source:19
  ن = len(س)
  # apl-source:20
  ممكن = [True]
  # apl-source:21
  for ك in range(ن):
    # apl-source:22
    ممكن.append(False)
  # apl-source:23
  for ي in range(1, ن + 1):
    # apl-source:24
    for ك in كلمات:
      # apl-source:25
      ط = len(ك)
      # apl-source:26
      if ط <= ي:
        # apl-source:27
        if ممكن[ي - ط] and س[ي - ط:ي] == ك:
          # apl-source:28
          ممكن[ي] = True
  # apl-source:29
  return ممكن[ن]
# apl-source:30

# apl-source:31
تأكد_يساوي(تتقطع("applepen", ["apple", "pen"]), True, "تقطيع")
# apl-source:32
تأكد_يساوي(تتقطع("catsand", ["cats", "dog"]), False, "لا")
# apl-source:33
تأكد_يساوي(تتقطع("", ["a"]), True, "فارغ")
# apl-source:34
