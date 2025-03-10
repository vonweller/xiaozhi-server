from config.logger import setup_logging
import json
from core.handle.abortHandle import handleAbortMessage
from core.handle.helloHandle import handleHelloMessage
from core.handle.receiveAudioHandle import startToChat
from core.handle.iotHandle import handleIotDescriptors, handleIotStatus
from core.handle.sendAudioHandle import send_stt_message
from core.handle.VLHandle import handleVLMessage
TAG = __name__
logger = setup_logging()


async def handleTextMessage(conn, message):
    """处理文本消息"""
    logger.bind(tag=TAG).info(f"收到文本消息：{message}")
    try:
        msg_json = json.loads(message)
        if isinstance(msg_json, int):
            await conn.websocket.send(message)
            return
        if msg_json["type"] == "hello":
            await handleHelloMessage(conn)
        elif msg_json["type"] == "abort":
            await handleAbortMessage(conn)
        elif msg_json["type"] == "listen":
            if "mode" in msg_json:
                conn.client_listen_mode = msg_json["mode"]
                logger.bind(tag=TAG).debug(f"客户端拾音模式：{conn.client_listen_mode}")
            if msg_json["state"] == "start":
                conn.client_have_voice = True
                conn.client_voice_stop = False
            elif msg_json["state"] == "stop":
                conn.client_have_voice = True
                conn.client_voice_stop = True
            elif msg_json["state"] == "detect":
                conn.asr_server_receive = False
                conn.client_have_voice = False
                conn.asr_audio.clear()
                if "text" in msg_json:
                    await startToChat(conn, msg_json["text"])
        elif msg_json["type"] == "iot":
            if "descriptors" in msg_json:
                await handleIotDescriptors(conn, msg_json["descriptors"])
            if "states" in msg_json:
                await handleIotStatus(conn, msg_json["states"])
         ####视觉识别添加能力 image中应该包含图片数据
        elif msg_json["type"] == "VL":
            await handleVLMessage(conn, msg_json)
        ####客户端文字对话能力 inputStr中应该包含text文字数据
        elif msg_json['type'] == 'inputStr':
            print('text:', msg_json['text'])
            text = msg_json['text']
            if len(text) > 0:
                await startToChat(conn, text)
            else:
                await send_stt_message(conn, text)
                conn.executor.submit(conn.chat, text)
    except json.JSONDecodeError:
        await conn.websocket.send(message)
