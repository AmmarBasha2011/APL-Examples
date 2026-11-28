
# apl-source:1
# مثال 991 — تجميع كثافي
# apl-source:2
# DBSCAN clustering
# apl-source:3
# Demonstrates: توسيع بذور الجوار
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/991-dbscan.apl
# apl-source:6

# apl-source:7
# تجميع كثافي DBSCAN: عنقود حيث تتقارب النقاط وضجيج حيث تنفرد
# apl-source:8
# لا يحتاج عدد العناقيد مسبقاً
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
نقاط = [[0, 0], [0, 1], [1, 0], [10, 10], [10, 11], [11, 10], [50, 50]]
# apl-source:19
ن = 7
# apl-source:20
أبسيلون2 = 2.25
# apl-source:21
أدنى = 2
# apl-source:22

# apl-source:23
def جيران(i):
  # apl-source:24
  ناتج = []
  # apl-source:25
  for j in range(ن):
    # apl-source:26
    ف_س = نقاط[j][0] - نقاط[i][0]
    # apl-source:27
    ف_ص = نقاط[j][1] - نقاط[i][1]
    # apl-source:28
    if ((ف_س * ف_س) + (ف_ص * ف_ص)) <= أبسيلون2:
      # apl-source:29
      ناتج = ناتج + [j]
  # apl-source:30
  return ناتج
# apl-source:31

# apl-source:32
وسوم = [-2, -2, -2, -2, -2, -2, -2]
# apl-source:33
عنقود = 0
# apl-source:34
for i in range(ن):
  # apl-source:35
  if وسوم[i] == -2:
    # apl-source:36
    جوار = جيران(i)
    # apl-source:37
    if len(جوار) < أدنى:
      # apl-source:38
      وسوم[i] = -1
    # apl-source:39
    else:
      # apl-source:40
      وسوم[i] = عنقود
      # apl-source:41
      بذور = []
      # apl-source:42
      for j in جوار:
        # apl-source:43
        if j != i:
          # apl-source:44
          بذور = بذور + [j]
      # apl-source:45
      رأس = 0
      # apl-source:46
      while رأس < len(بذور):
        # apl-source:47
        j = بذور[رأس]
        # apl-source:48
        رأس = رأس + 1
        # apl-source:49
        if وسوم[j] == -1:
          # apl-source:50
          وسوم[j] = عنقود
        # apl-source:51
        if وسوم[j] == -2:
          # apl-source:52
          وسوم[j] = عنقود
          # apl-source:53
          جوار2 = جيران(j)
          # apl-source:54
          if len(جوار2) >= أدنى:
            # apl-source:55
            for ك in جوار2:
              # apl-source:56
              if وسوم[ك] == -2:
                # apl-source:57
                بذور = بذور + [ك]
      # apl-source:58
      عنقود = عنقود + 1
# apl-source:59

# apl-source:60
تأكد_يساوي(عنقود, 2, "عنقودان")
# apl-source:61
تأكد_يساوي(وسوم[0], 0, "أول نقطة بالعنقود الأول")
# apl-source:62
تأكد_يساوي(وسوم[3], 1, "رابع نقطة بالعنقود الثاني")
# apl-source:63
تأكد_يساوي(وسوم[6], -1, "البعيدة ضجيج")
# apl-source:64
