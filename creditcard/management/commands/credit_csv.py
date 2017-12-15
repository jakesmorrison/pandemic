__author__ = 'jsmorrison'
from django.core.management.base import BaseCommand
from ...models import CreditStatus, PointsUsed
import pandas as pd
import numpy as np


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('type')

    def handle(self, *args, **options):
        self.convert_csv_to_db(options['type'])

    def convert_csv_to_db(self, csv_path):
        csv_path_1 = "/root/pandemic/creditcard/static/creditcard/csv/credit_status.csv"
        csv_path_2 = "/root/pandemic/creditcard/static/creditcard/csv/points_used.csv"
        df = pd.read_csv(csv_path_1)
        df = df.fillna(value=0)
        for index, row in df.iterrows():
            s = CreditStatus(
                status=row["Status"],
                holder =row["NameOnCard"],
                issuer = row["Issuer"],
                card = row["Card"],
                issuedate=str(row["IssueDate"].split("/")[2] + "-" + row["IssueDate"].split("/")[0] + "-" + row["IssueDate"].split("/")[1]),
                closedate=str(row["CloseDate"].split("/")[2] + "-" + row["CloseDate"].split("/")[0] + "-" + row["CloseDate"].split("/")[1]),
                line = int(row["Line"]),
                fee = int(row["AnnualFee"]),
                minspend = int(row["MinSpend"]),
                bonus = int(row["Bonus"]),
            )
            s.save()


        df = pd.read_csv(csv_path_2)
        df = df.fillna(value=0)
        for index, row in df.iterrows():
            s = PointsUsed(
                date=str(row["Date"].split("/")[2] + "-" + row["Date"].split("/")[0] + "-" + row["Date"].split("/")[1]),
                where=row["Where"],
                what=row["What"],
                dollar_cost=int(row["Dollar Cost"]),
                point_cost=int(row["Point Used"]),
                info=row["Info"],
            )
            s.save()