# مثال 6479 — قائمة: كل الكلمات ثم (كلمة معكوسة)
# list of rev over words all
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6479-words-all-rev-list.apl

# نقسم النص إلى كلمات
# نصفّي ثم نحوّل كل كلمة
# ونرجع: قائمة

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
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["eht", "tac", "tas", "no", "eht", "tam"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["lpa", "sekam", "edoc", "elpmis", "dna", "nuf"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["eno", "owt", "eerht", "ruof", "evif", "xis"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["a", "bb", "ccc", "dddd", "eeeee"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["ot", "eb", "ro", "ton", "ot", "eb", "taht", "si", "eht", "noitseuq"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["atad", "atad", "atad", "edoc", "edoc", "lpa"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["gninrael", "ot", "margorp", "si", "gninrael", "ot", "kniht"], "حالة 7")
تأكد_يساوي(ف("hello"), ["olleh"], "حالة 8")
