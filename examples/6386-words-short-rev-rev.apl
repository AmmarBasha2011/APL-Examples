# مثال 6386 — القائمة معكوسة: الكلمات القصيرة (3 أو أقل) ثم (كلمة معكوسة)
# rev of rev over words short
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6386-words-short-rev-rev.apl

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
    لو len(ك) <= 3:
      ر = ر + [ك[::-1]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["tam", "eht", "no", "tas", "tac", "eht"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["nuf", "dna", "lpa"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["xis", "owt", "eno"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["ccc", "bb", "a"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["eht", "si", "eb", "ot", "ton", "ro", "eb", "ot"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["lpa"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["ot", "si", "ot"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
