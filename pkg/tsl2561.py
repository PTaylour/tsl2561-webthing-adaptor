import board
import busio
import adafruit_tsl2561


def get_devices():
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_tsl2561.TSL2561(i2c)
    return [{'_id': 'tsl2561-1', 'sensor': sensor}]
