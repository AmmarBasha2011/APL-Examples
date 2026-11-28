# مثال 6465 — الأول: الكلمات ذات الطول الزوجي ثم (طول الكلمة)
# first of len over words even_len
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6465-words-even_len-len-first.apl

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
    لو len(ك) % 2 == 0:
      ر = ر + [len(ك)]
  لو len(ر) == 0:
    ارجع "لا شيء"
  ارجع ر[0]

تأكد_يساوي(ف("the cat sat on the mat"), 2, "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), 4, "حالة 2")
تأكد_يساوي(ف("one two three four five six"), 4, "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), 2, "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), 2, "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), 4, "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), 8, "حالة 7")
تأكد_يساوي(ف("hello"), "لا شيء", "حالة 8")
