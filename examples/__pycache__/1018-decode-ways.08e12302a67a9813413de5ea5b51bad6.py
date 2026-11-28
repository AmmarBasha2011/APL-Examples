
# apl-source:1
# مثال 1018 — طرق فك الترميز
# apl-source:2
# Decode ways
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1018-decode-ways.apl
# apl-source:6

# apl-source:7
# الرقم من 1 إلى 26 يمثل حرفاً
# apl-source:8
# عدد الطرق لبادئة يعتمد على قراءة خانة واحدة أو خانتين
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
def طرق(س):
  # apl-source:19
  ن = len(س)
  # apl-source:20
  ط = [0] * (ن + 1)
  # apl-source:21
  ط[0] = 1
  # apl-source:22
  if س[0] != "0":
    # apl-source:23
    ط[1] = 1
  # apl-source:24
  for ع in range(2, ن + 1):
    # apl-source:25
    if س[ع - 1] != "0":
      # apl-source:26
      ط[ع] = ط[ع] + ط[ع - 1]
    # apl-source:27
    ثنائي = int(س[ع - 2:ع])
    # apl-source:28
    if (ثنائي >= 10) and (ثنائي <= 26):
      # apl-source:29
      ط[ع] = ط[ع] + ط[ع - 2]
  # apl-source:30
  return ط[ن]
# apl-source:31

# apl-source:32
تأكد_يساوي(طرق("12"), 2, "اثنتان")
# apl-source:33
تأكد_يساوي(طرق("226"), 3, "ثلاث")
# apl-source:34
تأكد_يساوي(طرق("06"), 0, "صفر بادئ")
# apl-source:35
تأكد_يساوي(طرق("10"), 1, "عشرة فقط")
# apl-source:36
