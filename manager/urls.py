from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^home/$', views.index, name='index'),
    url(r'^update/(?P<enterprise_id>\d+)$', views.UpdateEnterpriseView.as_view(), name='update_enterprise'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
	url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),

    url(r'^messages/$', views.MessageView.as_view(), name='messages'),
    url(r'^messages/(?P<message_id>\d+)$', views.MessageView.as_view(), name='delete_message'),
    
    url(r'^budgets/$', views.BudgetView.as_view(), name='solicited_budgets'),
    url(r'^budgets/(?P<budget_id>\d+)$', views.BudgetView().show_budget, name='budget'),
    url(r'^budgets/delete/(?P<budget_id>\d+)$', views.BudgetView.as_view(), name='delete_budget'),
    url(r'^messages/notifications$', views.notifications, name='notifications'),

]