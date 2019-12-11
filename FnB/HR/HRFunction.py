import datetime


class YearError(Exception):
    def __init__(self, yearcheck): # Constructor or Initializer
        self.year=yearcheck 
        
class EmptyError(Exception):
    pass

class EntryError(Exception):
    pass 
    
    
def promoteCheck(stafflist):
    try:
        if not stafflist:
            raise(EmptyError())
        promoteList = [] 
        now = datetime.datetime.now()
        for i in stafflist:
            if i.last_promotion_year > now.year:
                raise(YearError(i.last_promotion_year))
            if (now.year - i.last_promotion_year) >= 2:  # the promotion will be applied at the end of year only
                promoteList.append(i.ID)
        return promoteList
    except AttributeError:
        print("This is not a list of Staff instances.")
    except YearError as YE:
        print("One staff has incorrect last_promotion_year:",YE.year)
    except EmptyError as EE:
        print("The staff list is empty")
    except :
        print("There is an error occured")
    finally:
        print("This is the end of the command") 

def serviceCheck(stafflist):
    try:
        now = datetime.datetime.now()
        if not stafflist:
            raise(EmptyError())
        stafflistservice = []
        yearmin = 10000
        for i in stafflist:
            if i.entry_year > now.year:
                raise(EntryError())
            if yearmin > i.entry_year:
                yearmin = i.entry_year
        for i in stafflist:
            if yearmin == i.entry_year:
                stafflistservice.append(i.ID)
        return stafflistservice
    except AttributeError:
        print("This is not a list of Staff instances.")
    except EntryError as YE:
        print("One staff has incorrect entry_year")
    except EmptyError as EE:
        print("The staff list is empty")
    except :
        print("There is an error occured")
    finally:
        print("This is the end of the command") 