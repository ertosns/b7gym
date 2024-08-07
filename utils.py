from consts import *

def get_price(period, count, week_mode=NO_BODYBUILDING, cardio_mode=NO_CARDIO):
    int_period = 1
    discount = 0
    if period==MONTHLY:
        int_period = 1
        discount = 0
    elif period==THREE_MONTHS:
        int_period = 3
        discount = THREE_MONTHS_DISCOUNT
    elif period==SIX_MONTHS:
        int_period = 6
        discount = SIX_MONTHS_DISCOUNT
    elif period==YEARLY:
        int_period = 12
        discount = YEARLY_DISCOUNT
    else:
        messagebox.showerror("No such thing as period {}".format(period))
        return CANT_GET_PRICE
    cost = 0
    if week_mode == FULL_WEEK:
        cost += 200
    elif week_mode == HALF_WEEK:
        cost += 100
    if cardio_mode == FULL_WEEK:
        cost += 300
    elif cardio_mode == HALF_WEEK:
        cost += 150
    return count*cost*int_period*(1-discount)
