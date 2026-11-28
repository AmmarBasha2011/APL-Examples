# مثال 6471 — قائمة: الكلمات ذات الطول الزوجي ثم (آخر حرف)
# list of last over words even_len
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6471-words-even_len-last-list.apl

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
      ر = ر + [ك[len(ك) - 1]]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["n"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["e", "e"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["r", "e"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["b", "d"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["o", "e", "r", "o", "e", "t", "s", "n"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["a", "a", "a", "e", "e"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["g", "o", "s", "g", "o"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
