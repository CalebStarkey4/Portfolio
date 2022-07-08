import sys
if len(sys.argv) < 2:
    print('usage: {0} principal interest\n'.format(sys.argv[0]))
else:
    p = sys.argv[1]
    r = sys.argv[2]
    print(round(p*(1+r)**10), 2)
    print('%5.2f' % (p*(1+r)**20))
    print('{0:5.2f}'.format(p*(1+r)**30))