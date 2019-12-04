#!/usr/bin/env python
# coding: utf-8


class Staff:
    def __init__(self, ID, name, title, supervisor, salary, entry_year, last_promotion_year, store_name):
        self.ID = ID
        self.name=name
        self.title=title
        self.supervisor=supervisor
        self.salary=salary
        self.entry_year=entry_year
        self.last_promotion_year=last_promotion_year
        self.store_name=store_name
    def info(self):
        print("ID: ", self.ID)
        print("Name: ", self.name)
        print("Title: ", self.title)
        print("SupervisorID: ", self.supervisor)
        print("Salary: ", self.salary) 
        print("Entry year: ", self.entry_year)
        print("Last promotion year: ", self.last_promotion_year)
        print("Store name: ", self.store_name)
        print("")

class Manager(Staff):
    def __init__(self, ID, name, title, supervisor, salary, entry_year, last_promotion_year, store_name, stafflist):
        Staff.__init__(self, ID, name, title, supervisor, salary, entry_year, last_promotion_year, store_name)
        self.stafflist=stafflist
    def info(self):
        Staff.info(self)
        print("Staff list (ID): ", self.stafflist)
