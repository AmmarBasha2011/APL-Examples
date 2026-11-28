
# apl-source:1
# مثال 756 — لوحة دفوراك
# apl-source:2
# Dvorak keyboard
# apl-source:3
# Demonstrates: خريطة بالموضع، صف رئيسي، نسبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/756-keyboard-dvorak-lite.apl
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
# تحويل نص مكتوب بلوحة QWERTY كأنه Dvorak وقياس كفاءة الصف الرئيسي
# apl-source:25
# Demonstrates: خريطة حرف-لحرف بالموضع, نسبة الصف الرئيسي, مقارنة لوحات
# apl-source:26
# Dvorak يضع الحروف الأكثر استعمالاً في الصف الرئيسي
# apl-source:27

# apl-source:28
كويرتي = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
# apl-source:29
دفوراك = "',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz"
# apl-source:30

# apl-source:31
def حول_إلى_دفوراك(نص):
  # apl-source:32
  ناتج = ""
  # apl-source:33
  for ي in range(len(نص)):
    # apl-source:34
    if نص[ي] in كويرتي:
      # apl-source:35
      ناتج = ناتج + دفوراك[كويرتي.index(نص[ي])]
    # apl-source:36
    else:
      # apl-source:37
      ناتج = ناتج + نص[ي]
  # apl-source:38
  return ناتج
# apl-source:39

# apl-source:40
def نسبة_الصف_الرئيسي(نص, صف):
  # apl-source:41
  حروف = 0
  # apl-source:42
  رئيسي = 0
  # apl-source:43
  for ي in range(len(نص)):
    # apl-source:44
    if نص[ي] >= "a" and نص[ي] <= "z":
      # apl-source:45
      حروف = حروف + 1
      # apl-source:46
      if نص[ي] in صف:
        # apl-source:47
        رئيسي = رئيسي + 1
  # apl-source:48
  if حروف == 0:
    # apl-source:49
    return 0.0
  # apl-source:50
  return رئيسي * 100.0 / حروف
# apl-source:51

# apl-source:52
تأكد_يساوي(حول_إلى_دفوراك("qwerty"), "',.pyf", "الصف العلوي")
# apl-source:53
تأكد_يساوي(حول_إلى_دفوراك("asdfgh"), "aoeuid", "الصف الرئيسي")
# apl-source:54
تأكد_يساوي(حول_إلى_دفوراك("zxcv"), ";qjk", "الصف السفلي")
# apl-source:55
تأكد_يساوي(حول_إلى_دفوراك("a b"), "a x", "الفراغ يبقى")
# apl-source:56

# apl-source:57
صف_كويرتي = "asdfghjkl"
# apl-source:58
صف_دفوراك = "aoeuidhtns"
# apl-source:59
نص = "the quick brown fox jumps over a lazy dog"
# apl-source:60
دفوراكي = حول_إلى_دفوراك(نص)
# apl-source:61

# apl-source:62
نسبة_ك = نسبة_الصف_الرئيسي(نص, صف_كويرتي)
# apl-source:63
نسبة_د = نسبة_الصف_الرئيسي(نص, صف_دفوراك)
# apl-source:64
تأكد_يساوي(نسبة_د > نسبة_ك, True, "دفوراك أراح للأصابع")
# apl-source:65
تأكد_يساوي(round(نسبة_ك, 1), 30.3, "نسبة كويرتي الفعلية")
# apl-source:66
تأكد_يساوي(round(نسبة_د, 1), 48.5, "نسبة دفوراك الفعلية")
# apl-source:67

# apl-source:68
print("hello بلوحة دفوراك:", حول_إلى_دفوراك("hello"))
# apl-source:69
