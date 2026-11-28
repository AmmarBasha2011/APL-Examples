
# apl-source:1
# مثال 1520 — قيمة الحروف بالجمّل
# apl-source:2
# Abjad numeral value of a word
# apl-source:3
# Demonstrates: نصوص عربية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1520-abjad-numeral-value.apl
# apl-source:6

# apl-source:7
# أ=1 ب=2 ج=3 د=4
# apl-source:8
# نجمع قيم حروف الكلمة
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
def قيمة_الجمل(كلمة):
  # apl-source:19
  قيم = {"ا": 1, "ب": 2, "ج": 3, "د": 4, "ه": 5, "و": 6, "ز": 7, "ح": 8, "ط": 9, "ي": 10, "ك": 20, "ل": 30, "م": 40, "ن": 50, "س": 60, "ع": 70, "ف": 80, "ص": 90, "ق": 100, "ر": 200, "ش": 300, "ت": 400, "ث": 500, "خ": 600, "ذ": 700, "ض": 800, "ظ": 900, "غ": 1000}
  # apl-source:20
  مجموع = 0
  # apl-source:21
  for ح in كلمة:
    # apl-source:22
    مجموع = مجموع + قيم.get(ح, 0)
  # apl-source:23
  return مجموع
# apl-source:24

# apl-source:25
تأكد_يساوي(قيمة_الجمل("باب"), 5, "باب")
# apl-source:26
تأكد_يساوي(قيمة_الجمل("علم"), 140, "علم")
# apl-source:27
تأكد_يساوي(قيمة_الجمل("محمد"), 92, "محمد")
# apl-source:28
تأكد_يساوي(قيمة_الجمل(""), 0, "فارغة")
# apl-source:29
