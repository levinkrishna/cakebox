from django.urls import path
from cakebox.views import SignUpView,SignInView,CategoryCreateView,remove_category,CakeCreateView,CakeListView,CakeUpdateView,remove_cakeview,CakeVarientCreateView,CakeDetailView,CakeVarientUpdateView,remove_varient,OfferCreateView,offer_delete_view,sign_out_view


urlpatterns=[
    path("register/",SignUpView.as_view(),name="signup"),
    path("",SignInView.as_view(),name="signin"),
    path("categories/add",CategoryCreateView.as_view(),name="add-category"),
    path("categories/<int:pk>/remove",remove_category,name="remove-category"),
    path("cakes/add",CakeCreateView.as_view(),name="cake-add"),
    path("cakes/all",CakeListView.as_view(),name="cake-list"),
    path("cakes/<int:pk>/change",CakeUpdateView.as_view(),name="cake-change"),
    path("cloths/<int:pk>/remove",remove_cakeview,name="cake-remove"),
    path("cakes/<int:pk>/vaients/add",CakeVarientCreateView.as_view(),name="add-varient"),
    path("cakes/<int:pk>/",CakeDetailView.as_view(),name="cake-detail"),
    path("varients/<int:pk>/change/",CakeVarientUpdateView.as_view(),name="update-varient"),
    path("varients/<int:pk>/remove/",remove_varient,name="remove-varient"),
    path("varient/<int:pk>/offer/add",OfferCreateView.as_view(),name="offer-add"),
    path("offers/<int:pk>/remove",offer_delete_view,name="delete-offer"),
    path("logout/",sign_out_view,name="signout")



    
]