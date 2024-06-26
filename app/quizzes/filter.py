import django_filters
from django.db.models import QuerySet

from .models import Test


class TestFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="contains")

    tag = django_filters.CharFilter(method="filter_search", label="find by tags(values separated by space)")

    def filter_search(self, queryset: QuerySet, name: str, value: str):
        return queryset.filter(tag__name__in=value.split(" "))

    ordering = django_filters.OrderingFilter(
        fields=(("name", "test name"), ("created", "created")),
    )

    class Meta:
        model = Test
        fields = ["name"]
