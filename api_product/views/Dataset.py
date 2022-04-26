from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
import tensorflow as tf


from api_account.permission import ManagerPermission, UserPermission
from api_base.pagination import CustomPagePagination
from api_base.views import BaseViewSet
from api_product.models import Dataset, Category
from api_product.serializers import DatasetSerializer
from api_product.services import DatasetService


class DatasetViewSet(BaseViewSet):
    queryset = Dataset.objects.all()
    permission_classes = [UserPermission]
    pagination_class = [CustomPagePagination]

    @action(detail=False, methods=['post'])
    def change_model(self, request):
        new_model = tf.keras.models.load_model(request.FILES.get('new_model').temporary_file_path())
        if new_model:
            new_model.save("api_product/constants/classify_model.h5")
            return Response({"detail": "Completed change file model!!"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error_message": "New model is conflict!!"}, status=status.HTTP_400_BAD_REQUEST)
