
# apl-source:1
# مثال 994 — شجرة المدى الكسولة
# apl-source:2
# Lazy segment tree
# apl-source:3
# Demonstrates: تحديث مؤجل بالدفع
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/994-lazy-segment-tree.apl
# apl-source:6

# apl-source:7
# شجرة المدى الكسولة: إضافة على مدى واستعلام مجموع بلا تحديث كل ورقة
# apl-source:8
# التحديث يؤجل في عقدة كسولة حتى يحتاجه نزول لاحق
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
شجرة = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# apl-source:19
كسول = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# apl-source:20
مصفوفة = [1, 3, 5, 7, 9, 11]
# apl-source:21

# apl-source:22
def ابن(عقدة, بداية, نهاية):
  # apl-source:23
  if بداية == نهاية:
    # apl-source:24
    شجرة[عقدة] = مصفوفة[بداية]
    # apl-source:25
    return 0
  # apl-source:26
  وسط = (بداية + نهاية) // 2
  # apl-source:27
  ابن((عقدة * 2) + 1, بداية, وسط)
  # apl-source:28
  ابن((عقدة * 2) + 2, وسط + 1, نهاية)
  # apl-source:29
  شجرة[عقدة] = شجرة[(عقدة * 2) + 1] + شجرة[(عقدة * 2) + 2]
  # apl-source:30
  return 0
# apl-source:31

# apl-source:32
def ادفع(عقدة, بداية, نهاية):
  # apl-source:33
  if كسول[عقدة] != 0:
    # apl-source:34
    شجرة[عقدة] = شجرة[عقدة] + (كسول[عقدة] * ((نهاية - بداية) + 1))
    # apl-source:35
    if بداية != نهاية:
      # apl-source:36
      كسول[(عقدة * 2) + 1] = كسول[(عقدة * 2) + 1] + كسول[عقدة]
      # apl-source:37
      كسول[(عقدة * 2) + 2] = كسول[(عقدة * 2) + 2] + كسول[عقدة]
    # apl-source:38
    كسول[عقدة] = 0
  # apl-source:39
  return 0
# apl-source:40

# apl-source:41
def حدث(عقدة, بداية, نهاية, غ, ح, قيمة):
  # apl-source:42
  ادفع(عقدة, بداية, نهاية)
  # apl-source:43
  if (نهاية < غ) or (بداية > ح):
    # apl-source:44
    return 0
  # apl-source:45
  if (غ <= بداية) and (نهاية <= ح):
    # apl-source:46
    كسول[عقدة] = كسول[عقدة] + قيمة
    # apl-source:47
    ادفع(عقدة, بداية, نهاية)
    # apl-source:48
    return 0
  # apl-source:49
  وسط = (بداية + نهاية) // 2
  # apl-source:50
  حدث((عقدة * 2) + 1, بداية, وسط, غ, ح, قيمة)
  # apl-source:51
  حدث((عقدة * 2) + 2, وسط + 1, نهاية, غ, ح, قيمة)
  # apl-source:52
  شجرة[عقدة] = شجرة[(عقدة * 2) + 1] + شجرة[(عقدة * 2) + 2]
  # apl-source:53
  return 0
# apl-source:54

# apl-source:55
def استعلم(عقدة, بداية, نهاية, غ, ح):
  # apl-source:56
  ادفع(عقدة, بداية, نهاية)
  # apl-source:57
  if (نهاية < غ) or (بداية > ح):
    # apl-source:58
    return 0
  # apl-source:59
  if (غ <= بداية) and (نهاية <= ح):
    # apl-source:60
    return شجرة[عقدة]
  # apl-source:61
  وسط = (بداية + نهاية) // 2
  # apl-source:62
  يسار = استعلم((عقدة * 2) + 1, بداية, وسط, غ, ح)
  # apl-source:63
  يمين = استعلم((عقدة * 2) + 2, وسط + 1, نهاية, غ, ح)
  # apl-source:64
  return يسار + يمين
# apl-source:65

# apl-source:66
ابن(0, 0, 5)
# apl-source:67
تأكد_يساوي(استعلم(0, 0, 5, 0, 5), 36, "المجموع قبل الإضافة")
# apl-source:68
حدث(0, 0, 5, 1, 3, 10)
# apl-source:69
تأكد_يساوي(استعلم(0, 0, 5, 0, 5), 66, "المجموع بعد الإضافة")
# apl-source:70
تأكد_يساوي(استعلم(0, 0, 5, 1, 3), 45, "مجموع المدى المعدل")
# apl-source:71
تأكد_يساوي(استعلم(0, 0, 5, 4, 5), 20, "مدى غير معدل")
# apl-source:72
