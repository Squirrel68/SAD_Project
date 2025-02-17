from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from book.models import Book

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Khách hàng có thể là ẩn danh
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Sản phẩm (sách) trong giỏ hàng
    quantity = models.PositiveIntegerField(default=1)  # Số lượng sách
    added_at = models.DateTimeField(auto_now_add=True)  # Ngày thêm vào giỏ

    def __str__(self):
        return f"{self.quantity} x {self.book.title} - {self.user.username if self.user else 'Guest'}"

    def get_total_price(self):
        return self.quantity * self.book.price  # Tính tổng giá theo số lượng
