from django.urls import path, include
#from watchlist_app.api.views import movie_list, movie_details used in api crud @app_view
from watchlist_app.api.views import WatchlistListAPIVIEW, WatchlistDetailAPIVIEW, StreamPlatformAPIVIEW, StreamPlatformDetailAPIVIEW, ReviewList, ReviewDetail, ReviewCreate

urlpatterns = [
    
    path('list/', WatchlistListAPIVIEW.as_view(), name='movie-list' ),
    path('<int:pk>', WatchlistDetailAPIVIEW.as_view(), name='movie-detail'),
    
    path('stream/', StreamPlatformAPIVIEW.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAPIVIEW.as_view(), name='stream-detail'),
    
    path('stream/<int:pk>/review', ReviewList.as_view(), name= 'review-list'), #particular movie all reviews
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'), #individual review
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create') #creating a review for x movie.
    
    # path('review/',ReviewList.as_view(), name='review-list'), #with mixins. get all reviews
    # path('review/<int:pk>',ReviewDetail.as_view(), name='review-list'), #with mixins. get single review

]
