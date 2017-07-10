from django.http import HttpResponse
from django.db import connection
from django.http import JsonResponse
from serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.shortcuts import render
from models import *
import json
import numbers

#this is a test comment 
# class hello(APIView):
#     # parser_classes = (JSONParser,)
#     def get(self, request, format=None):
#         # t = request.query_params
#         # x = open_cart.objects.filter()[:10]
#         # print x
#         with connection.cursor() as cursor:
#             cursor.execute("select distinct payment_zone from xyz.open_cart")
#             row = cursor.fetchall()
#             l = []
#             for r in row:
#                 s = TestInit(province=r[0])
#                 l.append(s)
#         serializer = TestSerializer(l, many=True)
#         return Response(serializer.data)

def hello(request):
   return render(request, "chart.html")


# construct the table for cohort chart
class Cohort(APIView):

    def get(self, format=None):
        with connection.cursor() as cursor:
            query = "with population_init as ( select  distinct x.email as unique_id, ( select y.date_added::date from sns_live_copy.oc_order y where  y.email = x.email order by 1 asc limit 1 ) as cohort_date, " \
                    "x.date_added::date as activity_date from sns_live_copy.oc_order x ), population AS ( select  * from  population_init where cohort_date != activity_date ), activity AS " \
                    "( SELECT date_added::DATE AS activity_date, email AS unique_id, cohort_date FROM sns_live_copy.oc_order JOIN population ON population.unique_id = email ), population_agg AS " \
                    "( SELECT cohort_date, COUNT(distinct unique_id) AS total FROM population GROUP BY 1 ) SELECT activity.cohort_date AS DATE, datediff('day', activity.cohort_date, activity_date) " \
                    "AS day, COUNT(distinct unique_id) AS value, total FROM activity JOIN population_agg ON activity.cohort_date = population_agg.cohort_date GROUP BY 1, 2, 4 order by 1, 2, 3, 4"
            cursor.execute(query)
            row = cursor.fetchall()
        x = []
        temp_month = row[0][0].month
        sum_month = 0
        for r in row:
            try:
                next_row_index = row.index(r) + 1
                if row[next_row_index][1] == 0:  # if next is a new date, add the value to the sum_month variable
                    sum_month += r[1]
                    # if new month
                    if temp_month != row[next_row_index][0].month:
                        x.append({'month': str(temp_month) + '-' + str(r[0].year), 'sum': sum_month})
                        sum_month = 0  # set sum_month to 0
                        temp_month = row[next_row_index][0].month  # update the temp_month variable to new month
            except IndexError:
                sum_month += r[1]
                x.append({'time': str(temp_month) + '-' + str(r[0].year), 'sum': sum_month})
                pass
        return Response(x)


def cohort(request):
    return render(request, "cohort.html")


def draw(request):
    with connection.cursor() as cursor:
        query = "with population_init as ( select  distinct x.email as unique_id, ( select y.date_added::date from sns_live_copy.oc_order y where  y.email = x.email order by 1 asc limit 1 ) as cohort_date, " \
                "x.date_added::date as activity_date from sns_live_copy.oc_order x ), population AS ( select  * from  population_init where cohort_date != activity_date ), activity AS " \
                "( SELECT date_added::DATE AS activity_date, email AS unique_id, cohort_date FROM sns_live_copy.oc_order JOIN population ON population.unique_id = email ), population_agg AS " \
                "( SELECT cohort_date, COUNT(distinct unique_id) AS total FROM population GROUP BY 1 ) SELECT activity.cohort_date AS DATE, datediff('day', activity.cohort_date, activity_date) " \
                "AS day, COUNT(distinct unique_id) AS value, total FROM activity JOIN population_agg ON activity.cohort_date = population_agg.cohort_date GROUP BY 1, 2, 4 order by 1, 2, 3, 4"
        cursor.execute(query)
        row = cursor.fetchall()
    x = []
    temp_month = row[0][0].month
    sum_month = 0
    for r in row:
        try:
            next_row_index = row.index(r) + 1
            if row[next_row_index][1] == 0:  # if next is a new date, add the value to the sum_month variable
                sum_month += r[1]
                # if new month
                if temp_month != row[next_row_index][0].month:
                    x.append({'month': [temp_month, r[0].year], 'sum': sum_month})
                    sum_month = 0  # set sum_month to 0
                    temp_month = row[next_row_index][0].month  # update the temp_month variable to new month
        except IndexError:
            sum_month += r[1]
            x.append({'time': [temp_month, r[0].year], 'sum': sum_month})
            pass
    return JsonResponse(x, safe=False)


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def test(request):
    query = request.GET.get('query')
    with connection.cursor() as cursor:
        cursor.execute(query)
        # select SUM(order_total) AS sum_order_quantity, payment_zone AS province from xyz.open_cart_filtered GROUP BY payment_zone
        # row = cursor.fetchall()
        row = dictfetchall(cursor)
        for r in row:
            for obj in r:
                print(isinstance(r[obj], unicode))
                if (not (isinstance(r[obj], str) or isinstance(r[obj], unicode))) and (r[obj] is not None):
                    print(r[obj])
                    r[obj] = float(r[obj])
        x = json.dumps(row)
    return HttpResponse(x,  content_type='application/json')
