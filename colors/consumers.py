from channels.generic.websocket import AsyncJsonWebsocketConsumer

"""
This uses the AsyncJsonWebsocketConsumer where the JSON part is important

Also for broadcasts you have to look at channel layers
"""

class ColorConsumer(AsyncJsonWebsocketConsumer):
    pass  # Replace this stuff
