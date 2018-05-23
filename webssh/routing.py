# -*- coding: utf-8 -*-

from channels import route_class, route
# channel_routing = [] #初始化定义channel_routing，以免sdj.routing --- cmdb.consumers --- cmdb.interactive --- sdj.asgi.channel_layer --- sdj.routing 循环import导致出错未定义channel_routing。

# print 1,'sdj.routing'
from cmdb.consumers import webterminal#,CommandExecute

# The channel routing defines what channels get handled by what consumers,
# including optional matching on message attributes. In this example, we route
# all WebSocket connections to the class-based BindingConsumer (the consumer
# class itself specifies what channels it wants to consume)



# channel_routing.extend([
#     route_class(webterminal,path = r'^/ws'),
#     # route_class(CommandExecute,path= r'^/execute'),
# ])



channel_routing = [
    route_class(webterminal,path = r'^/ws'),
    # route_class(CommandExecute,path= r'^/execute')
]
