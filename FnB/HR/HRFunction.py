import datetime


def promoteCheck(stafflist):
    promoteList = [] 
    now = datetime.datetime.now()
    for i in stafflist:
        if (now.year - i.last_promotion_year) >= 2:  # the promotion will be applied at the end of year only
            promoteList.append(i.ID)
    return promoteList

def serviceCheck(stafflist):
    stafflistservice = []
    yearmin = 10000
    for i in stafflist:
        if yearmin > i.entry_year:
            yearmin = i.entry_year
    for i in stafflist:
        if yearmin == i.entry_year:
            stafflistservice.append(i.ID)
    return stafflistservice