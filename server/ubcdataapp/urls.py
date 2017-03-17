from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # TODO: Need to check expected JSON format on Client side

    # TODO: retrieve projects between startIndex and

    # TODO: Version Node has List of Projects. { Version : NodeID }
    # e.g. { "10.0.10" : "317aad06-7ed0-4744-a578-d3e0a9657ed1"}

    # TODO: License Node has List of Projects. { License : NodeId}
    # e.g. { 11 : "317aad06-7ed0-4744-a578-d3e0a9657ed1"}

    # TODO: Send List of Projects
    # e.g. {    "id" : "317aad06-7ed0-4744-a578-d3e0a9657ed1",
    #           "dws": "c019ab29f45a31e456dda5174791b935",
    #           "dns": "38f259e333b580340f80c463ecd8305f",
    #           "so" : "d41d8cd98f00b204e9800998ecf8427e"   }
]
