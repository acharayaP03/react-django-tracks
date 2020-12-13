""" 
    This a general schema will create a general seperation of concern

"""

import graphene
import tracks.schema

class Query(tracks.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)