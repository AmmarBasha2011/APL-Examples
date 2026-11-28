
# apl-source:1
# مثال 790 — بلوم-بلوم-شوب
# apl-source:2
# Blum Blum Shub
# apl-source:3
# Demonstrates: تربيع modulo n، بت أدنى
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/790-blum-blum-shub.apl
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
# مولد بلوم-بلوم-شوب: تربيع متكرر modulo حاصل ضرب أوليين
# apl-source:25
# Demonstrates: أمن التشفير من صعوبة التحليل, استخراج البت الأدنى, تجميع بايت
# apl-source:26

# apl-source:27
م = 209
# apl-source:28
تأكد_يساوي(م, 209, "حاصل الضرب")
# apl-source:29

# apl-source:30
def بي_بي_اس_بتات(بذرة, عدد):
  # apl-source:31
  س = بذرة % 209
  # apl-source:32
  بتات = []
  # apl-source:33
  for ي in range(عدد):
    # apl-source:34
    س = (س * س) % 209
    # apl-source:35
    بتات.append(س % 2)
  # apl-source:36
  return بتات
# apl-source:37

# apl-source:38
تأكد_يساوي(بي_بي_اس_بتات(3, 8), [1, 1, 0, 0, 0, 0, 0, 1], "ثمانية بتات")
# apl-source:39
تأكد_يساوي(بي_بي_اس_بتات(3, 16), [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0], "ستة عشر بتاً")
# apl-source:40
بتات8 = بي_بي_اس_بتات(3, 8)
# apl-source:41
بايت = 0
# apl-source:42
for ب in بتات8:
  # apl-source:43
  بايت = بايت * 2 + ب
# apl-source:44
تأكد_يساوي(بايت, 193, "تجميع بايت من البتات")
# apl-source:45
تأكد_يساوي(بي_بي_اس_بتات(7, 6), [1, 0, 1, 0, 1, 0], "بذرة أخرى")
# apl-source:46
