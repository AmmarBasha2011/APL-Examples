
# apl-source:1
# مثال 950 — توليد المتاهات
# apl-source:2
# Maze generation
# apl-source:3
# Demonstrates: تراجع عودي مع خلط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/950-maze-generation.apl
# apl-source:6

# apl-source:7
# توليد متاهة بالتراجع العودي: نحت الممرات من شبكة جدران
# apl-source:8
# كل خلية تُزار مرة واحدة: متاهة مثالية بمسار وحيد
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
# شبكة 5x5 خلايا: الجدران قائمة أزواج (خليتان متجاورتان لا ممر بينهما)
# apl-source:19
# نمثل الممرات بمصفوفة جوار ثنائية
# apl-source:20
صفوف = 5
# apl-source:21
أعمدة = 5
# apl-source:22

# apl-source:23
def فهرس(صف, عمود):
  # apl-source:24
  return صف * 5 + عمود
# apl-source:25

# apl-source:26
# مولد عشوائي حتمي (LCG) لاختيار الترتيب
# apl-source:27
بذرة = [12345]
# apl-source:28
def عشوائي(حد):
  # apl-source:29
  بذرة[0] = (بذرة[0] * 1103515245 + 12345) % 2147483648
  # apl-source:30
  return بذرة[0] % حد
# apl-source:31

# apl-source:32
جوار = []
# apl-source:33
for _ in range(25):
  # apl-source:34
  صف = []
  # apl-source:35
  for __ in range(25):
    # apl-source:36
    صف = صف + [0]
  # apl-source:37
  جوار = جوار + [صف]
# apl-source:38

# apl-source:39
مزار = []
# apl-source:40
for _ in range(25):
  # apl-source:41
  مزار = مزار + [0]
# apl-source:42

# apl-source:43
def احفر(خلية):
  # apl-source:44
  مزار[خلية] = 1
  # apl-source:45
  صف = خلية // 5
  # apl-source:46
  عمود = خلية % 5
  # apl-source:47
  # جيران: أعلى، يمين، أسفل، يسار بترتيب عشوائي حتمي
  # apl-source:48
  اتجاهات = [0, 1, 2, 3]
  # apl-source:49
  # خلط فيشر-ييتس بالبذرة الحتمية
  # apl-source:50
  for i in range(3, 0, -1):
    # apl-source:51
    ج = عشوائي(i + 1)
    # apl-source:52
    مؤقت = اتجاهات[i]
    # apl-source:53
    اتجاهات[i] = اتجاهات[ج]
    # apl-source:54
    اتجاهات[ج] = مؤقت
  # apl-source:55
  for اتجاه in اتجاهات:
    # apl-source:56
    صف2 = صف
    # apl-source:57
    عمود2 = عمود
    # apl-source:58
    if اتجاه == 0:
      # apl-source:59
      صف2 = صف - 1
    # apl-source:60
    if اتجاه == 1:
      # apl-source:61
      عمود2 = عمود + 1
    # apl-source:62
    if اتجاه == 2:
      # apl-source:63
      صف2 = صف + 1
    # apl-source:64
    if اتجاه == 3:
      # apl-source:65
      عمود2 = عمود - 1
    # apl-source:66
    if صف2 >= 0 and صف2 < 5 and عمود2 >= 0 and عمود2 < 5:
      # apl-source:67
      جار = صف2 * 5 + عمود2
      # apl-source:68
      if مزار[جار] == 0:
        # apl-source:69
        جوار[خلية][جار] = 1
        # apl-source:70
        جوار[جار][خلية] = 1
        # apl-source:71
        احفر(جار)
# apl-source:72

# apl-source:73
احفر(0)
# apl-source:74

# apl-source:75
# كل خلية زُارت
# apl-source:76
مجموع = 0
# apl-source:77
for x in مزار:
  # apl-source:78
  مجموع = مجموع + x
# apl-source:79
print("خلايا مزارة:", مجموع)
# apl-source:80
تأكد_يساوي(مجموع, 25, "كل الخلايا مزارة")
# apl-source:81

# apl-source:82
# متاهة مثالية على 25 خلية لها 24 ممراً بالضبط
# apl-source:83
ممرات = 0
# apl-source:84
for i in range(25):
  # apl-source:85
  for ج in range(i + 1, 25):
    # apl-source:86
    ممرات = ممرات + جوار[i][ج]
# apl-source:87
print("الممرات:", ممرات)
# apl-source:88
تأكد_يساوي(ممرات, 24, "شجرة: ن-1 ممر")
# apl-source:89

# apl-source:90
# حتمية البذرة: نفس النتيجة عند إعادة التوليد
# apl-source:91
بذرة[0] = 12345
# apl-source:92
مزار2 = []
# apl-source:93
for _ in range(25):
  # apl-source:94
  مزار2 = مزار2 + [0]
# apl-source:95
مزار = مزار2
# apl-source:96
جوار2 = []
# apl-source:97
for _ in range(25):
  # apl-source:98
  صف2 = []
  # apl-source:99
  for __ in range(25):
    # apl-source:100
    صف2 = صف2 + [0]
  # apl-source:101
  جوار2 = جوار2 + [صف2]
# apl-source:102
جوار = جوار2
# apl-source:103
احفر(0)
# apl-source:104
ممرات2 = 0
# apl-source:105
for i in range(25):
  # apl-source:106
  for ج in range(i + 1, 25):
    # apl-source:107
    ممرات2 = ممرات2 + جوار[i][ج]
# apl-source:108
تأكد_يساوي(ممرات2, 24, "حتمية البذرة")
# apl-source:109
