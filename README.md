To run locally, do the usual:

#. Create a Python 3.6 virtualenv Django 1.11 version installed

#. Create project projectname (Class Based View Project)
   
    django-admin startproject cbv_companyproject

#. Go to the project dir 
   
    cd cbv_companyproject

#. Create application inside main project directory 

    py manage.py startapp testapp

#. Configure the templatefile and staticfile inside settings.py 

#.Create template folder and static folder, inside static folder create css folder and image folder, insert the required images, Here sqlite used as default database

#. Create class company with attributes

#. To convert model class to sql code use makemigrations 

    py manage.py makemigrations

#. To create table inside database 

    py manage.py migrate

#. Create superuser to connect with database 

    py manage.py createsuperuser

#. Register the model class inside admin.py file
   
    admin.site.register(model,modeladmin)

#. Define view function inside views.py 

    
#. Here CRUD operation has been implemented


#. Four default template file has been implemented for four different operation
    For List view - default template file name- company_list.html
                    default context object - company_list
                    
     For Detail view - default template file name- company_detail.html
                    default context object - company or object
                    
     For Create view - default template form name- company_form.html
                    
     For Delete view - default template file name- company_confirm_delete.html
                    
                    

#. Define view function inside urls.py
   
    from django.conf.urls import url
    from django.contrib import admin
    from testapp import views
    urlpatterns = [
       url(r'^admin/', admin.site.urls),
       url(r'^$', views.CompanyListView.as_view(),name='companies'),
       url(r'^(?P<pk>\d+)/$', views.CompanyDetailView.as_view(),name='detail'),
       url(r'^create/', views.CompanyCreateView.as_view()),
       url(r'^update/(?P<pk>\d+)/$', views.CompanyUpdateView.as_view()),
       url(r'^delete/(?P<pk>\d+)/$', views.CompanyDeleteView.as_view()),

#. To run server 

    py manage.py runserver
