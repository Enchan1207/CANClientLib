#
# CANクライアントライブラリ
#
import can
from .canBusListener import Listener

# RPi.GPIOが存在するか確認する
isPiImplemented = False
try:
    import RPi.GPIO as GPIO
    isPiImplemented = True
except ImportError:
    print("Couldn't import RPi.GPIO. Some features about Raspberry Pi will be limited.")

class Client():
    # Initializer 何も設定しないと仮想CANが立ち上がる
    def __init__(self, channel="test", bustype="virtual", bitrate=500000, intpin=None, filter=None) -> None:
        # GPIO初期設定
        if isPiImplemented:
            if intpin is not None:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(intpin, GPIO.IN)
            else:
                print("\033[31mERROR:\033[0m None has passed to argument intpin. Please pass valid pin value.")

        # インタフェース初期化
        self.canBus = can.interface.Bus(channel, bustype=bustype, bitrate = bitrate, canfilters = filter)

    # 受信コールバックを登録する
    def attachCallback(self, callback):
        self.listener = Listener(callback)
        self.notifier = can.Notifier(self.canBus, [self.listener,])
    
    # 受信コールバックの登録を解除する
    def detachCallback(self):
        self.notifier.remove_listener(self.listener)

    # CANフレームを送信する
    def sendFrame(self, id, data = None):
        if data is not None:
            message = can.Message(data = data, arbitration_id = id)
            self.canBus.send(message)
