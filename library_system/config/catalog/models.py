from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.ForeignKey(Author, on_delete= models.CASCADE, related_name= 'books')
    isbn = models.CharField(max_length = 13, unique=True)
    total_copies = models.PositiveIntegerField(default =1)

    def __str__(self):
        return self.title
    
class Member(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(unique = True)
    joined_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.name
    
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name = 'borrow_records')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name = 'borrow_records')
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank= True)

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"

