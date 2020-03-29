from rest_framework.views import APIView, Response
from user.models  import  ActivityPeriod
from user.serializer import ActivityPeriodSerializer

class AddActivatityPeriodAPI(APIView):
        def post(self,request):
            input_json = request.data
            output_json = {}
            json_function_output_var =AddActivatityPeriodJson.\
                add_activatity_period_Json_function(self,input_json)
            output_json['Payload']=json_function_output_var  
            return Response(output_json)

class AddActivatityPeriodJson(APIView):
    def add_activatity_period_Json_function(self,request):
            input_json = request
            output_json={}

            try:
                # add_activity_period = {}
                # add_activity_period['start_time'] = input_json['start_time']
                # add_activity_period['end_time'] = input_json['end_time']
                serializer_var = ActivityPeriodSerializer(data=input_json)
                if serializer_var.is_valid(raise_exception=True):
                    serializer_var.save()
                    output_json['Status'] = "Success"
                    output_json['Message'] = "Successfully add activity period."
                    return output_json

            except Exception as ex:
                output_json['Status'] = "Failure"
                output_json['Message'] = "Error occur while add activity."
                return output_json








                        