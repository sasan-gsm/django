from django.shortcuts import redirect


def redirect_root(request):
    return redirect('app1_post_list')