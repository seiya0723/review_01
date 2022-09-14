from django.db import models
from django.utils import timezone


#TIPS:travelは一般的な旅行、tourは具体的にどこかを一巡する旅行であるため、今回はTourモデルと命名
class Tour(models.Model):

    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    name        = models.CharField(verbose_name="ツアー名",max_length=100)
    description = models.CharField(verbose_name="ツアー説明文",max_length=500)

    price       = models.IntegerField(verbose_name="ツアー料金")

    
    #TODO:ここに旅行のサムネイル画像のフィールドを(ImageField)
    #https://noauto-nolife.com/post/django-fileupload/


class Review(models.Model):

    dt      = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    comment = models.CharField(verbose_name="コメント",max_length=500)

    #ツアーに対してのレビューなので、Tourと1対多のリレーションを組む
    #https://noauto-nolife.com/post/django-models-foreignkey/
    #tour    = models.ForeignKey(Tour, verbose_name="ツアー", on_delete=models.CASCADE)

    #TODO:ここに星評価(IntegerField)
    #https://noauto-nolife.com/post/django-template-integer-for-loop/

    

    def __str__(self):
        return self.comment
