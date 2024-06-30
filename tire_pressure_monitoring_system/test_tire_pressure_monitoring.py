import unittest

from tire_pressure_monitoring_system.tire_pressure_monitoring import Alarm, TestSensor


class AlarmTest(unittest.TestCase, Alarm):
    def setUp(self):
        self.Alarm = Alarm()

    def test_alarm_is_off_by_default(self):
        assert not self.Alarm.is_alarm_on

    def test_alarm_is_on_when_pressure_is_low(self):
        self.Alarm._sensor = TestSensor(value=10)
        self.Alarm.check()
        self.assertTrue(self.Alarm.is_alarm_on)

    def test_alarm_is_on_when_pressure_is_high(self):
        self.Alarm._sensor = TestSensor(value=25)
        self.Alarm.check()
        self.assertTrue(self.Alarm.is_alarm_on)

    def test_alarm_is_off_when_pressure_is_normal(self):
        self.Alarm._sensor = TestSensor(value=18)
        self.Alarm.check()
        self.assertFalse(self.Alarm.is_alarm_on)
