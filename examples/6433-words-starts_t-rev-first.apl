# مثال 6433 — الأول: الكلمات التي تبدأ بـ t ثم (كلمة معكوسة)
# first of rev over words starts_t
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6433-words-starts_t-rev-first.apl

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
      ر = ر + [ك[::-1]]
  لو len(ر) == 0:
    ارجع "لا شيء"
  ارجع ر[0]

تأكد_يساوي(ف("the cat sat on the mat"), "eht", "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), "لا شيء", "حالة 2")
تأكد_يساوي(ف("one two three four five six"), "owt", "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), "لا شيء", "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), "ot", "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), "لا شيء", "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), "ot", "حالة 7")
تأكد_يساوي(ف("hello"), "لا شيء", "حالة 8")
