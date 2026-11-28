
# apl-source:1
# مثال 844 — الأولية التوأم
# apl-source:2
# Twin primes
# apl-source:3
# Demonstrates: أزواج بفرق اثنين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/844-twin-primes.apl
# apl-source:6

# apl-source:7
# الأولية التوأم: أزواج (ف، ف+2) كلاهما أولي
# apl-source:8
# حدسية الأولية التوأم: لا نهائية (غير مثبتة حتى اليوم)
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
def أولي(ن):
  # apl-source:19
  if ن < 2:
    # apl-source:20
    return False
  # apl-source:21
  if ن < 4:
    # apl-source:22
    return 1 == 1
  # apl-source:23
  if ن % 2 == 0:
    # apl-source:24
    return False
  # apl-source:25
  قاسم = 3
  # apl-source:26
  while قاسم * قاسم <= ن:
    # apl-source:27
    if ن % قاسم == 0:
      # apl-source:28
      return False
    # apl-source:29
    قاسم = قاسم + 2
  # apl-source:30
  return 1 == 1
# apl-source:31

# apl-source:32
توائم = []
# apl-source:33
for ف in range(3, 100):
  # apl-source:34
  if أولي(ف) and أولي(ف + 2):
    # apl-source:35
    توائم = توائم + [[ف, ف + 2]]
# apl-source:36

# apl-source:37
print("التوائم تحت 100:", توائم)
# apl-source:38

# apl-source:39
تأكد_يساوي(len(توائم), 8, "ثمانية توائم تحت 100")
# apl-source:40
تأكد_يساوي(توائم[0][0], 3, "أول توأم يبدأ بـ 3")
# apl-source:41
تأكد_يساوي(توائم[1][0], 5, "ثاني توأم يبدأ بـ 5")
# apl-source:42
تأكد_يساوي(توائم[7][1], 73, "آخر توأم ينتهي بـ 73")
# apl-source:43

# apl-source:44
# كل توأم بعد (3,5) مجموعه من مضاعفات 12
# apl-source:45
for زوج in توائم:
  # apl-source:46
  if زوج[0] > 3:
    # apl-source:47
    تأكد_يساوي((زوج[0] + زوج[1]) % 12, 0, "مجموع التوأم من مضاعفات 12")
# apl-source:48
