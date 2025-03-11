FunctionCallConfig = [
            {
                "type": "function",
                "function": {
                    "name": "handle_exit_intent",
                    "description": "当用户想结束对话或需要退出系统时调用",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "say_goodbye": {
                                "type": "string",
                                "description": "和用户友好结束对话的告别语"
                            }
                        },
                        "required": []
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "play_music",
                    "description": "唱歌、听歌、播放音乐方法。比如用户说播放音乐，参数为：random，比如用户说播放两只老虎，参数为：两只老虎",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "song_name": {
                                "type": "string",
                                "description": "歌曲名称，如果没有指定具体歌名则为'random'"
                            }
                        },
                        "required": ["song_name"]
                    }
                }
            },
    {
        "type": "function",
        "function": {
            "name": "set_servo_angle",
            "description": "设置舵机的角度",
            "parameters": {
                "type": "object",
                "properties": {
                    "servo_id": {
                        "type": "integer",
                        "description": "舵机的ID"
                    },
                    "angle": {
                        "type": "integer",
                        "description": "舵机的目标角度"
                    }
                },
                "required": ["servo_id", "angle"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_servo_speed",
            "description": "设置舵机的速度",
            "parameters": {
                "type": "object",
                "properties": {
                    "servo_id": {
                        "type": "integer",
                        "description": "舵机的ID"
                    },
                    "speed": {
                        "type": "integer",
                        "description": "舵机的速度"
                    }
                },
                "required": ["servo_id", "speed"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_temperature",
            "description": "读取温度传感器的数据",
            "parameters": {
                "type": "object",
                "properties": {
                    "sensor_id": {
                        "type": "integer",
                        "description": "温度传感器的ID"
                    }
                },
                "required": ["sensor_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_humidity",
            "description": "读取湿度传感器的数据",
            "parameters": {
                "type": "object",
                "properties": {
                    "sensor_id": {
                        "type": "integer",
                        "description": "湿度传感器的ID"
                    }
                },
                "required": ["sensor_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_led_state",
            "description": "设置LED灯的状态",
            "parameters": {
                "type": "object",
                "properties": {
                    "led_id": {
                        "type": "integer",
                        "description": "LED灯的ID"
                    },
                    "state": {
                        "type": "string",
                        "description": "LED灯的状态，如 'on' 或 'off'"
                    }
                },
                "required": ["led_id", "state"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_led_color",
            "description": "设置LED灯的颜色",
            "parameters": {
                "type": "object",
                "properties": {
                    "led_id": {
                        "type": "integer",
                        "description": "LED灯的ID"
                    },
                    "color": {
                        "type": "string",
                        "description": "LED灯的颜色，如 'red', 'green', 'blue'"
                    }
                },
                "required": ["led_id", "color"]
            }
        }
    }
        ]