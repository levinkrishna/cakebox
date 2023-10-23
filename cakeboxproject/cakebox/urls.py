from django.urls import path
from cakebox.views import SignUpView,SignInView,CategoryCreateView,remove_category,CakeCreateView,CakeListView,CakeUpdateView,remove_cakeview


urlpatterns=[
    path("register/",SignUpView.as_view(),name="signup"),
    path("",SignInView.as_view(),name="signin"),
    path("categories/add",CategoryCreateView.as_view(),name="add-category"),
    path("categories/<int:pk>/remove",remove_category,name="remove-category"),
    path("cakes/add",CakeCreateView.as_view(),name="cake-add"),
    path("cakes/all",CakeListView.as_view(),name="cake-list"),
    path("cakes/<int:pk>/change",CakeUpdateView.as_view(),name="cake-change"),
    path("cloths/<int:pk>/remove",remove_cakeview,name="cake-remove")



    
]