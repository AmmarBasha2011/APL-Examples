
# apl-source:1
# مثال 1423 — الأساس سبعة
# apl-source:2
# Convert integer to base 7
# apl-source:3
# Demonstrates: نصوص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1423-base-seven.apl
# apl-source:6

# apl-source:7
# نقسم على سبعة ونجمع الباقي
# apl-source:8
# ونتعامل مع الإشارة منفصلة
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
def الى_سبعة(ن):
  # apl-source:19
  if ن == 0:
    # apl-source:20
    return "0"
  # apl-source:21
  سالب = ن < 0
  # apl-source:22
  if سالب:
    # apl-source:23
    ن = -ن
  # apl-source:24
  ناتج = ""
  # apl-source:25
  while ن > 0:
    # apl-source:26
    ناتج = str(ن % 7) + ناتج
    # apl-source:27
    ن = ن // 7
  # apl-source:28
  if سالب:
    # apl-source:29
    ناتج = "-" + ناتج
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(الى_سبعة(100), "202", "مئة")
# apl-source:33
تأكد_يساوي(الى_سبعة(-7), "-10", "سالب")
# apl-source:34
تأكد_يساوي(الى_سبعة(0), "0", "صفر")
# apl-source:35
