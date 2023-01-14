from rest_framework.viewsets import ModelViewSet
from myportfolio.utils import Helper
from .models import (Userdetailmodel, Usersociallink, Aboutcontent, Experience, Experienceinput, Projecttool, Project, Blog)
from .serializers import (UserdetailmodelSerializer, UsersociallinkSerializer, AboutcontentSerializer, ExperienceSerializer, ExperienceinputSerializer, ProjecttoolSerializer, ProjectSerializer, BlogSerializer)


class UserdetailmodelView(ModelViewSet):
	queryset = Userdetailmodel.objects.all()
	serializer_class = UserdetailmodelSerializer
	http_method_names = ['get']


class UsersociallinkView(ModelViewSet):
	queryset = Usersociallink.objects.all()
	serializer_class = UsersociallinkSerializer
	http_method_names = ['get']


class AboutcontentView(ModelViewSet):
	queryset = Aboutcontent.objects.all()
	serializer_class = AboutcontentSerializer
	http_method_names = ['get']


class ExperienceView(ModelViewSet):
	queryset = Experience.objects.all()
	serializer_class = ExperienceSerializer
	http_method_names = ['get']


class ExperienceinputView(ModelViewSet):
	queryset = Experienceinput.objects.all()
	serializer_class = ExperienceinputSerializer
	http_method_names = ['get']


class ProjecttoolView(ModelViewSet):
	queryset = Projecttool.objects.all()
	serializer_class = ProjecttoolSerializer
	http_method_names = ['get']


class ProjectView(ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	http_method_names = ['get']


class BlogView(ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
	http_method_names = ['get']
