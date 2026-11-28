
# apl-source:1
# مثال 918 — متتابعة ريكامان
# apl-source:2
# Recaman sequence
# apl-source:3
# Demonstrates: تراجع مشروط وتقدم
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/918-recaman.apl
# apl-source:6

# apl-source:7
# متتابعة ريكامان: تراجع n خطوات إن أمكن وإلا تقدم
# apl-source:8
# أ[ن] = أ[ن-1] - ن إن كان موجباً وجديداً، وإلا أ[ن-1] + ن
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
def ريكامان(عدد):
  # apl-source:19
  أ = [0]
  # apl-source:20
  for ن in range(1, عدد):
    # apl-source:21
    مرشح = أ[len(أ) - 1] - ن
    # apl-source:22
    موجود = 0
    # apl-source:23
    for x in أ:
      # apl-source:24
      if x == مرشح:
        # apl-source:25
        موجود = 1
    # apl-source:26
    if مرشح > 0 and موجود == 0:
      # apl-source:27
      أ = أ + [مرشح]
    # apl-source:28
    else:
      # apl-source:29
      أ = أ + [أ[len(أ) - 1] + ن]
  # apl-source:30
  return أ
# apl-source:31

# apl-source:32
أ = ريكامان(15)
# apl-source:33
print("أول 15 حداً:", أ)
# apl-source:34

# apl-source:35
متوقع = [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9]
# apl-source:36
تأكد_يساوي(len(أ), 15, "الطول")
# apl-source:37
for i in range(15):
  # apl-source:38
  تأكد_يساوي(أ[i], متوقع[i], "حد " + str(i))
# apl-source:39

# apl-source:40
# كل حد يبعد عن سابقه بموضعه
# apl-source:41
ب = ريكامان(20)
# apl-source:42
for i in range(1, 20):
  # apl-source:43
  فرق = ب[i] - ب[i - 1]
  # apl-source:44
  if فرق < 0:
    # apl-source:45
    فرق = -فرق
  # apl-source:46
  تأكد_يساوي(فرق, i, "قفزة " + str(i))
# apl-source:47
