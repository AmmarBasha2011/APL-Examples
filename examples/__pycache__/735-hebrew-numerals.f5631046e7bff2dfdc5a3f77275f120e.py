
# apl-source:1
# مثال 735 — أرقام عبرية
# apl-source:2
# Hebrew numerals
# apl-source:3
# Demonstrates: جيماطريا، تحليل شره، 15 و16 خاصة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/735-hebrew-numerals.apl
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
# الأرقام العبرية (جيماطريا): تحويل عدد صحيح إلى حروف عبرية
# apl-source:25
# Demonstrates: تحليل شره بأزواج قيمة/حرف, حالات خاصة 15 و16
# apl-source:26
# 15 و16 لا تُكتبان يه/يو (اختصار اسم الله) بل טו/טז
# apl-source:27

# apl-source:28
أزواج = [
  # apl-source:29
  [400, "ת"], [300, "ש"], [200, "ר"], [100, "ק"],
  # apl-source:30
  [90, "צ"], [80, "פ"], [70, "ע"], [60, "ס"], [50, "נ"],
  # apl-source:31
  [40, "מ"], [30, "ל"], [20, "כ"], [10, "י"],
  # apl-source:32
  [9, "ט"], [8, "ח"], [7, "ז"], [6, "ו"], [5, "ה"],
  # apl-source:33
  [4, "ד"], [3, "ג"], [2, "ב"], [1, "א"]
# apl-source:34
]
# apl-source:35

# apl-source:36
def إلى_عبري(عدد):
  # apl-source:37
  if عدد <= 0:
    # apl-source:38
    return ""
  # apl-source:39
  ناتج = ""
  # apl-source:40
  باقي = عدد
  # apl-source:41
  for زوج in أزواج:
    # apl-source:42
    if باقي == 15:
      # apl-source:43
      ناتج = ناتج + "טו"
      # apl-source:44
      return ناتج
    # apl-source:45
    if باقي == 16:
      # apl-source:46
      ناتج = ناتج + "טז"
      # apl-source:47
      return ناتج
    # apl-source:48
    if باقي >= زوج[0]:
      # apl-source:49
      ناتج = ناتج + زوج[1]
      # apl-source:50
      باقي = باقي - زوج[0]
  # apl-source:51
  if باقي > 0:
    # apl-source:52
    ناتج = ناتج + إلى_عبري(باقي)
  # apl-source:53
  return ناتج
# apl-source:54

# apl-source:55
def قيمة_عبرية(حروف):
  # apl-source:56
  قيم = {}
  # apl-source:57
  for زوج in أزواج:
    # apl-source:58
    قيم[زوج[1]] = زوج[0]
  # apl-source:59
  مجموع = 0
  # apl-source:60
  for ي in range(len(حروف)):
    # apl-source:61
    مجموع = مجموع + قيم.get(حروف[ي], 0)
  # apl-source:62
  return مجموع
# apl-source:63

# apl-source:64
تأكد_يساوي(إلى_عبري(1), "א", "واحد")
# apl-source:65
تأكد_يساوي(إلى_عبري(7), "ז", "سبعة")
# apl-source:66
تأكد_يساوي(إلى_عبري(18), "יח", "حي = 18")
# apl-source:67
تأكد_يساوي(إلى_عبري(15), "טו", "خمسة عشر خاصة")
# apl-source:68
تأكد_يساوي(إلى_عبري(16), "טז", "ستة عشر خاصة")
# apl-source:69
تأكد_يساوي(إلى_عبري(42), "מב", "اثنان وأربعون")
# apl-source:70
تأكد_يساوي(إلى_عبري(100), "ק", "مئة")
# apl-source:71
تأكد_يساوي(إلى_عبري(248), "רמח", "مئتان وثمانية وأربعون")
# apl-source:72
تأكد_يساوي(إلى_عبري(365), "שסה", "أيام السنة")
# apl-source:73
تأكد_يساوي(إلى_عبري(115), "קטו", "مئة وخمسة عشر")
# apl-source:74
تأكد_يساوي(إلى_عبري(0), "", "صفر فارغ")
# apl-source:75

# apl-source:76
تأكد_يساوي(قيمة_عبرية("יח"), 18, "قيمة حي")
# apl-source:77
تأكد_يساوي(قيمة_عبرية("רמח"), 248, "قيمة عكسية")
# apl-source:78
تأكد_يساوي(قيمة_عبرية(إلى_عبري(613)), 613, "ذهاب وإياب 613")
# apl-source:79
تأكد_يساوي(قيمة_عبرية(إلى_عبري(999)), 999, "ذهاب وإياب 999")
# apl-source:80

# apl-source:81
print("18 =", إلى_عبري(18))
# apl-source:82
print("613 =", إلى_عبري(613))
# apl-source:83
