from django.shortcuts import render
from django.views.decorators.http import require_GET
from .forms import LetterForm


@require_GET
def main(request):
    form = LetterForm()
    context = {'form': form}
    return render(request, 'letters/main.html', context)
    