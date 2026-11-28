# مثال 6370 — القائمة معكوسة: الكلمات الأطول من 3 حروف ثم (طول الكلمة)
# rev of len over words long3
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6370-words-long3-len-rev.apl

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
    لو len(ك) > 3:
      ر = ر + [len(ك)]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), [], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), [6, 4, 5], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), [4, 4, 5], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), [5, 4], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), [8, 4], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), [4, 4, 4, 4, 4], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), [5, 8, 7, 8], "حالة 7")
تأكد_يساوي(ف("hello"), [5], "حالة 8")
