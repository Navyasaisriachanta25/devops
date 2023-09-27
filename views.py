from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserDetails
from .serializers import UserDetailsSerializer,loginSerializer
from rest_framework import generics
# @api_view(['POST'])
# def create_user(request):
#     print("this")
#     serializer = UserDetailsSerializer(data=request.data)
#     print("dfg")
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class dashboardpost(generics.GenericAPIView):
    serializer_class = UserDetailsSerializer
    def post(self,request):
        g = UserDetailsSerializer(data=request.data)
        g.is_valid(raise_exception=True)
        h = g.save()
        return Response(UserDetailsSerializer(h).data)


class dataread(generics.GenericAPIView):
    serializer_class = UserDetailsSerializer
    
def get_user(request, userid): 
    try:
        user = UserDetails.objects.get(userid=userid)
        serializer = UserDetailsSerializer(user)
        return Response(serializer.data)
    except UserDetails.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    
    
    
    
class login(generics.GenericAPIView):
    serializer_class = loginSerializer
    def post(self,request):
        userid=request.data.get("userid")
        password=request.data.get("password")
        x=UserDetails.objects.get(userid=userid)
        if x.password==password:
            return Response({
                "message":"login Success",
                "result":loginSerializer(x).data,
                "status":200
            })
        else:
            return Response({
                "message":"login Failed",
                "status":400
            })