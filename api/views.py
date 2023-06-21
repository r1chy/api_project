from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
import subprocess

@api_view(['POST'])
def getDatafromJson(request):
    data = json.loads(request.body)
    targeturl = data['url']
    #hier muss der curl passieren und damit ändert sich dann die response
    #curl
    rc = subprocess.check_call(['/home/rich/project/myproject/api/testcurl.sh', targeturl])
    
    return rc