# Tuya Energy - Home Assistant Custom Component

A comprehensive Tuya integration for Home Assistant with enhanced energy monitoring capabilities. This custom component provides full Tuya device support including energy monitoring, power management, and device control.

## About This Project

This component is based on the official Home Assistant Tuya integration with enhanced energy monitoring capabilities. It provides a complete Tuya device solution while the official integration review is pending.

### Original Code Attribution
- **Original Tuya Integration**: Home Assistant Team
- **License**: Apache License 2.0
- **Source**: https://github.com/home-assistant/core/tree/dev/homeassistant/components/tuya

### Enhancements
- **Energy Monitoring**: Enhanced energy monitoring with cumulative and incremental reporting modes
- **State Restoration**: Automatic state restoration for energy sensors
- **Device Configuration**: Per-device energy reporting mode configuration
- **Diagnostic Features**: Detailed attributes for troubleshooting

## Features

- **Complete Tuya Device Support**: All Tuya device types including switches, lights, climate, sensors, and more
- **Enhanced Energy Monitoring**:
  - Real-time power, current, voltage monitoring
  - Energy consumption tracking
  - Support for both cumulative and incremental energy reporting modes
  - State restoration for energy sensors
  - Diagnostic attributes for troubleshooting
- **Device-Level Configuration**: Configure energy reporting mode per device
- **Auto-Discovery**: Automatic device discovery and setup
- **Cloud Integration**: Secure cloud-based device communication
- **MQTT Support**: Real-time device status updates
- **Multi-Platform Support**: All Tuya device platforms

## Supported Devices

### Energy Monitoring

- **Smart Plugs**: Power monitoring and control
- **Energy Monitors**: Power, current, voltage, energy consumption
- **Smart Meters**: Energy consumption tracking

### Lighting

- **Smart Bulbs**: RGB, tunable white, dimmable
- **Smart Switches**: On/off control
- **Dimmers**: Brightness control
- **Ceiling Lights**: Various types and configurations

### Climate & Comfort

- **Thermostats**: Temperature control
- **Air Conditioners**: Cooling and heating
- **Heaters**: Electric heaters
- **Fans**: Various fan types and speeds
- **Humidifiers**: Humidity control
- **Dehumidifiers**: Moisture removal

### Security & Safety

- **Cameras**: IP cameras with motion detection
- **Alarm Systems**: Security alarms
- **Sensors**: Motion, door/window, smoke, gas
- **Sirens**: Audio alarms

### Appliances

- **Vacuum Cleaners**: Robot vacuums
- **Valves**: Water control valves
- **Covers**: Garage doors, curtains, blinds
- **Pumps**: Water pumps

### Control & Automation

- **Switches**: Various switch types
- **Buttons**: Programmable buttons
- **Numbers**: Numeric controls
- **Selects**: Dropdown selections
- **Events**: Event triggers

## Installation

### HACS (Recommended)

1. Make sure you have [HACS](https://hacs.xyz/) installed
2. Add this repository as a custom repository in HACS
3. Search for "Tuya Energy" in the HACS store
4. Click "Download"
5. Restart Home Assistant

### Manual Installation

1. Download the latest release
2. Extract the `custom_components` folder to your Home Assistant configuration directory
3. Restart Home Assistant

## Configuration

### UI Configuration (Recommended)

1. Go to **Settings** > **Devices & Services**
2. Click **Add Integration**
3. Search for "Tuya Energy"
4. Follow the setup wizard

### YAML Configuration

```yaml
tuya_energy:
  username: your_tuya_username
  password: your_tuya_password
  country_code: your_country_code
  biz_type: smart_life  # or tuya
  polling_interval: 30
```

## Energy Reporting Modes

This component supports two energy reporting modes:

### Cumulative Mode (Default)

- Device reports total energy consumption
- Values increase over time
- Suitable for most energy monitoring devices

### Incremental Mode

- Device reports energy deltas
- Component accumulates energy values
- Provides state restoration for continuous monitoring
- Includes timestamp-based deduplication

### Device-Level Configuration

You can configure the energy reporting mode for each device:

1. Go to **Settings** > **Devices & Services**
2. Find your Tuya Energy integration
3. Click **Configure**
4. Select **Options**
5. Choose the energy reporting mode for each device

## Usage Examples

### Energy Monitoring Dashboard

```yaml
type: entities
entities:
  - entity: sensor.living_room_power
  - entity: sensor.living_room_current
  - entity: sensor.living_room_voltage
  - entity: sensor.living_room_energy
title: Energy Monitor
```

### Automation Example

```yaml
automation:
  - alias: "High Power Alert"
    trigger:
      platform: numeric_state
      entity_id: sensor.living_room_power
      above: 2000
    action:
      service: notify.mobile_app
      data:
        message: "High power consumption detected!"
```

### Light Control Example

```yaml
automation:
  - alias: "Turn on lights at sunset"
    trigger:
      platform: sun
      event: sunset
    action:
      service: light.turn_on
      target:
        entity_id: light.living_room
      data:
        brightness: 100
        color_temp: 2700
```

## Troubleshooting

### Common Issues

1. **Authentication Failed**: Check your Tuya credentials and country code
2. **Devices Not Found**: Ensure devices are added to your Tuya account
3. **Energy Values Not Updating**: Check the energy reporting mode configuration
4. **Devices Offline**: Check device connectivity in Tuya app

### Debug Logging

Add to your `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.tuya_energy: debug
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

This component is based on the official Tuya integration with enhanced energy monitoring capabilities. Special thanks to the Tuya development team and the Home Assistant community.
