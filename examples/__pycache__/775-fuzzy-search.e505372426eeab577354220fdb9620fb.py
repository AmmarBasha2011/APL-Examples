
# apl-source:1
# مثال 775 — بحث ضبابي
# apl-source:2
# Fuzzy search
# apl-source:3
# Demonstrates: مطابقة تتبعية، تسجيل نقاط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/775-fuzzy-search.apl
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
# بحث ضبابي بأسلوب fzf: مطابقة تتبعية مع تسجيل نقاط
# apl-source:25
# Demonstrates: مطابقة subsequence, مكافأة التتالي وبدايات الكلمات, خصم الفجوات
# apl-source:26

# apl-source:27
def درجة_ضبابي(استعلام, مرشح):
  # apl-source:28
  س = 0
  # apl-source:29
  درجة = 0
  # apl-source:30
  سابق = -2
  # apl-source:31
  for ي in range(len(مرشح)):
    # apl-source:32
    if س < len(استعلام) and مرشح[ي] == استعلام[س]:
      # apl-source:33
      درجة = درجة + 10
      # apl-source:34
      if ي == سابق + 1:
        # apl-source:35
        درجة = درجة + 6
      # apl-source:36
      if ي == 0 or مرشح[ي - 1] == "_" or مرشح[ي - 1] == "-" or مرشح[ي - 1] == " " or مرشح[ي - 1] == "/":
        # apl-source:37
        درجة = درجة + 8
      # apl-source:38
      درجة = درجة - (ي - سابق - 1)
      # apl-source:39
      سابق = ي
      # apl-source:40
      س = س + 1
  # apl-source:41
  if س == len(استعلام):
    # apl-source:42
    return درجة
  # apl-source:43
  return -1
# apl-source:44

# apl-source:45
تأكد_يساوي(درجة_ضبابي("fb", "fb"), 33, "تطابق تام")
# apl-source:46
تأكد_يساوي(درجة_ضبابي("fb", "foo_bar"), 32, "بداية كلمة")
# apl-source:47
تأكد_يساوي(درجة_ضبابي("fb", "fubar"), 26, "فجوة")
# apl-source:48
تأكد_يساوي(درجة_ضبابي("fb", "bar_foo"), -1, "لا مطابقة")
# apl-source:49

# apl-source:50
مرشحون = ["foo_bar", "fb", "fubar", "bar_foo"]
# apl-source:51
درجات = []
# apl-source:52
for م in مرشحون:
  # apl-source:53
  درجات.append(درجة_ضبابي("fb", م))
# apl-source:54
for ي in range(len(مرشحون)):
  # apl-source:55
  اقصى = ي
  # apl-source:56
  for ج in range(ي + 1, len(مرشحون)):
    # apl-source:57
    if درجات[ج] > درجات[اقصى]:
      # apl-source:58
      اقصى = ج
  # apl-source:59
  مؤقت1 = درجات[ي]
  # apl-source:60
  درجات[ي] = درجات[اقصى]
  # apl-source:61
  درجات[اقصى] = مؤقت1
  # apl-source:62
  مؤقت2 = مرشحون[ي]
  # apl-source:63
  مرشحون[ي] = مرشحون[اقصى]
  # apl-source:64
  مرشحون[اقصى] = مؤقت2
# apl-source:65
تأكد_يساوي(مرشحون[0], "fb", "الأفضل أولاً")
# apl-source:66
تأكد_يساوي(مرشحون[1], "foo_bar", "الثاني")
# apl-source:67
تأكد_يساوي(مرشحون[2], "fubar", "الثالث")
# apl-source:68
تأكد_يساوي(مرشحون[3], "bar_foo", "الأخير")
# apl-source:69
