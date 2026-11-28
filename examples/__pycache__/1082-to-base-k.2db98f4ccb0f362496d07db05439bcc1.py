
# apl-source:1
# مثال 1082 — التحويل لأي أساس
# apl-source:2
# Convert integer to base k
# apl-source:3
# Demonstrates: قسمة متكررة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1082-to-base-k.apl
# apl-source:6

# apl-source:7
# نقسم على الأساس ونجمع الباقي من الأخير للأول
# apl-source:8
# ونتعامل مع السالب بعلامة في البداية
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
def لاساس(ن, ك):
  # apl-source:19
  رموز = "0123456789abcdef"
  # apl-source:20
  if ن == 0:
    # apl-source:21
    return "0"
  # apl-source:22
  علامة = ""
  # apl-source:23
  if ن < 0:
    # apl-source:24
    علامة = "-"
    # apl-source:25
    ن = -ن
  # apl-source:26
  ناتج = ""
  # apl-source:27
  while ن > 0:
    # apl-source:28
    ناتج = رموز[ن % ك] + ناتج
    # apl-source:29
    ن = ن // ك
  # apl-source:30
  return علامة + ناتج
# apl-source:31

# apl-source:32
تأكد_يساوي(لاساس(100, 7), "202", "أساس سبعة")
# apl-source:33
تأكد_يساوي(لاساس(255, 16), "ff", "ستة عشري")
# apl-source:34
تأكد_يساوي(لاساس(0, 2), "0", "صفر")
# apl-source:35
تأكد_يساوي(لاساس(-7, 7), "-10", "سالب")
# apl-source:36
