
# apl-source:1
# مثال 260 — محول عملات بأسعار ثابتة
# apl-source:2
# Currency converter (fixed rates)
# apl-source:3
# Demonstrates: جدول أسعار، تحويل متسلسل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/260-currency-static.apl
# apl-source:6

# apl-source:7
أسعار = {"USD": 1.0, "EGP": 48.5, "EUR": 0.92, "SAR": 3.75, "AED": 3.67}
# apl-source:8

# apl-source:9
def حول(مبلغ, من, إلى):
    # apl-source:10
    بالدولار = مبلغ / أسعار[من]
    # apl-source:11
    return round(بالدولار * أسعار[إلى], 2)
# apl-source:12

# apl-source:13
print("100 دولار =", حول(100, "USD", "EGP"), "جنيه")
# apl-source:14
print("1000 جنيه =", حول(1000, "EGP", "SAR"), "ريال")
# apl-source:15
print("50 يورو =", حول(50, "EUR", "AED"), "درهم")
# apl-source:16
