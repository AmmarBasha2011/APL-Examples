
# apl-source:1
# مثال 683 — القاعدة 110
# apl-source:2
# Rule 110
# apl-source:3
# Demonstrates: أتمتة أولية، جدول قاعدة، أجيال
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/683-rule-110.apl
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
# الأتمتة الخلوية الأولية: القاعدة 110 (تuring-complete)
# apl-source:25
# Demonstrates: جدول قاعدة من رقم, تطور أجيال, حدود ميتة
# apl-source:26
# القاعدة 110: 111->0 110->1 101->1 100->0 011->1 010->1 001->1 000->0
# apl-source:27

# apl-source:28
def جيل(صف, عرض):
  # apl-source:29
  جديد = []
  # apl-source:30
  for ج in range(عرض):
    # apl-source:31
    يسار = 0
    # apl-source:32
    if ج > 0:
      # apl-source:33
      يسار = صف[ج - 1]
    # apl-source:34
    وسط = صف[ج]
    # apl-source:35
    يمين = 0
    # apl-source:36
    if ج < عرض - 1:
      # apl-source:37
      يمين = صف[ج + 1]
    # apl-source:38
    قيمة = 4 * يسار + 2 * وسط + يمين
    # apl-source:39
    if قيمة == 0 or قيمة == 4 or قيمة == 7:
      # apl-source:40
      جديد.append(0)
    # apl-source:41
    else:
      # apl-source:42
      جديد.append(1)
  # apl-source:43
  return جديد
# apl-source:44

# apl-source:45
def نص(صف, عرض):
  # apl-source:46
  س = ""
  # apl-source:47
  for ج in range(عرض):
    # apl-source:48
    if صف[ج] == 1:
      # apl-source:49
      س = س + "#"
    # apl-source:50
    else:
      # apl-source:51
      س = س + " "
  # apl-source:52
  return س
# apl-source:53

# apl-source:54
عرض = 21
# apl-source:55
صف = []
# apl-source:56
for ج in range(عرض):
  # apl-source:57
  صف.append(0)
# apl-source:58
صف[10] = 1
# apl-source:59
تأكد_يساوي(نص(صف, عرض), "          #          ", "الجيل صفر")
# apl-source:60
صف = جيل(صف, عرض)
# apl-source:61
تأكد_يساوي(نص(صف, عرض), "         ##          ", "الجيل الأول")
# apl-source:62
صف = جيل(صف, عرض)
# apl-source:63
تأكد_يساوي(نص(صف, عرض), "        ###          ", "الجيل الثاني")
# apl-source:64
صف = جيل(صف, عرض)
# apl-source:65
تأكد_يساوي(نص(صف, عرض), "       ## #          ", "الجيل الثالث")
# apl-source:66
for ي in range(4):
  # apl-source:67
  صف = جيل(صف, عرض)
# apl-source:68
print("الجيل 7:", نص(صف, عرض))
# apl-source:69
مجموع = 0
# apl-source:70
for ج in range(عرض):
  # apl-source:71
  مجموع = مجموع + صف[ج]
# apl-source:72
تأكد_يساوي(مجموع, 6, "ست خلايا حية في الجيل السابع")
# apl-source:73
