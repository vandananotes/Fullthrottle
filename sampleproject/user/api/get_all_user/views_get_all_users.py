from rest_framework.views import APIView, Response
from user.models  import  User
from user.serializer import UserSerializer,ActivityPeriodAndUserSerializer
import  json

class GetallUserAPI(APIView):
        def post(self,request):
            input_json = request.data
            output_json = {}
            json_function_output_var =GetallUserJson.\
                get_all_user_Json_function(self,input_json)
            output_json['ok'] =True
            output_json['Members']=json_function_output_var
            return Response(output_json)

class GetallUserJson(APIView):
    def get_all_user_Json_function(self,request):
            input_json = request
            output_json={}
            try:


                # primary_key = input_json['id']
                # get_user_info = User.objects.select_related('activity_periods').get(pk=primary_key)
                # serializer_var = ActivityPeriodAndUserSerializer(get_user_info)
                serializer_var = ActivityPeriodAndUserSerializer(User.objects.all(),many=True)
                output_json = serializer_var.data
                return output_json

            except Exception as ex:
                output_json['Status'] = "Failure"
                output_json['Message'] = "Error occur while get user."
                return output_json








                        