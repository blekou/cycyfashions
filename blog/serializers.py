from rest_framework import serializers
from .import models


class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Commentaire
        fields ='__all__'

class ArticleSerializer(serializers.ModelSerializer):
    commentaire = CommentaireSerializer(many=False, required="False")
    class Meta:
        model = models.Article
        fields = '__all__'

        

class TagSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(many=False, required="False")
    class Meta:
        models = models.Tag
        fields = '__all__'


class CategorieSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(many=False, required="False")
    class Meta:
        models = models.Categorie
        fields = '__all__'

