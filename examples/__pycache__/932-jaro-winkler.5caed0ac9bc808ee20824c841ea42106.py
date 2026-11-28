
# apl-source:1
# مثال 932 — تشابه جارو-وينكلر
# apl-source:2
# Jaro-Winkler similarity
# apl-source:3
# Demonstrates: مطابقات وتبديلات وبادئة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/932-jaro-winkler.apl
# apl-source:6

# apl-source:7
# تشابه جارو-وينكلر: قياس تقارب السلاسل النصية
# apl-source:8
# جارو + مكافأة للبادئة المشتركة (مناسب للأسماء)
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
def جارو(س1, س2):
  # apl-source:19
  ن1 = len(س1)
  # apl-source:20
  ن2 = len(س2)
  # apl-source:21
  نافذة = (ن1 + ن2) // 4
  # apl-source:22
  if نافذة < 1:
    # apl-source:23
    نافذة = 1
  # apl-source:24
  م1 = []
  # apl-source:25
  م2 = []
  # apl-source:26
  for _ in range(ن1):
    # apl-source:27
    م1 = م1 + [0]
  # apl-source:28
  for _ in range(ن2):
    # apl-source:29
    م2 = م2 + [0]
  # apl-source:30
  مطابقات = 0
  # apl-source:31
  for i in range(ن1):
    # apl-source:32
    بداية = i - نافذة
    # apl-source:33
    if بداية < 0:
      # apl-source:34
      بداية = 0
    # apl-source:35
    نهاية = i + نافذة + 1
    # apl-source:36
    if نهاية > ن2:
      # apl-source:37
      نهاية = ن2
    # apl-source:38
    for ج in range(بداية, نهاية):
      # apl-source:39
      if (م2[ج] == 0) and (س2[ج] == س1[i]):
        # apl-source:40
        م1[i] = 1
        # apl-source:41
        م2[ج] = 1
        # apl-source:42
        مطابقات = مطابقات + 1
  # apl-source:43
  if مطابقات == 0:
    # apl-source:44
    return 0
  # apl-source:45
  تبديلات = 0
  # apl-source:46
  k = 0
  # apl-source:47
  for i in range(ن1):
    # apl-source:48
    if م1[i] == 1:
      # apl-source:49
      while م2[k] == 0:
        # apl-source:50
        k = k + 1
      # apl-source:51
      if س1[i] != س2[k]:
        # apl-source:52
        تبديلات = تبديلات + 1
      # apl-source:53
      k = k + 1
  # apl-source:54
  return (مطابقات / ن1 + مطابقات / ن2 + (مطابقات - تبديلات / 2) / مطابقات) / 3
# apl-source:55

# apl-source:56
def جارو_وينكلر(س1, س2):
  # apl-source:57
  ج = جارو(س1, س2)
  # apl-source:58
  بادئة = 0
  # apl-source:59
  متصل = 1
  # apl-source:60
  for i in range(4):
    # apl-source:61
    if متصل == 1 and (i < len(س1)) and (i < len(س2)) and (س1[i] == س2[i]):
      # apl-source:62
      بادئة = بادئة + 1
    # apl-source:63
    else:
      # apl-source:64
      متصل = 0
  # apl-source:65
  return ج + بادئة * 0.1 * (1 - ج)
# apl-source:66

# apl-source:67
print("martha/marhta:", جارو_وينكلر("martha", "marhta"))
# apl-source:68
print("dwayne/duane:", جارو_وينكلر("dwayne", "duane"))
# apl-source:69

# apl-source:70
تأكد_يساوي(round(جارو_وينكلر("martha", "marhta"), 6), 0.961111, "مارثا")
# apl-source:71
تأكد_يساوي(round(جارو_وينكلر("dwayne", "duane"), 6), 0.84, "دواين")
# apl-source:72
تأكد_يساوي(جارو_وينكلر("abc", "abc"), 1, "تطابق تام")
# apl-source:73

# apl-source:74
# نافذة المطابقة: نصف طول الأطول ناقص واحد
# apl-source:75
# ملاحظة: صيغة (ن1+ن2)//4 تقارب max//2-1 للسلاسل المتقاربة
# apl-source:76
تأكد_يساوي(round(جارو("abcd", "wxyz"), 6), 0, "لا مطابقات")
# apl-source:77
