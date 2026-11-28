
# apl-source:1
# مثال 882 — كشف الدورة بفلويد
# apl-source:2
# Floyd cycle detection
# apl-source:3
# Demonstrates: سلحفاة وأرنب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/882-floyd-cycle.apl
# apl-source:6

# apl-source:7
# كشف الدورة بفلويد (السلحفاة والأرنب): مؤشران بسرعتين
# apl-source:8
# يجد دورة القائمة بذاكرة O(1) ثم يحدد بدايتها وطولها
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
# نمذجة قائمة مترابطة بدالة تالي على الفهارس
# apl-source:19
def تالي(س):
  # apl-source:20
  return (2 * س + 1) % 7
# apl-source:21

# apl-source:22
def فلويد(بداية):
  # apl-source:23
  سلحفاة = تالي(بداية)
  # apl-source:24
  أرنب = تالي(تالي(بداية))
  # apl-source:25
  while سلحفاة != أرنب:
    # apl-source:26
    سلحفاة = تالي(سلحفاة)
    # apl-source:27
    أرنب = تالي(تالي(أرنب))
  # apl-source:28
  # المرحلة الثانية: بداية الدورة
  # apl-source:29
  ميو = 0
  # apl-source:30
  سلحفاة = بداية
  # apl-source:31
  while سلحفاة != أرنب:
    # apl-source:32
    سلحفاة = تالي(سلحفاة)
    # apl-source:33
    أرنب = تالي(أرنب)
    # apl-source:34
    ميو = ميو + 1
  # apl-source:35
  # طول الدورة
  # apl-source:36
  لامدا = 1
  # apl-source:37
  أرنب = تالي(سلحفاة)
  # apl-source:38
  while سلحفاة != أرنب:
    # apl-source:39
    أرنب = تالي(أرنب)
    # apl-source:40
    لامدا = لامدا + 1
  # apl-source:41
  return [ميو, لامدا]
# apl-source:42

# apl-source:43
نتيجة = فلويد(0)
# apl-source:44
print("ميو ولامدا:", نتيجة)
# apl-source:45

# apl-source:46
تأكد_يساوي(نتيجة[0], 0, "الدورة تبدأ فوراً")
# apl-source:47
تأكد_يساوي(نتيجة[1], 3, "طول الدورة 3")
# apl-source:48

# apl-source:49
# تحقق مباشر: 0 -> 1 -> 3 -> 0
# apl-source:50
تأكد_يساوي(تالي(0), 1, "0 إلى 1")
# apl-source:51
تأكد_يساوي(تالي(1), 3, "1 إلى 3")
# apl-source:52
تأكد_يساوي(تالي(3), 0, "3 إلى 0")
# apl-source:53

# apl-source:54
# ذيل أطول: تالي2 = س+1 لـ س<4 ثم دورة
# apl-source:55
def تالي2(س):
  # apl-source:56
  if س < 4:
    # apl-source:57
    return س + 1
  # apl-source:58
  return 4 + (س - 3) % 3
# apl-source:59

# apl-source:60
def فلويد2(بداية):
  # apl-source:61
  سلحفاة = تالي2(بداية)
  # apl-source:62
  أرنب = تالي2(تالي2(بداية))
  # apl-source:63
  while سلحفاة != أرنب:
    # apl-source:64
    سلحفاة = تالي2(سلحفاة)
    # apl-source:65
    أرنب = تالي2(تالي2(أرنب))
  # apl-source:66
  ميو = 0
  # apl-source:67
  سلحفاة = بداية
  # apl-source:68
  while سلحفاة != أرنب:
    # apl-source:69
    سلحفاة = تالي2(سلحفاة)
    # apl-source:70
    أرنب = تالي2(أرنب)
    # apl-source:71
    ميو = ميو + 1
  # apl-source:72
  لامدا = 1
  # apl-source:73
  أرنب = تالي2(سلحفاة)
  # apl-source:74
  while سلحفاة != أرنب:
    # apl-source:75
    أرنب = تالي2(أرنب)
    # apl-source:76
    لامدا = لامدا + 1
  # apl-source:77
  return [ميو, لامدا]
# apl-source:78

# apl-source:79
نتيجة2 = فلويد2(0)
# apl-source:80
print("مع ذيل:", نتيجة2)
# apl-source:81
تأكد_يساوي(نتيجة2[0], 4, "الدورة تبدأ بعد ذيل 4")
# apl-source:82
تأكد_يساوي(نتيجة2[1], 3, "طول الدورة 3")
# apl-source:83
