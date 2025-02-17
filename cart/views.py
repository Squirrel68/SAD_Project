from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from book.models import Book
from .models import Cart

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, book=book)

    if not created:
        cart_item.quantity += 1  # Nếu đã có trong giỏ hàng, tăng số lượng
    cart_item.save()

    messages.success(request, f"Đã thêm {book.title} vào giỏ hàng.")
    return redirect("cart:view_cart")

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)

    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "total_price": total_price
    })

@login_required
def update_cart(request, book_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        cart_item = get_object_or_404(Cart, user=request.user, book_id=book_id)
        cart_item.quantity = max(1, quantity)
        cart_item.save()
        messages.success(request, "Cập nhật giỏ hàng thành công.")
    return redirect("cart:view_cart")

@login_required
def remove_from_cart(request, book_id):
    cart_item = get_object_or_404(Cart, user=request.user, book_id=book_id)
    cart_item.delete()
    messages.success(request, "Đã xóa sản phẩm khỏi giỏ hàng.")
    return redirect("cart:view_cart")
