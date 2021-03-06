# -*- coding: utf-8 -*-
# author: itimor

from rest_framework import serializers
from jobs.models import Jobs, JobGroup
from hosts.models import Host

class JobGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobGroup
        fields = ['url', 'id', 'name', 'desc']


class JobsSerializer(serializers.ModelSerializer):
    hosts = serializers.SlugRelatedField(many=True, queryset=Host.objects.all(), slug_field='hostname')
    group = serializers.SlugRelatedField(queryset=JobGroup.objects.all(), slug_field='name')
    class Meta:
        model = Jobs
        fields = ['url', 'id', 'name', 'hosts', 'group', 'jobs_type', 'code_repo', 'code_url', 'code_branch',
                  'deploy_env', 'deploy_script', 'deploy_test', 'deploy_status',
                  'create_time', 'update_time', 'cost_time', 'desc']
        read_only_fields = ('deploy_status', 'publish_time', 'cost_time')