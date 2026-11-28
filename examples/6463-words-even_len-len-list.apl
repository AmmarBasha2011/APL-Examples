# مثال 6463 — قائمة: الكلمات ذات الطول الزوجي ثم (طول الكلمة)
# list of len over words even_len
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6463-words-even_len-len-list.apl

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
      ر = ر + [len(ك)]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), [2], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), [4, 6], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), [4, 4], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), [2, 4], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), [2, 2, 2, 2, 2, 4, 2, 8], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), [4, 4, 4, 4, 4], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), [8, 2, 2, 8, 2], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
