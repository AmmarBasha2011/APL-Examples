# مثال 6458 — القائمة معكوسة: الكلمات ذات الطول الزوجي ثم (كلمة معكوسة)
# rev of rev over words even_len
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6458-words-even_len-rev-rev.apl

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
    لو len(ك) % 2 == 0:
      ر = ر + [ك[::-1]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["no"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["elpmis", "edoc"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["evif", "ruof"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["dddd", "bb"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["noitseuq", "si", "taht", "eb", "ot", "ro", "eb", "ot"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["edoc", "edoc", "atad", "atad", "atad"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["ot", "gninrael", "si", "ot", "gninrael"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
