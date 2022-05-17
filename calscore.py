class calsc():
    def calsum(self, sc):
        for i in range(len(sc)):
            sc[i][5] = sum(sc[i][2:5])
            print(sc[i])
    
    def meansc(self, sc):
        for i in range(len(sc)):
            if sc[i][5] == 0:
                print('是否尚未計算平均值')
            sc[i][6] = round(sc[i][5] / len(sc[i][2:-3]), 1)
            print(sc[i])

    def sortsc(self, sc):
        sc.sort(key = lambda x:x[5],reverse=True)
        for i in range(len(sc)):
            if sc[i][6] == sc[i - 1][6] and i > 1:
                sc[i][7] = i
                print(sc[i])
            else:
                sc[i][7] = i + 1
                print(sc[i])

sc = [[1, '洪錦魁', 80, 95, 88, 0, 0, 0],
      [2, '洪兵如', 98, 97, 96, 0, 0, 0],
      [3, '洪與星', 91, 93, 95, 0, 0, 0],
      [4, '洪與冰', 92, 97, 80, 0, 0, 0],
      [5, '洪星與', 92, 97, 90, 0, 0, 0]
    ]

#計算總分與平均
cal_sc = calsc()
print('計算總分:')
cal_sc.calsum(sc)
print('計算平均值:')
cal_sc.meansc(sc)
print('依平均排序名次:')
cal_sc.sortsc(sc)
