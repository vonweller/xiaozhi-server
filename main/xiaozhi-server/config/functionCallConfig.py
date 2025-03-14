FunctionCallConfig = [
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