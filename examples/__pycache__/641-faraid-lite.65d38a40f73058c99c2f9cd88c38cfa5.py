
# apl-source:1
# مثال 641 — الفرائض المبسطة
# apl-source:2
# Islamic inheritance shares
# apl-source:3
# Demonstrates: فرائض، أنصبة، عصبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/641-faraid-lite.apl
# apl-source:6

# apl-source:7
# Assertion style:
# apl-source:8
#   دالة تأكد_يساوي(فعلي, متوقع, اسم):
# apl-source:9
#     لو فعلي != متوقع:
# apl-source:10
#       اطبع "فشل:", اسم
# apl-source:11
#       اطبع "  متوقع:", متوقع
# apl-source:12
#       اطبع "  فعلي:", فعلي
# apl-source:13
#       قياسي_نظام_اخرج(1)
# apl-source:14
#     اطبع "ناجح:", اسم
# apl-source:15

# apl-source:16
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:17
  if فعلي != متوقع:
    # apl-source:18
    print("فشل:", اسم)
    # apl-source:19
    print("  متوقع:", متوقع)
    # apl-source:20
    print("  فعلي:", فعلي)
    # apl-source:21
    قياسي_نظام_اخرج(1)
  # apl-source:22
  print("ناجح:", اسم)
# apl-source:23

# apl-source:24
# الفرائض المبسطة: الأنصبة الشرعية الثابتة
# apl-source:25
# Demonstrates: أنصبة مقررة, عصبة بالباقي, حالات شائعة
# apl-source:26
# تطبيق تعليمي مبسط؛ الفتوى للجهات الشرعية المختصة
# apl-source:27

# apl-source:28
def وزّع(تركة, زوج, أبناء, بنات):
  # apl-source:29
  أنصبة = {}
  # apl-source:30
  if زوج:
    # apl-source:31
    if أبناء + بنات > 0:
      # apl-source:32
      أنصبة["زوج"] = تركة // 4
    # apl-source:33
    else:
      # apl-source:34
      أنصبة["زوج"] = تركة // 2
  # apl-source:35
  باقي = تركة
  # apl-source:36
  for مفتاح in أنصبة:
    # apl-source:37
    باقي = باقي - أنصبة[مفتاح]
  # apl-source:38
  أسهم = أبناء * 2 + بنات
  # apl-source:39
  if أسهم > 0:
    # apl-source:40
    أنصبة["ابن"] = باقي * 2 // أسهم
    # apl-source:41
    أنصبة["بنت"] = باقي // أسهم
  # apl-source:42
  return أنصبة
# apl-source:43

# apl-source:44
ن1 = وزّع(120000, True, 2, 1)
# apl-source:45
print("زوج وابنان وبنت:", ن1)
# apl-source:46
تأكد_يساوي(ن1["زوج"], 30000, "ربع الزوج مع الفرع")
# apl-source:47
تأكد_يساوي(ن1["ابن"], 36000, "للذكر مثل حظ الأنثيين")
# apl-source:48
تأكد_يساوي(ن1["بنت"], 18000, "نصيب البنت")
# apl-source:49
تأكد_يساوي(ن1["زوج"] + 2 * ن1["ابن"] + ن1["بنت"], 120000, "التركة كاملة")
# apl-source:50
ن2 = وزّع(80000, True, 0, 0)
# apl-source:51
تأكد_يساوي(ن2["زوج"], 40000, "نصف الزوج بلا فرع")
# apl-source:52
