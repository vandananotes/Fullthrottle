from rest_framework.views import APIView, Response
from user.serializer import UserSerializer

class AddUserAPI(APIView):
    def post(self, request):
        input_json = request.data
        output_json = {}
        json_function_output_var = AddUserJson. \
            add_user_Json_function(self, input_json)
        output_json['Payload'] = json_function_output_var
        return Response(output_json)


class AddUserJson(APIView):
    def add_user_Json_function(self, request):
        input_json = request
        output_json = {}
        try:

            add_user_param= {}
            add_user_param['real_name'] = input_json['real_name']
            add_user_param['tz'] = input_json['tz']
            add_user_param['activity_periods'] = input_json['activity_periods']
            serializer_var = UserSerializer(data=add_user_param)
            if serializer_var.is_valid(raise_exception=True):
                serializer_var.save()
                output_json['Status'] = "Success"
                output_json['Message'] = "Successfully add user."
                output_json['user'] = serializer_var.data
                return output_json

        except Exception as ex:
            output_json['Status'] = "Failure"
            output_json['Message'] = "Error occur while add user."
            return output_json








