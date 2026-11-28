# مثال 6482 — القائمة معكوسة: كل الكلمات ثم (كلمة معكوسة)
# rev of rev over words all
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6482-words-all-rev-rev.apl

# نقسم النص إلى كلمات
# نصفّي ثم نحوّل كل كلمة
# ونرجع: القائمة معكوسة

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ن):
  ر = []
  لكل ك في ن.split(" "):
    لو 1 == 1:
      ر = ر + [ك[::-1]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["tam", "eht", "no", "tas", "tac", "eht"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["nuf", "dna", "elpmis", "edoc", "sekam", "lpa"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["xis", "evif", "ruof", "eerht", "owt", "eno"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["eeeee", "dddd", "ccc", "bb", "a"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["noitseuq", "eht", "si", "taht", "eb", "ot", "ton", "ro", "eb", "ot"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["lpa", "edoc", "edoc", "atad", "atad", "atad"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["kniht", "ot", "gninrael", "si", "margorp", "ot", "gninrael"], "حالة 7")
تأكد_يساوي(ف("hello"), ["olleh"], "حالة 8")
