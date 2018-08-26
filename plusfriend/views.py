from .decorators import bot

@bot
def on_init(request):
    return {'type': 'text'}


@bot
def on_message(request):
    pass

@bot
def on_added(request):
    user_key = request.JSON['user_key']


@bot
def on_block(request, user_key):
    pass


@bot
def on_leave(request, user_key):
    pass