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
    thumbnail = models.ImageField(upload_to='%Y/%m/%d/')
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



class ArticleVote(models.Model):
    article = models.OneToOneField(Article, 
        on_delete=models.CASCADE, related_name='votes')
    

    def __str__(self):
        return self.article.title + ' votes'


    def upvotes_count(self):
        return self.upvotes.count()


    def downvotes_count(self):
        return self.downvotes.count()



class ArticleUpvote(models.Model):
    vote = models.ForeignKey(ArticleVote, 
        on_delete=models.CASCADE, related_name='upvotes')
    user = models.ForeignKey(User, 
        on_delete=models.CASCADE, related_name='upvotes')


    def __str__(self):
        return self.vote.article.title + ' upvote by ' + self.user.username



class ArticleDownvote(models.Model):
    vote = models.ForeignKey(ArticleVote, 
        on_delete=models.CASCADE, related_name='downvotes')
    user = models.ForeignKey(User, 
        on_delete=models.CASCADE, related_name='downvotes')


    def __str__(self):
        return self.vote.article.title + ' downvote by ' + self.user.username



class Comment(models.Model):
    user = models.ForeignKey(User, 
        on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, 
        on_delete=models.CASCADE, related_name='comments')


    def __str__(self):
        return f'Comment {self.pk} for article {self.article}'



class Reply(models.Model):
    user = models.ForeignKey(User, 
        on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, 
        on_delete=models.CASCADE, related_name='replies')


    def __str__(self):
        return f'Reply {self.pk} for article {self.comment.article}'