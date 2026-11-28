
# apl-source:1
# مثال 911 — أعظم نافذة منزلقة
# apl-source:2
# Sliding window maximum
# apl-source:3
# Demonstrates: طابور مزدوج متناقص
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/911-sliding-window-maximum.apl
# apl-source:6

# apl-source:7
# أعظم نافذة منزلقة: طابور مزدوج يحفظ المرشحين المتناقصين
# apl-source:8
# كل عنصر يدخل ويخرج مرة واحدة: O(n)
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def أعظم_نافذة(مصفوفة, ك):
  # apl-source:19
  نتيجة = []
  # apl-source:20
  طابور = []
  # apl-source:21
  for i in range(len(مصفوفة)):
    # apl-source:22
    # أخرج الأصغر من الذيل
    # apl-source:23
    while len(طابور) > 0 and مصفوفة[طابور[len(طابور) - 1]] <= مصفوفة[i]:
      # apl-source:24
      طابور = طابور[:len(طابور) - 1]
    # apl-source:25
    طابور = طابور + [i]
    # apl-source:26
    # أخرج الخارج عن النافذة من الرأس
    # apl-source:27
    if طابور[0] <= i - ك:
      # apl-source:28
      طابور = طابور[1:]
    # apl-source:29
    if i >= ك - 1:
      # apl-source:30
      نتيجة = نتيجة + [مصفوفة[طابور[0]]]
  # apl-source:31
  return نتيجة
# apl-source:32

# apl-source:33
نتيجة = أعظم_نافذة([1, 3, -1, -3, 5, 3, 6, 7], 3)
# apl-source:34
print("النواتج:", نتيجة)
# apl-source:35

# apl-source:36
تأكد_يساوي(len(نتيجة), 6, "عدد النوافذ")
# apl-source:37
تأكد_يساوي(نتيجة[0], 3, "نافذة 1")
# apl-source:38
تأكد_يساوي(نتيجة[1], 3, "نافذة 2")
# apl-source:39
تأكد_يساوي(نتيجة[2], 5, "نافذة 3")
# apl-source:40
تأكد_يساوي(نتيجة[3], 5, "نافذة 4")
# apl-source:41
تأكد_يساوي(نتيجة[4], 6, "نافذة 5")
# apl-source:42
تأكد_يساوي(نتيجة[5], 7, "نافذة 6")
# apl-source:43

# apl-source:44
# نافذة بحجم 1 تعيد المصفوفة نفسها
# apl-source:45
فردية = أعظم_نافذة([5, 2, 9], 1)
# apl-source:46
تأكد_يساوي(فردية[1], 2, "نافذة مفردة")
# apl-source:47

# apl-source:48
# نافذة تغطي الكل
# apl-source:49
كلية = أعظم_نافذة([2, 9, 4], 3)
# apl-source:50
تأكد_يساوي(len(كلية), 1, "نافذة واحدة")
# apl-source:51
تأكد_يساوي(كلية[0], 9, "الأعظم الكلي")
# apl-source:52
