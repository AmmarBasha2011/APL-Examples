
# apl-source:1
# مثال 1022 — اللص والبيوت الدائرية
# apl-source:2
# House robber on a circle
# apl-source:3
# Demonstrates: حالتان لبيت أول وأخير
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1022-house-robber-circular.apl
# apl-source:6

# apl-source:7
# البيت الأول والأخير متجاوران فلا يؤخذان معاً
# apl-source:8
# نحل مرتين: بدون الأول ثم بدون الأخير ونأخذ الأكبر
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
def خطي(ق):
  # apl-source:19
  أ = 0
  # apl-source:20
  ب = 0
  # apl-source:21
  for س in ق:
    # apl-source:22
    ج = ب
    # apl-source:23
    if (أ + س) > ج:
      # apl-source:24
      ج = أ + س
    # apl-source:25
    أ = ب
    # apl-source:26
    ب = ج
  # apl-source:27
  return ب
# apl-source:28

# apl-source:29
def سرقة_دائرية(ق):
  # apl-source:30
  if len(ق) == 1:
    # apl-source:31
    return ق[0]
  # apl-source:32
  ص1 = خطي(ق[1:])
  # apl-source:33
  ص2 = خطي(ق[:-1])
  # apl-source:34
  if ص1 > ص2:
    # apl-source:35
    return ص1
  # apl-source:36
  return ص2
# apl-source:37

# apl-source:38
تأكد_يساوي(سرقة_دائرية([2, 3, 2]), 3, "ثلاثة بيوت")
# apl-source:39
تأكد_يساوي(سرقة_دائرية([1, 2, 3, 1]), 4, "أربعة بيوت")
# apl-source:40
تأكد_يساوي(سرقة_دائرية([5]), 5, "بيت واحد")
# apl-source:41
تأكد_يساوي(سرقة_دائرية([1, 2, 3]), 3, "الأكبر وحده")
# apl-source:42
