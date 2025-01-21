from rest_framework import mixins
from .models import Category
from .serializers import ContentSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import exceptions


class PDFFileTypeMixin(mixins.UpdateModelMixin, mixins.CreateModelMixin):
    def check_file_type(self, serializer: ContentSerializer):
        document: InMemoryUploadedFile = serializer.validated_data.get('document') # type: ignore
        if document.content_type != 'application/pdf':
            raise exceptions.ValidationError("Document can only be of type 'PDF'")

    def perform_create(self, serializer: ContentSerializer):
        self.check_file_type(serializer)
        serializer.save(author=self.request.user) # type: ignore
    
    def perform_update(self, serializer):
        self.check_file_type(serializer)
        serializer.save(author=self.request.user) # type: ignore
