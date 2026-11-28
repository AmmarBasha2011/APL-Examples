
# apl-source:1
# مثال 825 — متتالية هالتون
# apl-source:2
# Halton sequence
# apl-source:3
# Demonstrates: انعكاس جذري، أساسات أولية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/825-quasi-random-halton.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# متتالية هالتون شبه العشوائية: قلب الجذر بأساسات أولية لتغطية متجانسة
# apl-source:25
# Demonstrates: انعكاس جذري, أساسان مستقلان, تباين منخفض للتكامل العددي
# apl-source:26

# apl-source:27
def هالتون(فهرس, أساس):
  # apl-source:28
  ك = 1.0
  # apl-source:29
  نتيجة = 0.0
  # apl-source:30
  ن = فهرس
  # apl-source:31
  while ن > 0:
    # apl-source:32
    ك = ك / أساس
    # apl-source:33
    نتيجة = نتيجة + ك * (ن % أساس)
    # apl-source:34
    ن = ن // أساس
  # apl-source:35
  return نتيجة
# apl-source:36

# apl-source:37
تأكد_يساوي(round(هالتون(1, 2), 4), 0.5, "أولى أساس 2")
# apl-source:38
تأكد_يساوي(round(هالتون(2, 2), 4), 0.25, "ثانية أساس 2")
# apl-source:39
تأكد_يساوي(round(هالتون(3, 2), 4), 0.75, "ثالثة أساس 2")
# apl-source:40
تأكد_يساوي(round(هالتون(4, 2), 4), 0.125, "رابعة أساس 2")
# apl-source:41
تأكد_يساوي(round(هالتون(5, 2), 4), 0.625, "خامسة أساس 2")
# apl-source:42
تأكد_يساوي(round(هالتون(3, 3), 4), 0.1111, "أساس 3")
# apl-source:43
تأكد_يساوي(round(هالتون(10, 2), 4), 0.3125, "عاشرة أساس 2")
# apl-source:44
تأكد_يساوي(round(هالتون(7, 5), 4), 0.44, "أساس 5")
# apl-source:45
نقطة = [round(هالتون(6, 2), 4), round(هالتون(6, 3), 4)]
# apl-source:46
تأكد_يساوي(نقطة, [0.375, 0.2222], "نقطة ثنائية الأبعاد")
# apl-source:47
