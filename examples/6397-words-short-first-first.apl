# مثال 6397 — الأول: الكلمات القصيرة (3 أو أقل) ثم (أول حرف)
# first of first over words short
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6397-words-short-first-first.apl

# نقسم النص إلى كلمات
# نصفّي ثم نحوّل كل كلمة
# ونرجع: الأول

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
      ر = ر + [ك[0]]
  لو len(ر) == 0:
    ارجع "لا شيء"
  ارجع ر[0]

تأكد_يساوي(ف("the cat sat on the mat"), "t", "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), "a", "حالة 2")
تأكد_يساوي(ف("one two three four five six"), "o", "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), "a", "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), "t", "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), "a", "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), "t", "حالة 7")
تأكد_يساوي(ف("hello"), "لا شيء", "حالة 8")
