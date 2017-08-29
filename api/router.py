# -*- coding: utf-8 -*-
# author: itimor

from rest_framework.routers import DefaultRouter
from api.hosts.views import HostViewSet, HostGroupViewSet, SaltServerViewSet
from api.jobs.views import JobsViewSet, JobGroupViewSet
from api.users.views import UserViewSet, GroupViewSet, RoleViewSet
from api.tools.views import DutyViewSet, UploadViewSet

router = DefaultRouter()
router.register(r'hosts', HostViewSet)
router.register(r'hostgroups', HostGroupViewSet)
router.register(r'ansible', SaltServerViewSet)
router.register(r'upload', UploadViewSet)
router.register(r'jobs', JobsViewSet)
router.register(r'jobgroups', JobGroupViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'dutys', DutyViewSet)