from rest_framework import status
from rest_framework.response import Response
from base.models import Item

def get_item_instance(view_func):
    def _wrapped_view(request, pk, *args, **kwargs):
        # pk = args.get('pk')
        # print(args)
        try:
            instance = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

        return view_func(request, instance, *args, **kwargs)

    return _wrapped_view