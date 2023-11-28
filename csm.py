def get_hpr(str2):
    str1 = """0
1.220114802
0.573452033
-0.065770671
0.243326172
-0.338169105
    """

    y = 0.00422179

    coef = list(map(float, str1.split()))
    ar = list(map(float, str2.split()))

    result = y
    for i in range(6):
        result += coef[i] * ar[i]
    return result

def get_mdd(str2):
    str1 = """0
0.076256674
0.16251229
0.287837163
0.435322501
-0.095515972
    """

    y = 0.037487693


    coef = list(map(float, str1.split()))
    ar = list(map(float, str2.split()))

    result = y
    for i in range(6):
        result += coef[i] * ar[i]
    return result


lst = [x/100 for x in range(101)]
lst_thr = [x/100 for x in range(101)]
mx_val = []
mx_hpr = 0

while True:
  for threshold in lst_thr:
    for krw in lst:
      for ada in lst:
        for eth in lst:
          for doge in lst:
            btc = 1-(krw+ada+eth+doge)
            if ada<0:
              continue

            strr = " ".join([str(krw),str(btc),str(eth),str(doge),str(ada),str(threshold)])
            hpr = get_hpr(strr)
            mdd = get_mdd(strr)

            if mdd > 0.15:
              continue
            if hpr > mx_hpr:
              mx_hpr = hpr
              mx_val = [krw,btc,eth,doge,ada,threshold]
              print(f'HPR={mx_hpr*100:.1f}')
              print(mx_val)