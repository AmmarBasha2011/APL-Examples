# مثال 6429 — الأول: الكلمات التي تبدأ بـ t ثم (حروف كبيرة)
# first of upper over words starts_t
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6429-words-starts_t-upper-first.apl

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
    لو ك[0] == "t":
      ر = ر + [ك.upper()]
  لو len(ر) == 0:
    ارجع "لا شيء"
  ارجع ر[0]

تأكد_يساوي(ف("the cat sat on the mat"), "THE", "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), "لا شيء", "حالة 2")
تأكد_يساوي(ف("one two three four five six"), "TWO", "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), "لا شيء", "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), "TO", "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), "لا شيء", "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), "TO", "حالة 7")
تأكد_يساوي(ف("hello"), "لا شيء", "حالة 8")
