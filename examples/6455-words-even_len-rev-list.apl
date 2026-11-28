# مثال 6455 — قائمة: الكلمات ذات الطول الزوجي ثم (كلمة معكوسة)
# list of rev over words even_len
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6455-words-even_len-rev-list.apl

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
    لو len(ك) % 2 == 0:
      ر = ر + [ك[::-1]]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["no"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["edoc", "elpmis"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["ruof", "evif"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["bb", "dddd"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["ot", "eb", "ro", "ot", "eb", "taht", "si", "noitseuq"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["atad", "atad", "atad", "edoc", "edoc"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["gninrael", "ot", "si", "gninrael", "ot"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
