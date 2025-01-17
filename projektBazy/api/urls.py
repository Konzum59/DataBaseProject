from django.urls import path
from .views import ListingsView, UserAddressesView, CreateListingView, ReviewViewSet
from . import views
urlpatterns = [
     path('',views.getData),
    path('categories/',views.getCategory),
     path('add/', views.addCategory),
     path('login/', views.login),
    path('signup/', views.signup),
    path('test_token/', views.test_token),
     path('logout/', views.logout),
    #{ "title":"Toa gali","description":"Does it count as water toy?","price":50,"location":"wroclaw","category":1 }
    path('postListing/', views.post_listing),
     path('postAddress/', views.add_address),
    path('user/<int:user_id>/category/<int:category_id>/', ListingsView.as_view(), name='user-category-listings'),
    path('user/<int:user_id>/', ListingsView.as_view(), name='user-listings'),   
    path('category/<int:category_id>/', ListingsView.as_view(), name='category-listings'),
    path('listing/<int:listing_id>/cancel/', views.cancel_listing, name='cancel_listing'),
    path('listings/<int:listing_id>/', views.get_listing, name='listing'),
    path('user/<int:user_id>/addresses/', UserAddressesView.as_view(), name='user-addresses'),
    path('transactions_all/', views.get_all_transactions, name='all-transactions'),
    path('transactions/', views.create_transaction, name='create-transaction'),
    path('transactions/<int:transaction_id>/update/', views.update_transaction_status, name='update-transaction-status'),
    path('listings/create/', CreateListingView.as_view(), name='create-listing'),
    path('addmessage/<int:listing_id>/<int:chat_id>', views.add_chat_message, name='add-chat-message'),
    path('addmessage/<int:listing_id>', views.add_chat_message, name='add-chat-message'),
    path('chats/<int:listing_id>', views.get_chats, name='listing-chats'),
    path('chats/', views.get_all_chats, name='all-chats'),
    path('chats/create/', views.create_chat, name='create-chat'),
    path('messages/<int:chat_id>', views.get_messages, name='chat-messages'),
    path('viewedmessage/<int:message_id>', views.set_message_viewed, name='message-viewed'),
    path('reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='review-detail'),
    path('reviews/<int:pk>/user-reviews/', ReviewViewSet.as_view({'get': 'user_reviews'}), name='user-reviews'),
    path('reviews/<int:pk>/average-rating/', ReviewViewSet.as_view({'get': 'average_rating'}), name='average-rating'),
]
#Do something like this to test it
#http://127.0.0.1:8000/postAddress/
#and for example put something like this: 
#   {
#       "country": "Poland",
#       "town": "Wrocław",
#       "street": "Świdnicka",
#       "postal_code": 50029,
#       "building_number": 15,
#       "id": 1
#   }