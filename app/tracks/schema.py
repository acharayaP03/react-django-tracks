"""
    Import graphene first then import graphene django 
"""

import graphene
from graphene_django import DjangoObjectType

""" Rather than rewriting the entire model within track lets import it"""

from .models import Track

class TrackType(DjangoObjectType):
    class Meta:
        model = Track

class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)

    def resolve_tracks(self, info):
        """ return all tracks from the Track model """
        return Track.objects.all()