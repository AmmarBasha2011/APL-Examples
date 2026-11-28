
# apl-source:1
# مثال 851 — عدد سيارة الأجرة
# apl-source:2
# Taxicab number
# apl-source:3
# Demonstrates: مجموع مكعبين بطريقتين
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/851-taxicab-number.apl
# apl-source:6

# apl-source:7
# عدد سيارة الأجرة: 1729 = 1³+12³ = 9³+10³
# apl-source:8
# أصغر عدد يكتب مجموع مكعبين موجبين بطريقتين (حوار هاردي ورامانوجان)
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
def طرق_مكعبات(ن):
  # apl-source:19
  طرق = []
  # apl-source:20
  س = 1
  # apl-source:21
  while س * س * س <= ن // 2 + 1:
    # apl-source:22
    باقي = ن - س * س * س
    # apl-source:23
    # جذر تكعيبي صحيح للباقي إن وجد
    # apl-source:24
    ص = 1
    # apl-source:25
    while ص * ص * ص < باقي:
      # apl-source:26
      ص = ص + 1
    # apl-source:27
    if ص >= س and ص * ص * ص == باقي:
      # apl-source:28
      طرق = طرق + [[س, ص]]
    # apl-source:29
    س = س + 1
  # apl-source:30
  return طرق
# apl-source:31

# apl-source:32
طرق = طرق_مكعبات(1729)
# apl-source:33
print("طرق كتابة 1729:", طرق)
# apl-source:34

# apl-source:35
تأكد_يساوي(len(طرق), 2, "طريقتان")
# apl-source:36
تأكد_يساوي(طرق[0][0], 1, "الأولى تبدأ بـ 1")
# apl-source:37
تأكد_يساوي(طرق[0][1], 12, "الأولى: 1³+12³")
# apl-source:38
تأكد_يساوي(طرق[1][0], 9, "الثانية تبدأ بـ 9")
# apl-source:39
تأكد_يساوي(طرق[1][1], 10, "الثانية: 9³+10³")
# apl-source:40

# apl-source:41
# كل الأعداد الأصغر لها طريقة واحدة على الأكثر: مسح واحد على أزواج المكعبات
# apl-source:42
عد_الطرق = []
# apl-source:43
for _ in range(1729):
  # apl-source:44
  عد_الطرق = عد_الطرق + [0]
# apl-source:45
for س in range(1, 13):
  # apl-source:46
  for ص in range(س, 13):
    # apl-source:47
    مجموع = س * س * س + ص * ص * ص
    # apl-source:48
    if مجموع <= 1728:
      # apl-source:49
      عد_الطرق[مجموع] = عد_الطرق[مجموع] + 1
# apl-source:50
أصغر_بطريقتين = 0
# apl-source:51
for ن in range(2, 1729):
  # apl-source:52
  if عد_الطرق[ن] >= 2 and أصغر_بطريقتين == 0:
    # apl-source:53
    أصغر_بطريقتين = ن
# apl-source:54
تأكد_يساوي(أصغر_بطريقتين, 0, "لا عدد أصغر من 1729 بطريقتين")
# apl-source:55
