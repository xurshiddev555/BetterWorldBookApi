
from rest_framework.pagination import PageNumberPagination, CursorPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100

class CustomCursorPagination(CursorPagination):
    ordering = '-created_at'