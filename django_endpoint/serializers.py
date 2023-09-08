from rest_framework import serializers
from .models import Endpoint

class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        fields=["slack_name","track","github_file_url","github_repo_url","status_code"]