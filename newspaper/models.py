from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name



class Subcategory(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, 
        on_delete=models.CASCADE, related_name='subcategories')


    def __str__(self):
        return self.name



class Article(models.Model):
    thumbnail = models.ImageField(upload_to='newspaper/%Y/%m/%d/')
    category = models.ForeignKey(Category, 
        on_delete=models.CASCADE, related_name='articles')
    subcategory = models.ForeignKey(Subcategory, 
        on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()


    def __str__(self):
        return f'{self.title} by {self.author}'



class Comment(models.Model):
    user = models.ForeignKey(User, 
        on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, 
        on_delete=models.CASCADE, related_name='comments')


    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
        vote = CommentVote.objects.create(comment=self, 
            upvotes=0, downvotes=0)


    def __str__(self):
        return f'Comment {self.pk} for article {self.article}'


    



class Reply(models.Model):
    user = models.ForeignKey(User, 
        on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, 
        on_delete=models.CASCADE, related_name='replies')


    def save(self, *args, **kwargs):
        super(Reply, self).save(*args, **kwargs)
        ReplyVote.objects.create(reply=self,
            upvotes=0, downvotes=0)


    def __str__(self):
        return f'Reply {self.pk} for article {self.comment.article}'



class CommentVote(models.Model):
    comment = models.OneToOneField(Comment, 
        on_delete=models.CASCADE, related_name='votes')
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()


    def __str__(self):
        return f"Up {self.upvotes} - Down {self.downvotes}"



class ReplyVote(models.Model):
    reply = models.OneToOneField(Reply,
        on_delete=models.CASCADE, related_name='votes')
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()


    def __str__(self):
        return f"Up {self.upvotes} - Down {self.downvotes}"