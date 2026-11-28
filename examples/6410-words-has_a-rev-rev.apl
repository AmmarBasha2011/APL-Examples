# مثال 6410 — القائمة معكوسة: الكلمات التي فيها a ثم (كلمة معكوسة)
# rev of rev over words has_a
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6410-words-has_a-rev-rev.apl

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
    لو "a" in ك:
      ر = ر + [ك[::-1]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["tam", "tas", "tac"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["dna", "sekam", "lpa"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), [], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["a"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["taht"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["lpa", "atad", "atad", "atad"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["gninrael", "margorp", "gninrael"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
