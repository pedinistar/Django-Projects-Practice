from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def date_time_view(request):
  dt = datetime.datetime.now()
  return HttpResponse(
    f'''
<html>

<head>
  <title>Datetime Application</title>
</head>

<body>
  <h1>Current Date and Time Information</h1>
  <p>Date and Time: {dt}</p>
  <p>Month: {dt.month}</p>
</body>

</html>

    '''
  )