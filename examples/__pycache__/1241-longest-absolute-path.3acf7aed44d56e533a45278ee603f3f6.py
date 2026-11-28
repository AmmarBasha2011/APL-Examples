
# apl-source:1
# مثال 1241 — أطول مسار مطلق
# apl-source:2
# Longest absolute file path
# apl-source:3
# Demonstrates: مكدس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1241-longest-absolute-path.apl
# apl-source:6

# apl-source:7
# عمق كل سطر يحدد طول المسار قبله
# apl-source:8
# نخزن طول كل عمق ونحسب للملفات فقط
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
def اطول_مسار(نص_):
  # apl-source:19
  اطوال = {0: 0}
  # apl-source:20
  اقصى = 0
  # apl-source:21
  for سطر in نص_.split("\n"):
    # apl-source:22
    اسم = سطر.lstrip("\t")
    # apl-source:23
    عمق = len(سطر) - len(اسم)
    # apl-source:24
    if "." in اسم:
      # apl-source:25
      ط = اطوال[عمق] + len(اسم)
      # apl-source:26
      if ط > اقصى:
        # apl-source:27
        اقصى = ط
    # apl-source:28
    else:
      # apl-source:29
      اطوال[عمق + 1] = اطوال[عمق] + len(اسم) + 1
  # apl-source:30
  return اقصى
# apl-source:31

# apl-source:32
تأكد_يساوي(اطول_مسار("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"), 20, "مثال أول")
# apl-source:33
تأكد_يساوي(اطول_مسار("a"), 0, "لا ملفات")
# apl-source:34
تأكد_يساوي(اطول_مسار("file1.txt"), 9, "ملف في الجذر")
# apl-source:35
