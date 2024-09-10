from eqt_ana import calc_eqt, trace_eqt_ana
DL, Delta, M, M0 = calc_eqt(
    Epsilon=23.44, W=282.99, M0=356.83, e=0.0167)
trace_eqt_ana(DL, Delta, M, M0)
DL, Delta, M, M0 = calc_eqt(
    Epsilon=23.44, W=282.99, M0=356.83, e=0.0)
trace_eqt_ana(DL, Delta, M, M0)
DL, Delta, M, M0 = calc_eqt(
    Epsilon=0.0, W=282.99, M0=356.83, e=0.0167)
trace_eqt_ana(DL, Delta, M, M0)
