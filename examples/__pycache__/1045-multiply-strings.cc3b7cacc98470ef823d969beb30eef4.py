
# apl-source:1
# مثال 1045 — ضرب أعداد نصية
# apl-source:2
# Multiply strings
# apl-source:3
# Demonstrates: ضرب خانة بخانة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1045-multiply-strings.apl
# apl-source:6

# apl-source:7
# نضرب كل خانتين ونضيف الناتج في موضعه
# apl-source:8
# ثم نمرر الحمل من اليمين لليسار
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
def اضرب_نص(أ, ب):
  # apl-source:19
  if (أ == "0") or (ب == "0"):
    # apl-source:20
    return "0"
  # apl-source:21
  خانات = [0] * (len(أ) + len(ب))
  # apl-source:22
  for ي in range(len(أ) - 1, -1, -1):
    # apl-source:23
    for ك in range(len(ب) - 1, -1, -1):
      # apl-source:24
      ج = ي + ك + 1
      # apl-source:25
      مج = (int(أ[ي]) * int(ب[ك])) + خانات[ج]
      # apl-source:26
      خانات[ج] = مج % 10
      # apl-source:27
      خانات[ج - 1] = خانات[ج - 1] + (مج // 10)
  # apl-source:28
  ناتج = ""
  # apl-source:29
  for خ in خانات:
    # apl-source:30
    ناتج = ناتج + str(خ)
  # apl-source:31
  return ناتج.lstrip("0")
# apl-source:32

# apl-source:33
تأكد_يساوي(اضرب_نص("2", "3"), "6", "بسيط")
# apl-source:34
تأكد_يساوي(اضرب_نص("123", "456"), "56088", "ثلاث خانات")
# apl-source:35
تأكد_يساوي(اضرب_نص("999", "999"), "998001", "حمل كثير")
# apl-source:36
تأكد_يساوي(اضرب_نص("0", "12345"), "0", "صفر")
# apl-source:37
