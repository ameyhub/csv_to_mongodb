import pymongo
from pymongo import MongoClient
import pandas as pd
import json

items = 'C:/Users/ameyd/csv_to_mongodb/Churn_Modelling.csv'


class mongo(object):

    def __init__(self, dbname=None, collectionname=None):
        self.dbname = dbname
        self.collectionname = collectionname

        self.client = MongoClient("localhost", 27017, maxPoolSize=50)

        self.DB = self.client[self.dbname]
        self.collection = self.DB[self.collectionname]

    def InsertData(self, path=items):
        df = pd.read_csv(" ")
        data = df.to_dict('records')

        self.collection.insert_many(data, ordered=False)
        print("All the Data has been Exported to Mongo DB Server .... ")


if __name__ == "__main__":
    mongodb = mongo(dbname='Dataset', collectionname='Churn_Modelling')
    #mongodb = InsertData(path='C:/Users/ameyd/csv_to_mongodb/Churn_Modelling.csv')
