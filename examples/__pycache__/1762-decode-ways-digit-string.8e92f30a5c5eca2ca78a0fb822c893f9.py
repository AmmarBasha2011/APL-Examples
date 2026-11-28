
# apl-source:1
# مثال 1762 — طرق فك ترميز الأرقام
# apl-source:2
# Decode ways of digit string
# apl-source:3
# Demonstrates: برمجة ديناميكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1762-decode-ways-digit-string.apl
# apl-source:6

# apl-source:7
# رقم واحد أو رقمان
# apl-source:8
# الصفر وحده لا يصح
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
def طرق_الفك(س):
  # apl-source:19
  if len(س) == 0 or س[0] == "0":
    # apl-source:20
    return 0
  # apl-source:21
  أ = 1
  # apl-source:22
  ب = 1
  # apl-source:23
  for ك in range(1, len(س)):
    # apl-source:24
    ج = 0
    # apl-source:25
    if س[ك] != "0":
      # apl-source:26
      ج = ب
    # apl-source:27
    اثنان = int(س[ك - 1:ك + 1])
    # apl-source:28
    if اثنان >= 10 and اثنان <= 26:
      # apl-source:29
      ج = ج + أ
    # apl-source:30
    أ = ب
    # apl-source:31
    ب = ج
  # apl-source:32
  return ب
# apl-source:33

# apl-source:34
تأكد_يساوي(طرق_الفك("12"), 2, "اثنان")
# apl-source:35
تأكد_يساوي(طرق_الفك("226"), 3, "ثلاث")
# apl-source:36
تأكد_يساوي(طرق_الفك("06"), 0, "صفر")
# apl-source:37
تأكد_يساوي(طرق_الفك("10"), 1, "عشرة")
# apl-source:38
