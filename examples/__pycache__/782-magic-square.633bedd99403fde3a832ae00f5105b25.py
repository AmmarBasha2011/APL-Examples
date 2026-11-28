
# apl-source:1
# مثال 782 — المربع السحري
# apl-source:2
# Magic square
# apl-source:3
# Demonstrates: الطريقة السيامية، ثابت سحري
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/782-magic-square.apl
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
# المربع السحري للرتب الفردية بالطريقة السيامية
# apl-source:25
# Demonstrates: صعود قطري ملتف, نزول عند الاصطدام, ثابت سحري n(n^2+1)/2
# apl-source:26

# apl-source:27
def مربع_سحري(ن):
  # apl-source:28
  م = []
  # apl-source:29
  for ي in range(ن):
    # apl-source:30
    صف = []
    # apl-source:31
    for ج in range(ن):
      # apl-source:32
      صف.append(0)
    # apl-source:33
    م.append(صف)
  # apl-source:34
  ص = 0
  # apl-source:35
  ع = ن // 2
  # apl-source:36
  for رقم in range(1, ن * ن + 1):
    # apl-source:37
    صف = م[ص]
    # apl-source:38
    صف[ع] = رقم
    # apl-source:39
    ص_ج = (ص - 1) % ن
    # apl-source:40
    ع_ج = (ع + 1) % ن
    # apl-source:41
    if م[ص_ج][ع_ج] != 0:
      # apl-source:42
      ص = (ص + 1) % ن
    # apl-source:43
    else:
      # apl-source:44
      ص = ص_ج
      # apl-source:45
      ع = ع_ج
  # apl-source:46
  return م
# apl-source:47

# apl-source:48
م3 = مربع_سحري(3)
# apl-source:49
تأكد_يساوي(م3[0][0], 8, "م3 خلية 1")
# apl-source:50
تأكد_يساوي(م3[0][1], 1, "م3 خلية 2")
# apl-source:51
تأكد_يساوي(م3[0][2], 6, "م3 خلية 3")
# apl-source:52
تأكد_يساوي(م3[1][0], 3, "م3 خلية 4")
# apl-source:53
تأكد_يساوي(م3[1][1], 5, "م3 خلية 5")
# apl-source:54
تأكد_يساوي(م3[2][2], 2, "م3 خلية 6")
# apl-source:55
تأكد_يساوي(م3[0][0] + م3[1][1] + م3[2][2], 15, "م3 قطر")
# apl-source:56
م5 = مربع_سحري(5)
# apl-source:57
تأكد_يساوي(م5[0][0], 17, "م5 خلية 1")
# apl-source:58
تأكد_يساوي(م5[0][1], 24, "م5 خلية 2")
# apl-source:59
تأكد_يساوي(م5[0][4], 15, "م5 خلية 3")
# apl-source:60
مج = 0
# apl-source:61
for ج in range(5):
  # apl-source:62
  مج = مج + م5[2][ج]
# apl-source:63
تأكد_يساوي(مج, 65, "م5 مجموع صف")
# apl-source:64
قطر = 0
# apl-source:65
for ي in range(5):
  # apl-source:66
  قطر = قطر + م5[ي][ي]
# apl-source:67
تأكد_يساوي(قطر, 65, "م5 قطر")
# apl-source:68
عمود = 0
# apl-source:69
for ي in range(5):
  # apl-source:70
  عمود = عمود + م5[ي][4]
# apl-source:71
تأكد_يساوي(عمود, 65, "م5 عمود")
# apl-source:72
