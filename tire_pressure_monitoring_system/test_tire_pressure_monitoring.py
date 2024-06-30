import unittest
from unittest.mock import patch

from tire_pressure_monitoring_system.tire_pressure_monitoring import Alarm


class AlarmTest(unittest.TestCase):
    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)

    def test_alarm_is_on_when_pressure_is_low(self):
        with patch('tire_pressure_monitoring_system.sensor.Sensor.pop_next_pressure_psi_value',
                   return_value=10):
            alarm = Alarm()
            alarm.check()
            self.assertTrue(alarm.is_alarm_on)

    def test_alarm_is_on_when_pressure_is_high(self):
        with patch('tire_pressure_monitoring_system.sensor.Sensor.pop_next_pressure_psi_value',
                   return_value=25):
            alarm = Alarm()
            alarm.check()
            self.assertTrue(alarm.is_alarm_on)

    def test_alarm_is_off_when_pressure_is_normal(self):
        with patch('tire_pressure_monitoring_system.sensor.Sensor.pop_next_pressure_psi_value',
                   return_value=18):
            alarm = Alarm()
            alarm.check()
            self.assertFalse(alarm.is_alarm_on)

    def test_alarm_state_resets_after_normal_pressure(self):
        with patch('tire_pressure_monitoring_system.sensor.Sensor.pop_next_pressure_psi_value',
                   side_effect=[10, 18]):
            alarm = Alarm()
            alarm.check()  # Low pressure, alarm should be on
            self.assertTrue(alarm.is_alarm_on)
            alarm.check()  # Normal pressure, alarm should be off
            self.assertFalse(alarm.is_alarm_on)
