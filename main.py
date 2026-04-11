import tornado.ioloop
import tornado.web
from core.config import config
from core.logger import setup_logger
from server.handlers import CreateRoomHandler, GameWebSocketHandler
from server.manager import RoomManager


def make_app():
    room_manager = RoomManager()

    import os
    print("STATIC_PATH =", config.STATIC_PATH)
    print("INDEX EXISTS =", os.path.exists(os.path.join(config.STATIC_PATH, "index.html")))

    return tornado.web.Application([
        (r"/api/create-room", CreateRoomHandler, {"room_manager": room_manager}),
        (r"/ws", GameWebSocketHandler, {"room_manager": room_manager}),
        (r"/(.*)", tornado.web.StaticFileHandler, {
            "path": config.STATIC_PATH,
            "default_filename": "index.html"
        }),
    ])


if __name__ == "__main__":
    setup_logger()
    app = make_app()
    app.listen(config.PORT, config.LISTEN_ADDRESS)
    print(f"Servidor rodando em http://localhost:{config.PORT}")
    tornado.ioloop.IOLoop.current().start()