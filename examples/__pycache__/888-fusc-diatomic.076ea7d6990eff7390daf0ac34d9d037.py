
# apl-source:1
# مثال 888 — دالة فوسك الثنائية الذرية
# apl-source:2
# fusc diatomic sequence
# apl-source:3
# Demonstrates: استدعاء بشروط زوجية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/888-fusc-diatomic.apl
# apl-source:6

# apl-source:7
# متتابعة فوسك (ثنائية الذرات لستيرن): f(2n)=f(n) و f(2n+1)=f(n)+f(n+1)
# apl-source:8
# f(n)/f(n+1) يعد كل الكسور الموجبة المختزلة بالضبط مرة
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
def فوسك(ن):
  # apl-source:19
  ف = [0, 1]
  # apl-source:20
  for i in range(2, ن + 1):
    # apl-source:21
    if i % 2 == 0:
      # apl-source:22
      ف = ف + [ف[i // 2]]
    # apl-source:23
    else:
      # apl-source:24
      ف = ف + [ف[(i - 1) // 2] + ف[(i + 1) // 2]]
  # apl-source:25
  return ف
# apl-source:26

# apl-source:27
ف = فوسك(16)
# apl-source:28
print("fusc(0..16):", ف)
# apl-source:29

# apl-source:30
تأكد_يساوي(ف[0], 0, "fusc(0) = 0")
# apl-source:31
تأكد_يساوي(ف[1], 1, "fusc(1) = 1")
# apl-source:32
تأكد_يساوي(ف[5], 3, "fusc(5) = 3")
# apl-source:33
تأكد_يساوي(ف[9], 4, "fusc(9) = 4")
# apl-source:34
تأكد_يساوي(ف[11], 5, "fusc(11) = 5")
# apl-source:35
تأكد_يساوي(ف[16], 1, "fusc(16) = fusc(8) = 1")
# apl-source:36

# apl-source:37
# الكسور f(n)/f(n+1) متمايزة لأول 16 نسبة
# apl-source:38
نسب = []
# apl-source:39
for i in range(1, 16):
  # apl-source:40
  نسب = نسب + [[ف[i], ف[i + 1]]]
# apl-source:41
متميزة = 0
# apl-source:42
for i in range(len(نسب)):
  # apl-source:43
  جديدة = 1 == 1
  # apl-source:44
  for ج in range(i):
    # apl-source:45
    if (نسب[ج][0] == نسب[i][0]) and (نسب[ج][1] == نسب[i][1]):
      # apl-source:46
      جديدة = False
  # apl-source:47
  if جديدة:
    # apl-source:48
    متميزة = متميزة + 1
# apl-source:49
تأكد_يساوي(متميزة, 15, "كل النسب متميزة")
# apl-source:50
