
# apl-source:1
# مثال 868 — مصفوفة الفروقات
# apl-source:2
# Difference array
# apl-source:3
# Demonstrates: تحديث نطاق في O(1)
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/868-difference-array.apl
# apl-source:6

# apl-source:7
# مصفوفة الفروقات: تحديثات نطاقات كثيرة في O(1) لكل تحديث
# apl-source:8
# نبني التراكم مرة واحدة في النهاية بدل تعديل كل عنصر
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
def طبق_تحديثات(طول_مصفوفة, تحديثات):
  # apl-source:19
  # ف[ل] += ق ، ف[ر+1] -= ق
  # apl-source:20
  ف = []
  # apl-source:21
  for _ in range(طول_مصفوفة + 1):
    # apl-source:22
    ف = ف + [0]
  # apl-source:23
  for ت in تحديثات:
    # apl-source:24
    ف[ت[0]] = ف[ت[0]] + ت[2]
    # apl-source:25
    ف[ت[1] + 1] = ف[ت[1] + 1] - ت[2]
  # apl-source:26
  ناتج = []
  # apl-source:27
  جار = 0
  # apl-source:28
  for i in range(طول_مصفوفة):
    # apl-source:29
    جار = جار + ف[i]
    # apl-source:30
    ناتج = ناتج + [جار]
  # apl-source:31
  return ناتج
# apl-source:32

# apl-source:33
# أصفار من 5 عناصر: +2 على [1,3] ثم +3 على [0,2]
# apl-source:34
ناتج = طبق_تحديثات(5, [[1, 3, 2], [0, 2, 3]])
# apl-source:35
print("بعد التحديثين:", ناتج)
# apl-source:36

# apl-source:37
تأكد_يساوي(ناتج[0], 3, "الموضع 0: +3 فقط")
# apl-source:38
تأكد_يساوي(ناتج[1], 5, "الموضع 1: 2+3")
# apl-source:39
تأكد_يساوي(ناتج[3], 2, "الموضع 3: +2 فقط")
# apl-source:40
تأكد_يساوي(ناتج[4], 0, "الموضع 4: بلا تحديث")
# apl-source:41

# apl-source:42
# تحديث متداخل ثالث: -1 على [2,4]
# apl-source:43
ناتج2 = طبق_تحديثات(5, [[1, 3, 2], [0, 2, 3], [2, 4, -1]])
# apl-source:44
print("بعد ثلاثة تحديثات:", ناتج2)
# apl-source:45
تأكد_يساوي(ناتج2[2], 4, "الموضع 2: 2+3-1")
# apl-source:46
تأكد_يساوي(ناتج2[4], -1, "الموضع 4: -1")
# apl-source:47
