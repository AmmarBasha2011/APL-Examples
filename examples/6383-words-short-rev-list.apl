# مثال 6383 — قائمة: الكلمات القصيرة (3 أو أقل) ثم (كلمة معكوسة)
# list of rev over words short
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6383-words-short-rev-list.apl

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
    لو len(ك) <= 3:
      ر = ر + [ك[::-1]]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["eht", "tac", "tas", "no", "eht", "tam"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["lpa", "dna", "nuf"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["eno", "owt", "xis"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["a", "bb", "ccc"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["ot", "eb", "ro", "ton", "ot", "eb", "si", "eht"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["lpa"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["ot", "si", "ot"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
