
# apl-source:1
# مثال 871 — جاوس-زايدل
# apl-source:2
# Gauss-Seidel
# apl-source:3
# Demonstrates: تحديث فوري بالقيم الجديدة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/871-gauss-seidel.apl
# apl-source:6

# apl-source:7
# جاوس-زايدل: حل تكراري للأنظمة الخطية يستخدم أحدث القيم فوراً
# apl-source:8
# يتقارب للمصفوفات المهيمنة قطرياً
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
def جاوس_زايدل(معاملات, ثوابت, تكرارات):
  # apl-source:19
  ن = len(ثوابت)
  # apl-source:20
  حل = []
  # apl-source:21
  for _ in range(ن):
    # apl-source:22
    حل = حل + [0.0]
  # apl-source:23
  for _ in range(تكرارات):
    # apl-source:24
    for i in range(ن):
      # apl-source:25
      مجموع = 0.0
      # apl-source:26
      for ج in range(ن):
        # apl-source:27
        if ج != i:
          # apl-source:28
          مجموع = مجموع + معاملات[i][ج] * حل[ج]
      # apl-source:29
      حل[i] = (ثوابت[i] - مجموع) / معاملات[i][i]
  # apl-source:30
  return حل
# apl-source:31

# apl-source:32
# 4س + ص = 1 ، س + 3ص = 2  =>  س = 1/11 ، ص = 7/11
# apl-source:33
حل = جاوس_زايدل(
  # apl-source:34
  [
    # apl-source:35
    [4.0, 1.0],
    # apl-source:36
    [1.0, 3.0]
  # apl-source:37
  ],
  # apl-source:38
  [1.0, 2.0],
  # apl-source:39
  50
# apl-source:40
)
# apl-source:41
print("الحل:", حل)
# apl-source:42

# apl-source:43
تأكد_يساوي(round(حل[0], 9), round(0.09090909090909091, 9), "س = 1/11")
# apl-source:44
تأكد_يساوي(round(حل[1], 9), round(0.6363636363636364, 9), "ص = 7/11")
# apl-source:45

# apl-source:46
# تحقق بالتعويض
# apl-source:47
تحقق1 = 4.0 * حل[0] + حل[1]
# apl-source:48
تحقق2 = حل[0] + 3.0 * حل[1]
# apl-source:49
تأكد_يساوي(round(تحقق1, 9), 1.0, "المعادلة الأولى")
# apl-source:50
تأكد_يساوي(round(تحقق2, 9), 2.0, "المعادلة الثانية")
# apl-source:51
