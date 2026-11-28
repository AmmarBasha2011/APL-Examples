# مثال 6467 — قائمة: الكلمات ذات الطول الزوجي ثم (أول حرف)
# list of first over words even_len
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6467-words-even_len-first-list.apl

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
      ر = ر + [ك[0]]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["o"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["c", "s"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["f", "f"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["b", "d"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["t", "b", "o", "t", "b", "t", "i", "q"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["d", "d", "d", "c", "c"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["l", "t", "i", "l", "t"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
