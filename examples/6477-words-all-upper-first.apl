# مثال 6477 — الأول: كل الكلمات ثم (حروف كبيرة)
# first of upper over words all
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6477-words-all-upper-first.apl

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
    لو 1 == 1:
      ر = ر + [ك.upper()]
  لو len(ر) == 0:
    ارجع "لا شيء"
  ارجع ر[0]

تأكد_يساوي(ف("the cat sat on the mat"), "THE", "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), "APL", "حالة 2")
تأكد_يساوي(ف("one two three four five six"), "ONE", "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), "A", "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), "TO", "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), "DATA", "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), "LEARNING", "حالة 7")
تأكد_يساوي(ف("hello"), "HELLO", "حالة 8")
