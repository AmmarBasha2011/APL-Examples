
# apl-source:1
# مثال 997 — صنبور أرقام ط
# apl-source:2
# Pi spigot algorithm
# apl-source:3
# Demonstrates: بقايا تنتج رقماً رقماً
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/997-pi-spigot.apl
# apl-source:6

# apl-source:7
# صنبور باي: أرقام ط تنتج واحداً واحداً دون كسور عائمة طويلة
# apl-source:8
# خوارزمية رابينوفيتز-واغون بمصفوفة بقايا
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
ن = 11
# apl-source:19
صناديق = ((ن * 10) // 3) + 1
# apl-source:20
بقايا = []
# apl-source:21
for _ in range(صناديق):
  # apl-source:22
  بقايا = بقايا + [2]
# apl-source:23
أرقام = []
# apl-source:24
محتجز = 0
# apl-source:25
سابق = 0
# apl-source:26
for _ in range(ن):
  # apl-source:27
  حمل = 0
  # apl-source:28
  for j in range(صناديق, 0, -1):
    # apl-source:29
    س = (بقايا[j - 1] * 10) + (حمل * j)
    # apl-source:30
    بقايا[j - 1] = س % ((2 * j) - 1)
    # apl-source:31
    حمل = س // ((2 * j) - 1)
  # apl-source:32
  بقايا[0] = حمل % 10
  # apl-source:33
  رقم = حمل // 10
  # apl-source:34
  if رقم == 9:
    # apl-source:35
    محتجز = محتجز + 1
  # apl-source:36
  elif رقم == 10:
    # apl-source:37
    أرقام = أرقام + [سابق + 1]
    # apl-source:38
    for __ in range(محتجز):
      # apl-source:39
      أرقام = أرقام + [0]
    # apl-source:40
    سابق = 0
    # apl-source:41
    محتجز = 0
  # apl-source:42
  else:
    # apl-source:43
    أرقام = أرقام + [سابق]
    # apl-source:44
    سابق = رقم
    # apl-source:45
    for __ in range(محتجز):
      # apl-source:46
      أرقام = أرقام + [9]
    # apl-source:47
    محتجز = 0
# apl-source:48
أرقام = أرقام + [سابق]
# apl-source:49

# apl-source:50
تأكد_يساوي(أرقام[1], 3, "الرقم الصحيح")
# apl-source:51
تأكد_يساوي(أرقام[2], 1, "أول عشري")
# apl-source:52
تأكد_يساوي(أرقام[3], 4, "ثاني عشري")
# apl-source:53
تأكد_يساوي(أرقام[5], 5, "رابع عشري")
# apl-source:54
تأكد_يساوي(أرقام[11], 5, "عاشر عشري")
# apl-source:55
تأكد_يساوي(len(أرقام), 12, "عدد الأرقام")
# apl-source:56
