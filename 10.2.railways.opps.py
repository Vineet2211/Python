import pandas as pd
 
pd.DataFrame()
class RailwaysForm:
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysApplication=RailwaysForm()
harrysApplication.name="VINEET"
harrysApplication.train="Rajdhani Express"
harrysApplication.printData()

