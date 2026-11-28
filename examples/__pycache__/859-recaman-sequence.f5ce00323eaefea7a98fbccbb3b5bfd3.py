
# apl-source:1
# مثال 859 — متتابعة ريكامان
# apl-source:2
# Recaman sequence
# apl-source:3
# Demonstrates: تراجع إن أمكن وإلا تقدم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/859-recaman-sequence.apl
# apl-source:6

# apl-source:7
# متتابعة ريكامان: تراجع خطوة ن للخلف إن أمكن وإلا تقدم
# apl-source:8
# أ₀=0 وأₙ = أₙ₋₁ - ن إن كان موجباً وجديداً، وإلا أₙ₋₁ + ن
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
def موجود(قائمة, قيمة):
  # apl-source:19
  for عنصر in قائمة:
    # apl-source:20
    if عنصر == قيمة:
      # apl-source:21
      return 1 == 1
  # apl-source:22
  return False
# apl-source:23

# apl-source:24
def ريكامان(عدد_الحدود):
  # apl-source:25
  ت = [0]
  # apl-source:26
  for ن in range(1, عدد_الحدود):
    # apl-source:27
    مرشح = ت[len(ت) - 1] - ن
    # apl-source:28
    if مرشح > 0 and not موجود(ت, مرشح):
      # apl-source:29
      ت = ت + [مرشح]
    # apl-source:30
    else:
      # apl-source:31
      ت = ت + [ت[len(ت) - 1] + ن]
  # apl-source:32
  return ت
# apl-source:33

# apl-source:34
ت = ريكامان(21)
# apl-source:35
print("أول 21 حداً:", ت)
# apl-source:36

# apl-source:37
تأكد_يساوي(len(ت), 21, "21 حداً")
# apl-source:38
تأكد_يساوي(ت[1], 1, "أ₁ = 1")
# apl-source:39
تأكد_يساوي(ت[4], 2, "أ₄ = 2 (أول تراجع)")
# apl-source:40
تأكد_يساوي(ت[10], 11, "أ₁₀ = 11")
# apl-source:41
تأكد_يساوي(ت[18], 43, "أ₁₈ = 43")
# apl-source:42
تأكد_يساوي(ت[19], 62, "أ₁₉ = 62")
# apl-source:43
تأكد_يساوي(ت[20], 42, "أ₂₀ = 42")
# apl-source:44
