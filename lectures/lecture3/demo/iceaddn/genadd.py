n = 64
for i in range(n):
    cin = "1'b1" if i == 0 else 'fa%d_COUT' % (i-1)
    print """\
wire fa%d_COUT;
wire fa%d_SUM;
FA fa%d (J1[%d], J3[%d], %s, fa%d_SUM, fa%d_COUT);
""" % (i, i, i, i%8, i%8, cin, i, i)

print 'assign D5 = fa%d_COUT;' % (n-1)

#FA fa%d (1'b1, 1'b0, %s, fa%d_SUM, fa%d_COUT);
#FA fa%d (A[%d], B[%d], %s, fa%d_SUM, fa%d_COUT);
