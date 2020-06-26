from django.core.exceptions import ValidationError
from collections import Counter
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def lambda_function(request):
    dados = request.data.get('question')

    if dados is None:
        raise ValidationError('Not empty')

    answer = []
    for item, count in Counter(dados).most_common():
        for _ in range(count):
            answer.append(item)
    return Response({
        'solution': answer
    }, status=status.HTTP_200_OK)
