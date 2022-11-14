from django.db import models

# membuat model Blogs
class Blogs(models.Model):
	title = models.CharField(max_length=100)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True) # auto_now_add adalah fungsi dari django

	# menampilkan title saat memanggil Blogs.objects.all() di dalam shell
	def __str__(self):
		return self.title

# buat class comment
class Comment(models.Model):
	blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)